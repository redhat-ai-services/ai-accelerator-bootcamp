import os
import kfp.compiler
from kfp import dsl

kubeflow_endpoint = os.environ["KUBEFLOW_ENDPOINT"]
#kubeflow_endpoint = 'https://ds-pipeline-dspa.parasol-insurance.svc.cluster.local:8443'
base_image = os.getenv(
    "BASE_IMAGE",
    "image-registry.openshift-image-registry.svc:5000/openshift/python:latest")


@dsl.component(
    base_image=base_image,
    packages_to_install=["requests~=2.32.0", "zipp~=3.19.0"],
)
def download_data(dataset_type: str,
                  datasets: dsl.Output[dsl.Dataset]):
    import requests
    import zipfile

    URL = f"https://rhods-public.s3.amazonaws.com/sample-data/accident-data/accident-{dataset_type}.zip"

    print("Downloading file...")
    response = requests.get(URL, stream=True)
    block_size = 1024
    with open(f'./accident-{dataset_type}.zip', 'wb') as f:
        for data in response.iter_content(block_size):
            f.write(data)

    print("Unzipping file...")
    with zipfile.ZipFile(f'./accident-{dataset_type}.zip', 'r') as zip_ref:
        zip_ref.extractall(path=datasets.path)
    print("Done!")

@dsl.component(
    base_image=base_image,
    packages_to_install=["ultralytics~=8.2.0", "opencv-contrib-python-headless~=4.10.0"],
)
def train_model(datasets: dsl.Input[dsl.Dataset],
                model_onnx: dsl.Output[dsl.Model]):
    import os
    import shutil
    import datetime
    from ultralytics import YOLO

    print("setting the symlink for the datasets")
    os.symlink(datasets.path, "/opt/app-root/src/datasets")

    # load a pretrained model (recommended for training)
    print("using a base model to start the training")
    model = YOLO('yolov8m.pt')
    print("training the model")
    model.train(data=f'{datasets.path}/accident-sample/data.yaml',
                epochs=1, imgsz=640, batch=2)

    print("saving the file as onnx")

    # create runs/detect/train/weights/best.onnx
    YOLO("/opt/app-root/src/runs/detect/train/weights/best.pt").export(
        format="onnx")

    # save best.onnx as accident-detection_{timestamp}.onnx
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    os.makedirs(model_onnx.path, exist_ok=True)
    shutil.copy('/opt/app-root/src/runs/detect/train/weights/best.onnx',
                f'{model_onnx.path}/accident-detection_{timestamp}.onnx')


@dsl.component(
    base_image=base_image,
    packages_to_install=["boto3"],
)
def upload_to_s3(model_onnx: dsl.Input[dsl.Model]):
    import os
    import boto3
    from botocore.client import Config

    print("configuring s3 instance")
    # Configuration
    minio_url = "http://minio.parasol-insurance.svc.cluster.local:9000"
    access_key = "minio"
    secret_key = "minio123"

    # Setting up the MinIO client
    s3 = boto3.client(
        's3',
        endpoint_url=minio_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version='s3v4'),
    )

    for (dirpath, dirnames, filenames) in os.walk(model_onnx.path):
        for file in filenames:
            print(f"uploading file {dirpath}/{file}")
            s3.upload_file(f"{dirpath}/{file}", "models",
                           f"accident_model/{file}")


@kfp.dsl.pipeline(
    name="Accident Detection",
)
def accident_detection_pipeline(model_obc: str = "accident-detection"):
    download_data_task = download_data(dataset_type="sample")
    train_model_task = train_model(datasets=download_data_task.output)
    upload_to_s3(model_onnx=train_model_task.outputs["model_onnx"])


if __name__ == "__main__":
    print(f"Connecting to kfp: {kubeflow_endpoint}")

    sa_token_path = "/run/secrets/kubernetes.io/serviceaccount/token"  # noqa: S105
    if "BEARER_TOKEN" in os.environ:
        bearer_token = os.environ["BEARER_TOKEN"]
    elif os.path.isfile(sa_token_path):
        with open(sa_token_path) as f:
            bearer_token = f.read().rstrip()

    # Check if the script is running in a k8s pod
    # Get the CA from the service account if it is
    # Skip the CA if it is not
    sa_ca_cert = "/run/secrets/kubernetes.io/serviceaccount/service-ca.crt"
    if os.path.isfile(sa_ca_cert) and "svc" in kubeflow_endpoint:
        ssl_ca_cert = sa_ca_cert
    else:
        ssl_ca_cert = None

    client = kfp.Client(
        host=kubeflow_endpoint,
        existing_token=bearer_token,
        ssl_ca_cert=ssl_ca_cert,
    )
    result = client.create_run_from_pipeline_func(accident_detection_pipeline, arguments={}, experiment_name="accident_detection")
    print(f"Starting pipeline run with run_id: {result.run_id}")
    # Wait 20 minutes for the pipeline to complete
    client.wait_for_run_completion(run_id=result.run_id, timeout=1200)
