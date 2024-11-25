## Part 1: CI/CD and Version Control
## **Question 1: Setting Up a CI/CD Pipeline with Cloud Build and Cloud Deploy**
- To establish a CI/CD pipeline for deploying a containerized API service on Google Cloud Platform (GCP) using Cloud Build and Cloud Deploy, follow these steps:

# *CI Pipeline:*

1.*Code Storage:* Store application and infrastructure code in Bitbucket.
2.*Automation via Triggers:* Configure Cloud Build triggers to start automatically when changes are pushed to  specific branches (e.g., main or release).
3.*Define Pipeline Steps in *cloudbuild.yaml*:*
    - Build the containerized Java application using Docker.
    - Run automated unit and integration tests.
    - Push the container image to Google Container Registry (GCR).

Example cloudbuild.yaml:
```bash
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/api-service:$COMMIT_SHA', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/api-service:$COMMIT_SHA']
images:
  - 'gcr.io/$PROJECT_ID/api-service:$COMMIT_SHA'

```

# *CD Pipeline:*
1.*Automated Deployments:* Use Cloud Deploy to automate deployments to staging and production environments.
2.*Delivery Pipeline:*
    - Reference Kubernetes manifests stored in the repository.
    - Define separate stages for staging and production with automated rollouts.
3.*Approval Gates:*
    - Automate staging deployment and include manual approvals for production.

Example delivery pipeline:  

```bash
apiVersion: deploy.cloud.google.com/v1
kind: DeliveryPipeline
metadata:
  name: api-service-pipeline
spec:
  stages:
    - targetId: staging
      profiles: [staging]
    - targetId: production
      profiles: [production]

```    

# *Automation in Deployment:*
    - Integrate with Google Kubernetes Engine (GKE) for deployment.
    - Use Cloud Monitoring to trigger automated rollback if health checks fail.
    - Implement Slack or email notifications for deployment success/failure updates.
NB:This fully automated pipeline ensures smooth deployments with minimal manual intervention, reducing errors and increasing reliability.

## **Question 2: Managing Version Control for Code and Infrastructure**
- Version control for application and infrastructure code can be handled using separate repositories for clarity and organization:

1.**Application Repository:**
- Contains the API service code and its configurations. Example structure:

```bash
    /app            # Java API code
    /Dockerfile     # Docker build file
    /cloudbuild.yaml  # CI/CD pipeline configuration
 ``` 

2.**Infrastructure Repository:**
- Manages Infrastructure as Code (IaC), such as Terraform configurations for GKE clusters, VPC, and networking. Example structure:
```bash
    /terraform
    /gke-cluster.tf   # GKE cluster configurations
    /cloud-run.tf     # Cloud Run setup
```   
3.**Branching Strategy:** 
Use a feature-branch workflow for isolated development. Key branches:

- main: Production-ready code.
- dev: For testing and development.
- feature/*: For new features or bug fixes.
4.**Bitbucket Pipelines:**
Automate the CI process to test and push code changes, trigger Cloud Build, and integrate with Cloud Deploy for seamless deployment.

## Question 3: Containerizing the API Service with Docker
Steps to containerize the Java-based API service:

1.*Create a Dockerfile:*
Use a multi-stage build for smaller, efficient images. Example:
```bash
Dockerfile
Copy code
FROM maven:3.8-openjdk-11-slim AS build
WORKDIR /app
COPY . .
RUN mvn clean install

FROM openjdk:11-jre-slim
COPY --from=build /app/target/api-service.jar /app/api-service.jar
CMD ["java", "-jar", "/app/api-service.jar"]
``` 

2.*Optimizations:*

    - Use a lightweight base image (openjdk:11-jre-slim).
C   - ache Maven dependencies to speed up builds.
3.*Considerations:*

    - Set resource limits in Kubernetes to prevent resource exhaustion.
    - Use health checks in the container to ensure the service is running properly.


## Question 4: API Management with ApigeeX
# *Features to Leverage:*

1.*Rate Limiting:* Protect the API from abuse.
2.*Authentication:* Use OAuth 2.0 policies for secure user authentication.
3.*Traffic Management:* Route traffic between environments (e.g., canary releases).
4.*Monitoring:* Enable API analytics to track usage and errors.
# Benefits:

- Simplified authentication and authorization.
- Improved security and compliance.
- Enhanced API observability.

## Question 5: Key Metrics and Monitoring Setup
To monitor the API service:

1.*Metrics:*

- Latency: Response time for API requests.
- Error Rates: Percentage of failed requests (e.g., HTTP 5xx).
- Throughput: Number of requests per second.
- Resource Usage: CPU and memory consumption of the container.
2.*Logs:*

- API request and response logs.
- Application logs (e.g., exceptions and stack traces).

3.*Setup:*

- Use Cloud Monitoring for metrics and alerts.
- Use Cloud Logging to aggregate and query logs.

## Question 6: Incident Troubleshooting Process
1. *Detection*
Example: An alert in Cloud Monitoring shows that the API error rate (HTTP 5xx) has spiked in the last 10 minutes.
2. *Diagnosis*
- Step 1: Check Logs:

Look at logs in Cloud Logging and find repeated errors, e.g., "Database connection timeout."
- Step 2: Check Metrics:

Observe metrics like CPU and memory usage. In this case, memory usage is very high, indicating a possible resource issue.
3. *Resolution*
- Step 1: Restart the API service to restore functionality temporarily:

```bash
kubectl rollout restart deployment api-service
```
- Step 2: Investigate further and find the issue is caused by an unclosed database connection. Fix the bug in the code, test it locally, and redeploy using the CI/CD pipeline.

4. *Post-Incident Review*
Lesson Learned: Add monitoring for database connections to catch similar issues earlier.

## Part 4: Infrastructure as Code and Scalability
## Question 7: Using IaC for Infrastructure Management
- I would use *Terraform* to define infrastructure and store the code in *Bitbucket* for version control. I organize reusable modules for components like *GKE clusters, VPCs, and IAM roles*.

- For automation, I leverage Terraform Cloud or Jenkins to run *terraform plan and terraform apply*.

- This approach ensures consistency, tracks changes, and simplifies scaling for efficient infrastructure management.

# Question 8: Describe your approach to ensuring the infrastructure is resilient and scalable. How would you architect the solution to handle varying loads and potential failures?

1.*Resilience:*
- I would deploy across multiple GCP zones to prevent regional failures.
- I would enable auto-healing in GKE to restart failed pods automatically.

2.*Scalability:*
- Use horizontal pod autoscaling in GKE to adjust resources based on demand.
- Implement a Cloud Load Balancer to distribute traffic efficiently.
3.*Architecture:*
- Could follow a microservices-based design for flexibility and fault isolation.
- Could set up a CI/CD pipeline to deploy updates seamlessly without downtime.
