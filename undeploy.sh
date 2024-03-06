#!/bin/bash

# Delete the Kubernetes deployments and services
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f redis-deployment.yaml
kubectl delete -f redis-service.yaml
kubectl delete -f huey-deployment.yml

echo "Application and all related services have been successfully deleted!"
