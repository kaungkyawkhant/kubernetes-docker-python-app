# kubernetes-docker-python-app
View the the running pod in kubernetes cluster 

```
kubectl get pod
```

Using the deployment.yml file create new pod using docker container from docker hub.
```
kubectl apply -f deployment.yml
```

Check the running pod by watch command
```
kubectl get pod -w
```

Using the services.yml file create new service to expose the port 5000 to public.
```
kubectl apply -f services.yml
```

Testing web app status in terminal 
Using the deployment.yml file create new pod using docker container from docker hub.
```
curl http://[ip address]:5000
```

Hope you enjoy trying out kubernetes and docker in linode.com with free trial.

