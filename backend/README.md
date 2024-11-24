# 4G Capital Challenge - Backend

This repository contains the backend application for the 4G Capital Challenge, which I have containerized and deployed to Kubernetes using ArgoCD.


## Project Overview
The backend application is built using Flask and PostgreSQL. I have containerized the application using Docker and deployed it to Kubernetes using ArgoCD for continuous deployment. The Flask app connects to a PostgreSQL database and exposes RESTful API endpoints for interacting with stored messages.

## Prerequisites
Before setting up this project, ensure you have the following installed:

- Docker (for containerization)
- Kubernetes (for deployment)
- `kubectl` (for interacting with your Kubernetes cluster)
- ArgoCD (for continuous deployment)
- A local or cloud-based PostgreSQL instance, or Kubernetes-based PostgreSQL

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/koechronix/Task-Challenge-.git 
   cd Task-Challenge


# Deployment
I have containerized the backend application and deployed it to Kubernetes using ArgoCD. The deployment configurations are stored in the deployment/ directory.

# ArgoCD Integration
ArgoCD is used to automate the continuous deployment of the application. Once the repository is updated, ArgoCD handles the process of deploying the changes to the Kubernetes cluster.

# Environment Variables
Ensure the following environment variables are set for proper functioning:
DATABASE_URL: Connection string for the PostgreSQL database.

# API Endpoints
The backend exposes the following API endpoints:

GET /messages: Fetch all stored messages from the database.
POST /messages: Add a new message to the database.


