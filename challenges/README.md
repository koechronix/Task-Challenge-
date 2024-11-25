## Project Information 
-*Initial Plan:* Deploy the project on Google Cloud Platform (GCP) using Cloud Run and Google Kubernetes Engine (GKE).
*Reason for Change:* Billing limitations in GCP's free-tier offerings.
*Revised Strategy:* Switch to a local Kubernetes environment using Kubernetes IN Docker (KIND).
## Benefits of KIND:
- Enables efficient testing and development.
- Simulates a cloud-like environment locally.
- Provides a lightweight, cost-effective solution.
- Avoids additional costs while maintaining containerized deployment benefits.