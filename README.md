# AWS IoT Ingestion Pipeline

This repository demonstrates a simplified AWS-based ingestion pipeline
for shop-floor or IoT data.

## Why this project
In industrial environments, data from machines, PLCs, or edge devices
is often uploaded to the cloud for processing, monitoring, or analytics.
This project illustrates a common pattern used to ingest that data
reliably into AWS.

## Architecture overview
- Shop-floor systems upload files or data to Amazon S3
- An S3 event triggers an AWS Lambda function
- Lambda processes the data and logs results

## AWS services used
- Amazon S3 – durable data ingestion layer
- AWS Lambda – event-driven data processing
- AWS CloudWatch – logging and monitoring

## How this would be used
In a real production system, this pipeline could be extended to:
- Process machine logs
- Trigger alerts on abnormal data
- Forward data to containerized services running on ECS

## Notes
This project focuses on architecture and data flow.
It is intentionally simplified for learning and demonstration purposes.
