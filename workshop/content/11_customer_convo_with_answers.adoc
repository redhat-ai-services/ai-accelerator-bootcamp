## Q&A
Here are some sample answers to each of the customer conversation questions, not all of these answers are consistent and apply concurrently.

---
### Technical
(T01) **Consultant**: Where are we deploying OpenShift AI? Do you have a platform or hardware in mind already?

.**Customer**:
* We have a dedicated on-prem testing lab environment but we prefer our labs use VMs unless that won't work.
* We've got an in-house lab with a few bare-metal servers we had in mind for this, there's also some storage gear, and everything is attached to 10GbE network switches.
* In an AWS cloud environment we can spin up ad-hoc.
* We've got some options but don't really know, what would you recommend?

---
(T02) **Consultant**: Are you planning to use GPU accelerators?

.**Customer**:
* Yes, we have Nvidia A100s in several of the lab hosts we'd like to use for deployment.
* It's possible, we haven't installed GPUs in our lab gear but might be able to find a couple for testing if you think it'll make a difference.
* Our data science team says they are essential for doing training on their deep learning models, but we don't have any in our lab due to cost. Will that be a problem?

---
(T03) **Consultant**: What do you plan to use for storage? (Enterprise Array? Ceph/ODF? S3?)

.**Customer**:
* We plan to use our existing enterprise-grade storage arrays, we've got a NetApp and a Pure FlashArray in the lab. We don't have an object storage solution at the moment, but I think we can do that on the NetApp.
* We've got Ceph in production, do we need a separate Ceph deployment for this?
* We can use the cloud platform native storage resources.

---
(T04) **Consultant**: Will we be deploying/using ODF (converged or external)?

.**Customer**:
* We are considering deploying OpenShift Data Foundation (ODF) in a converged configuration. We do have several unused SSDs in each of the lab servers.
* If we can use ODF with our lab Ceph cluster, that'd be ideal

---
(T05) **Consultant**: Does the deployment environment have direct or proxied internet access, or is it a disconnected environment?

.**Customer**:
* The deployment environment has direct internet access.
* We don't have direct access, but can use a web proxy if needed or use Artifactory for proxy repositories
* This lab has no internet access and is fully disconnected, but we can use a bastion host to gather resources and attach it to the lab for deployment.

---
(T06) **Consultant**: Do you have experience with OpenShift?

.**Customer**:
* Yes, we have substantial experience with OpenShift in our environment, our team is well-versed in managing and deploying OpenShift clusters.
* We have a few OpenShift deployments, but we primarily use Kubernetes from other vendors (Azure AKS, Rancher)
* We don't use OpenShift today, we've been looking at containers but haven't deployed any in our environment yet.

---
(T07) **Consultant**: Do you have an internal git repository?

.**Customer**:
* Yes, we maintain an internal git repository for version control and collaboration, it’s integrated into our CI/CD pipelines.
* We have an internal git repo, but it won't be accessible to the lab
* We use GitHub enterprise, but I'm not sure we can setup accounts for this
* No, we don't use git formally in our IT today

---
(T08) **Consultant**: What do you use for DNS, SSO, NTP?

.**Customer**:
* For DNS, we use our internal DNS servers.
* We have an enterprise DNS solution from Infoblox.
* We use Azure DNS is tied to our Azure AD deployment

* Single Sign-On (SSO) is handled via our enterprise SSO solution.
* We use Red Hat Single Sign-On with SAML and OIDC.

* Network Time Protocol (NTP) is synchronized with our internal NTP servers.
* We have PTP in use across our environment as our workloads are very time sensitive

---
(T09) **Consultant**: Do you have CI/CD/DevOps processes in use in the environment today?

.**Customer**:
* Yes, we have established CI/CD pipelines to streamline our development and deployment processes.
* Our DevOps practices are well-integrated into our workflow to ensure continuous integration and delivery.

---
### Delivery
(D01) **Consultant**: Is the environment ready for deployment?

.**Customer**:
* Yes, our environment is prepared for the deployment.
* We have ensured that all necessary infrastructure and resources are in place.

---
(D02) **Consultant**: How will the consultant gain access to the environment? (VPN, VDI, SSH, etc.)

.**Customer**:
* The consultant will gain access via secure VPN. We will provide the necessary credentials and setup instructions.
* We'll get you onboarded and ship you a secure laptop you can use to get into our environment
* We aren't comfortable setting up remote access for your team, so we'd like to work with you via video conference/chat 'over-the-shoulder'

---
(D03) **Consultant**: Who is the primary point-of-contact on the team we will be working with?

.**Customer**:
* (Senior Engineer) will be your primary point-of-contact. They are well-versed in our infrastructure and can assist with any questions.

---
(D04) **Consultant**: Who are the internal teams involved in this deployment? (Containers, Network, Storage, Infrastructure, Security, ...?)

