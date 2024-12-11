# STEDI Human Balance Analytics Lakehouse Project

## Introduction
The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time and is in need of a data lakehouse solution. Not all of the early adopters have agreed to share their data for research purposes. Thus, the team needs a separate data store for trusted data where the customer data from the website would be sanitized and records of customers who have not agreed to share their data for research purposes be excluded. In addition, the team needs a curated dataset for machine learning, which would combine the step trainer data for customers who have accelerometer data and have agreed to share their data for research with accelerometer records. 

The diagram below demonstrates the lakehouse achetecture.

![datalake](./images/lakehouse.png)

## Data
There are three sources of data for this project
- *Customer data*, which includes consent to release information for research purposes. There are 956 rows in the raw JSON customers data file.
- *Data from step trainer* - a motion sensor that records the distance of the object detected. The step trainer file contains 28,680 rows.
- *Accelerometer data* from the app which uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions. The accelerometer file has 81,273 rows.
## Tools
The following AWS tools are used in this project:
- AWS IAM
- AWS S3
- Python and Spark
- AWS Glue
- AWS Athena

## Steps
1) Prepair
## Outcome
As the result of the above steps, the original data is stransforemed into sql tables in three different zones - 1) landing, 2) trusted, 3) curated. 
