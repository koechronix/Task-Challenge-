# Project Overview
Welcome to the TODO Project! This project focuses on building and deploying a backend and frontend application. It uses modern tools like Kubernetes,Docker, CI/CD pipelines, and emphasizes simplicity and efficiency for seamless local or cloud deployment.

# Applications
   # Backend Application
Framework: Developed with Flask, providing a lightweight API.
Key Features:
Health check endpoint (/) to verify the service is alive.
Integration with a PostgreSQL database for storing messages.

  # Fronend Application
Designed to interact with the backend API and offer a user-friendly interface.

# Infrastructure Setup

Provisioned a PostgreSQL instance using Terraform to manage backend data.

# Cloud Deploy:
Created deployment targets for both the frontend and backend to streamline CI/CD processes.

# Deployment Strategy
   # Terraform:
Utilized Terraform to provision infrastructure as code.

   # Docker:
Containerized both applications for deployment on Google Cloud Run.

   # CI/CD Pipeline:
Set up a CI/CD pipeline using Google Cloud Deploy to automate the deployment process, ensuring continuous integration and delivery.

# Configuration Management
Developed YAML configurations for defining services and job specifications in Cloud Run.