.**Customer**:
* The deployment will involve the Containers, Network, Storage, Infrastructure, and Security teams. Each team has designated members ready to assist as needed.

---
(D05) **Consultant**: Are there any processes around change control or activity planning we need to be aware of?

.**Customer**:
* Yes, we have a formal change control process in place. All planned activities interacting with production need to be documented and approved by our change control board. Any work inside the lab shouldn't need any change control, but we'd like to be kept in the loop for major changes or deployment activities.
* If you have any needs for network changes, you can coordinate with our network team, and they'll action them as resources permit.

---
(D06) **Consultant**: What time zone is the team based in? Is there flexibility in working hours?

.**Customer**:
* The container team is primarily based in the Eastern Time Zone (EST), but several of the internal teams we work with are in different parts of the US and Canada (mostly in PST and MST)
* There is some flexibility in working hours to accommodate collaboration with external teams.

---
(D07) **Consultant**: Are there any upcoming change freezes, holidays, training, or other disruptions to the delivery schedule?

.**Customer**:
* There is an upcoming change freeze at the end of the fiscal quarter -- it lasts from the week before the quarter end until 2 weeks after, so we need to be mindful of any changes we need outside of the lab and make sure we've prepped ahead of time.
* Additionally, we have some scheduled holidays and training sessions in the next few weeks, but we'll send those over to your project manager.

---
### Business
(B01) **Consultant**: Do you have specific challenges you're aiming to address with machine learning?

.**Customer**:
* Yes, we aim to improve our predictive maintenance processes and customer sentiment analysis.
* We're also looking to enhance our fraud detection capabilities.

---
(B02) **Consultant**: Do you have any AI models or data science projects in use today?

.**Customer**:
* We have a few AI models in production, including customer churn prediction and inventory optimization.
* Our data science team is actively working on new projects related to market analysis.

---
(B03) **Consultant**: How do you deploy/serve models today?

.**Customer**:
* Currently, we use a combination of custom scripts and containerized applications to deploy our models.
* We also leverage some cloud services for model serving but are looking to consolidate this process.
* This is all handled with the cloud-native AI tooling provided by our cloud provider.

---
(B04) **Consultant**: What tools/applications are being used for data science in your organization today?

.**Customer**:
* Our data scientists primarily use JupyterLab, RStudio, and various Python libraries.
* For collaboration and version control, we use Git and GitHub.

---
(B05) **Consultant**: Are there specific frameworks like TensorFlow or PyTorch you plan to utilize or know your data scientists are already using?

.**Customer**:
* Yes, our team frequently uses TensorFlow and PyTorch for model development.
* We also use Scikit-learn for more traditional machine learning tasks.

---
(B06) **Consultant**: What are your business/technical goals for deploying OpenShift AI?

.**Customer**:
* We aim to streamline our AI/ML workflows and improve model deployment efficiency.
* Technically, we want to ensure scalability and robustness in our AI infrastructure.

---
(B07) **Consultant**: Do you have any specific success criteria for this engagement?

.**Customer**:
* Success would mean reducing model deployment time and improving collaboration among our data scientists.
* We also aim to achieve seamless integration with our existing infrastructure.

---
(B08) **Consultant**: What are the key metrics you'll use to gauge the effectiveness of this engagement?

.**Customer**:
* Key metrics include model performance, deployment time, and user adoption rates.
* We will also measure the reduction in operational overhead and improvements in collaboration efficiency.

---
(B09) **Consultant**: Are there other vendors you're working with to build your AI/ML platforms? **Customer**:

* Yes, we have partnerships with several cloud service providers and hardware vendors.
* We also work with a few specialized AI software vendors for specific needs.

---
(B10) **Consultant**: What is the timeframe you are working with to get this deployed?

.**Customer**:
* We aim to complete the deployment within the next three to six months.
* This timeline is flexible but aligned with our strategic planning cycles.

---
(B11) **Consultant**: What kinds of internal datasets do you expect to use/connect with your AI/ML projects?

.**Customer**:
* We will use a variety of datasets, including transactional data, customer feedback, and operational logs.
* Our projects will also integrate with external data sources for enhanced analytics.

---
(B12) **Consultant**: Do you have projections on the number of users/growth rate for this environment?

.**Customer**:
* Initially, we expect around 20-30 active users, primarily data scientists and analysts.
* We anticipate a growth rate of about 20% per year as more departments adopt AI/ML solutions.

---
(B13) **Consultant**: What is the scale of the environment we're going to build?

.**Customer**:
* We plan to start with a moderate scale, supporting multiple teams and a variety of projects.
* Scalability is key, so the infrastructure needs to handle increasing workloads efficiently.

---
(B14) **Consultant**: How will most of the target audience access this environment?

.**Customer**:
* Users will primarily access the environment through secure VPN connections.
* We will provide web-based interfaces and APIs for ease of use and integration.
