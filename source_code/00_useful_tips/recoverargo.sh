oc delete argocd --all -n openshift-gitops
oc delete pods --all -n openshift-gitops-operator
echo "rerun ./bootstrap.sh "
