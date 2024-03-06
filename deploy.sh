#!/bin/bash

# Apply the Kubernetes configurations
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f huey-deployment.yml
echo "Application has been deployed successfully!"
# Wait for the deployment to be ready
kubectl wait --for=condition=available --timeout=600s deployment/cambai
# Set up port forwarding
echo "Port forwarding has been set up. You can now access the application on localhost:8080/docs"
kubectl port-forward service/cambai 8080:80
