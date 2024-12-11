# STEDI Human Balance Analytics Lakehouse Project

## Introduction
The STEDI team wants to use motion sensor data to train a machine learning model to accurately detect steps in real-time. They require a data lakehouse solution. Not all early adopters have agreed to share their data for research purposes. Thus, the team needs a separate data store for trusted data where the customer data from the website would be sanitized and records of customers who have not agreed to share their data for research purposes be excluded. In addition, the team needs a curated dataset for machine learning, which would combine the step trainer data for customers who have accelerometer data and have agreed to share their data for research with accelerometer records. 


The diagram below demonstrates the lakehouse architecture.

![datalake](./images/lakehouse.png)

## Data
There are three sources of data for this project:
- **Customer data:** Includes consent to release information for research purposes. There are 956 rows in the raw JSON customer data file.
- **Data from step trainer:** A motion sensor that records the distance of the object detected. The step trainer file contains 28,680 rows.
- **Accelerometer data:** Uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions. The accelerometer file has 81,273 rows.

## Tools
The following AWS tools are used in this project:
- AWS IAM
- AWS S3
- Python and Spark
- AWS Glue
- AWS Athena

## Steps
1. Prepare

## Outcome
As a result of the above steps, the original data is transformed into SQL tables in three different zones: 
1. Landing
2. Trusted
3. Curated
