# Payoneer

1. we have the script "counter-service.py" thact count each POST to our web service .
   you can check it with the command : curl -X POST <http://3.71.38.22> #This is the public EC2 ip#

I added /healthcheck to the app . so you can run <http://3.71.38.22/healthcheck> - to get status of your app .

2. The Dockerfile build the app .

3. requirenments.txt for the flask install .

4. Deployment perform via github actions .

Future tasks :


For scalability and realibility of the Application it prefered to Deploy the app on K8s .

1. Create helm chart that will contain all the templetes (deployment , service , ingress ...etc)
   
2. Then deploy it on k8s (eks) cluster using helm commands or in gitops method ArgoCD .
   
3. Add monitoring to the service (prometheuse and grafana ) to get the metrics .



