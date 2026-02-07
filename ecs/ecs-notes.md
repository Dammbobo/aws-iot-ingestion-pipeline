# ECS Extension (Conceptual)

In a production environment, this ingestion pipeline could be extended by
forwarding processed data from AWS Lambda to containerized services running
on Amazon ECS.

## Why ECS
- Suitable for long-running processing workloads
- Easier operational model than managing Kubernetes
- Commonly used for enterprise and industrial applications

## Example use cases
- Aggregating machine data
- Running validation or enrichment jobs
- Forwarding data to dashboards or analytics systems
