# CBD3354 Activity 1
# **Web Application with Docker and Kubernetes**

## **Project Overview**
This project is a containerized web application featuring a Python Flask backend accessed via an API and a frontend served using NGINX. Both components are deployed in separate containers and connect to an SQL Server database hosted on Google Cloud Platform (GCP). The application is orchestrated using Kubernetes.

## **Features**
- API-based Flask backend for processing and storing user data (username and phone number)
- Frontend served through NGINX for improved performance and security
- SQL Server database connectivity
- Docker containers for each component
- Scalable deployment using Kubernetes
- Secure management of credentials using Kubernetes secrets

## **Project Structure**

```bash
├── backend/                 # Python Flask application
│   └── app.py               # Main Flask application file
│   └── Dockerfile           # Dockerfile for backend
├── frontend/                # NGINX configuration for the frontend
│   └── index.html           # Frontend HTML form
│   └── style.css            # Frontend styling
│   └── Dockerfile           # Dockerfile for frontend
├── kubernetes/              # Kubernetes configuration files
│   ├── deployment.yaml      # Deployments for frontend and backend
│   ├── service.yaml         # Services for frontend and backend
│   └── secrets.yaml         # Secrets for managing sensitive data
├── README.md                # Project documentation
└── docker-compose.yml       # Docker Compose configuration for local development

```
## **Setup Instructions**

### **Prerequisites**
Ensure you have the following installed:
- Docker
- Kubernetes (kubectl)
- Google Cloud SDK
- Git

### **Local Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/frankrodrigo/cbd3354-activity1.git
   cd cbd3354-activity1

2. **Build and run using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    The frontend will be accessible at http://localhost, and the backend API will be running on port 5000.

## **Kubernetes Deployment**

1. **Build and push Docker images to a container registry:**
    ```bash
    docker build -t gcr.io/[project-id]/frontend:latest ./frontend
    docker build -t gcr.io/[project-id]/backend:latest ./backend
    docker push gcr.io/[project-id]/frontend:latest
    docker push gcr.io/[project-id]/backend:latest

2. **Deploy to Google Kubernetes Engine:**
    ```bash
    kubectl apply -f ./kubernetes/deployment.yaml
    kubectl apply -f ./kubernetes/service.yaml
    kubectl apply -f ./kubernetes/secrets.yaml

2. **Access the application via the load balancer IP provided by GKE.**
    ```bash
    kubectl get services
