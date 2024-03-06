# CAMB.AI Assignment 

This is a FastAPI application that uses Redis as a database and Huey for task scheduling.

## Application Structure

The application consists of the following main components:

- `main.py`: This is the main FastAPI application file. It defines the API endpoints and the tasks that are scheduled using Huey.

- `deployment.yaml`: This file contains the Kubernetes Deployment configuration for the main application.

- `service.yaml`: This file contains the Kubernetes Service configuration for the main application.

- `redis-deployment.yaml`: This file contains the Kubernetes Deployment configuration for the Redis database.

- `redis-service.yaml`: This file contains the Kubernetes Service configuration for the Redis database.

- `huey-worker.yaml`: This file contains the Kubernetes Deployment configuration for the Huey worker.

## API Endpoints

The application defines the following API endpoints:

- `POST /items/{item_id}`: This endpoint accepts an item ID and a value, writes them to the Redis database, and returns the item ID and value.

- `GET /items/{item_id}`: This endpoint accepts an item ID and returns the corresponding value from the Redis database.

## Testing the Application
Test cases are written in `test.py` file. You can run the test cases using the following command:
```bash
pytest test.py
```
More information about the test cases can be found in the Documentation.md file.

## Running the Application

To run the application, you need to have Docker and Kubernetes installed. You can then use the following command to deploy the application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f huey-worker.yaml
```
Alternatively, you can use the provided `deploy.sh` script to deploy the application and the `undeploy.sh` script to undeploy the application. These scripts will apply the Kubernetes configurations and set up port forwarding so you can access the application on your local machine. The commands to run these scripts are as follows:

```bash
./deploy.sh
./undeploy.sh
```
