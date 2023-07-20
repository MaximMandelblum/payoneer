# elementor-test

Created Workflow that contains few things :

1. Run action every push to main 
2. Job that doing deploy on ubuntu-latest version.
3. we have few steps to accomplish this task :

* Set up Minikube - start minikube.
* Checkout code - check out the repo code.
* Run Minikube docker env - enter runtime minikube env.
* Build Docker image - build docker image from Dockerfile.
* Check image created - check if the image created and located in minikube local registry.
* Deploy application using Helm chart - Deploy the application helm cahrt on minikube k8s cluster.
* Check pod status  - check pod status after deployment to verify they running without any problem.
* Port forward to check the app - port forward the app service to be able connect it.
* Add hosts to /etc/hosts - add the ingress host we will connect in browser inside /etc/hosts.
* Run Rick and Morty test - run the get check on our deployed app to get the result.
* Run healthcheck test - perform healthcheck test to verify we good.
