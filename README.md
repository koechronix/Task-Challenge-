## Project Overview
The Task Challenge involves developing both a backend and frontend application, along with the necessary infrastructure to facilitate deployment and management. The backend is built using Flask and integrates with a PostgreSQL database, while the frontend provides a user-friendly interface to interact with the backend.


The repository is structured into separate directories for each project component, simplifying the management and deployment process.

## Prerequisites
Ensure the following tools and software are installed before setting up the project:

**Docker** (for containerizing applications)
**Kubernetes** (for application deployment)
**kubectl** (for managing Kubernetes clusters)
**ArgoCD** (for automating deployments)
A **PostgreSQL** database instance (or a Kubernetes-based setup)
**KIND** (for creating local Kubernetes clusters)

## Folder Structure
```bash 
task/
├── backend/                                  # Backend application
│   ├── deployment/                           # Deployment configurations for backend
│   │   ├── flask-service.yaml                # Kubernetes service for Flask application
│   │   └── postgres-service.yaml             # Kubernetes service for PostgreSQL
│   ├── images/                               # Screenshots or images related to the backend
│   │   ├── Screenshot from 2024-11-24 15-36-50.png
│   │   ├── Screenshot from 2024-11-24 15-38-23.png
│   │   └── Screenshot from 2024-11-24 19-08-02.png
│   ├── Dockerfile                            # Dockerfile for containerizing the backend
│   ├── main.py                               # Main Python application file
│   ├── README.md                             # Documentation for backend setup
│   └── requirements.txt                      # Python dependencies for the backend
├── frontend/                                 # Frontend application
│   ├── build/                                # Compiled or built files for deployment
│   ├── images/                               # Screenshots or images related to the frontend
│   │   ├── Screenshot from 2024-11-24 14-21-09.png
│   │   ├── Screenshot from 2024-11-24 14-40-02.png
│   │   ├── Screenshot from 2024-11-24 14-46-21.png
│   │   └── Screenshot from 2024-11-24 14-47-22.png
│   ├── node_modules/                         # Node.js dependencies (auto-generated)
│   ├── public/                               # Static assets for the frontend
│   ├── src/                                  # Source code for the frontend
│   ├── .gitignore                            # Git ignore file for frontend
│   ├── Dockerfile                            # Dockerfile for containerizing the frontend
│   ├── package-lock.json                     # Dependency lock file for Node.js
│   ├── package.json                          # Node.js project metadata and dependencies
│   └── README.md                             # Documentation for frontend setup
├── infra/                                    # Infrastructure setup and configuration
│   ├── dev.yaml                              # Development environment Kubernetes configuration
│   ├── main.tf                               # Terraform configuration file
│   ├── README.md                             # Documentation for infrastructure setup
│   └── service.yaml                          # Kubernetes service configuration
├── Instructions.md                           # General project instructions or guidelines
└── README.md                                 # Main project documentation
```
## Deployment
The deployment setup for this project is organized within specific directories for each component, including the backend, frontend, and infrastructure. The project accommodates both local and cloud-based deployment methods, with configurations designed to maintain uniformity across both environments.

## Local Deployment Using KIND
1.**Build Application Containers:** Package both the backend and frontend applications into Docker containers. KIND is then used to emulate a Kubernetes cluster on your local machine for deployment.

2.**Set Up a Local Kubernetes Cluster:** Utilize KIND to spin up a local Kubernetes cluster. This environment is designed to closely replicate the setup of GCP Kubernetes, ensuring the deployment process remains consistent across environments.

3.**Deploy the Applications:** Leverage Kubernetes manifests configured for KIND to deploy both the backend and frontend applications into the local cluster.

4.**Automate Deployments with ArgoCD:** ArgoCD is configured to streamline the deployment process by continuously monitoring the repository for changes. Any updates pushed to the repository are automatically deployed to the local Kubernetes cluster or GCP Kubernetes Engine.

## GCP Deployment (Original Approach)
1.**Infrastructure Setup with Terraform:** Infrastructure components, including Google Cloud SQL, Cloud Run, and Google Kubernetes Engine (GKE), were initially set up using Terraform to automate resource provisioning on Google Cloud Platform.

2.**Pushing Docker Images to GCP:** Docker images for the backend and frontend were uploaded to Google Container Registry (GCR). These images were then deployed to Cloud Run for serverless operations or GKE for managed Kubernetes environments.

3.**Serverless Deployment via Cloud Run:** The backend service was planned to operate on Google Cloud Run for its serverless capabilities. However, due to restrictions in the free-tier account, the deployment strategy shifted to a local Kubernetes setup.

4.**Continuous Deployment with ArgoCD:** To streamline updates and deployments, ArgoCD was configured to manage automatic application deployments to GKE within the cloud environment.


## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
