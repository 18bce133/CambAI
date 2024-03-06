# Documentation for Key-Value Store Application

## Overview
This application is a key-value store developed using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue. It is designed to scale reliably across multiple pods/deployments.

## Application Structure

### main.py
This is the main application file where the FastAPI application is defined. It includes the following endpoints:

- `POST /items/{item_id}`: This endpoint accepts an item ID and a value, and writes them to the Redis store. The write operation is performed asynchronously using a Huey task.
- `GET /items/{item_id}`: This endpoint accepts an item ID and returns the corresponding value from the Redis store.

### Dockerfile
The Dockerfile is used to build a Docker image for the application. It starts from a Python 3.10 base image, sets the working directory to `/app`, copies the requirements file and installs the Python dependencies. Then it copies the rest of the application code and sets the default command to start the FastAPI server.

After building, the Docker image is pushed to Docker Hub to be accessible by Kubernetes.

### deployment.yaml
This file defines a Kubernetes Deployment for the main application. The deployment creates a pod with a single container running the application image (`nihar0804/my-app:latest`). The application listens on port 80.

### service.yaml
This file defines a Kubernetes Service for the main application. The service exposes the application on port 80.

### redis-deployment.yaml
This file defines a Kubernetes Deployment for the Redis server. The deployment creates a pod with a single container running the Redis image (`redis:latest`). The Redis server listens on port 6379.

### redis-service.yaml
This file defines a Kubernetes Service for the Redis server. The service exposes the Redis server on port 6379.

### huey-worker deployment
This is a Kubernetes Deployment for the Huey worker. The worker is responsible for executing tasks queued by the main application. The worker runs in a separate pod and uses the same application image as the main application.

## Approach
The application is designed to be scalable and reliable. It uses Kubernetes to manage the deployment, scaling, and networking of the application components. The FastAPI framework is used to define the API endpoints, and Huey is used for task scheduling. Redis is used as the database to store the key-value pairs.

The application is designed to be stateless, meaning that it does not store any data locally. All data is stored in the Redis database, which allows the application to be scaled horizontally by adding more pods/deployments.

The application is also designed to be fault-tolerant. If a pod or deployment fails, Kubernetes will automatically restart it. The Huey worker is responsible for executing tasks queued by the main application, and it can be scaled independently of the main application to handle a large number of tasks.

## Design Decisions
- **Microservices Architecture:** The application follows a microservices architecture pattern, with separate deployments for the main application, Redis server, and Huey worker. This allows each component to scale independently based on demand.
- **Asynchronous Task Execution:** Write operations to the Redis store are performed asynchronously using Huey tasks. This ensures that the API remains responsive even under heavy load.
- **Use of Kubernetes:** Kubernetes is used to manage the deployment, scaling, and networking of the application components. This allows the application to be easily deployed and scaled across multiple pods/deployments.

## Challenges
- **Integration Testing:** In a real-world scenario, integration tests would be required to test the application in a Kubernetes environment. This would involve setting up a test Kubernetes cluster and running tests against it.
- **Security:** The application does not currently implement any security measures such as authentication or authorization. In a production environment, these would need to be added to secure the application.
- **Monitoring and Logging:** The application does not currently include any monitoring or logging solutions. In a production environment, these would need to be added to monitor the health of the application and diagnose issues.
- **Data Persistence:** The application currently uses an in-memory Redis database. In a production environment, a more robust and scalable data storage solution would be required.
- **Error Handling:** The application does not currently implement comprehensive error handling. In a production environment, error handling would need to be improved to provide a better user experience and to help diagnose issues.

## Running the Application
To run the application, you need to have a Kubernetes cluster set up. You can then apply the Kubernetes configuration files using `kubectl apply -f <filename>`. This needs to be done for each of the configuration files.

But for the sake of simplicity, you can use the following command to deploy the application:

### Deploy the application
 This script is used to deploy the application. It applies the Kubernetes configurations, waits for the deployment to be ready, and sets up port forwarding so you can access the application on your local machine. You can run this script using the following command:
```bash
./deploy.sh
```

### Undeploying the Application
This script is used to undeploy the application. It deletes the Kubernetes deployments and services related to the application. You can run this script using the following command:
```bash
./undeploy.sh
```

Please note that the application image (`nihar0804/my-app:latest`) needs to be available in a Docker registry that is accessible from the Kubernetes cluster.

## Scaling the Application
The application can be scaled by increasing the number of replicas in the Kubernetes Deployment configurations. This can be done by modifying the `replicas` field in the `deployment.yaml` and `huey-deployment.yml` deployment.

## Testing the Application
Test cases are written in `test.py` file. You can run the test cases using the following command:
```bash
pytest test.py
```
Some of the test cases are:
- Test if data is written to the Redis store
- Test if data is read from the Redis store
- Test if the application returns a 404 error when trying to read a non-existent key
- Test of data is not written to the Redis store when the value is not provided
- Test if data is not written to the Redis store when the value is empty

More test cases can be added to cover more scenarios. In a real-world scenario, we can also write integration tests to test the application in a Kubernetes environment.  

## Conclusion
This application demonstrates a scalable, robust system with a keen eye on documentation, process, code style, minimalism, and clarity. It leverages the power of Kubernetes, FastAPI, and Huey to provide a reliable key-value store.
