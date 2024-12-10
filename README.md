# STEDI Human Balance Analytics Lakehouse Project

## Introduction
In this project, we build a data lakehouse solution for the STEDI team using their sensor data to train a machine learning model. The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Yet, not all of the early adopters have agreed to share their data for research purposes. Since privacy is a primary consideration for the company, one of the first tasks is to ensure that data from only those customers who agree to share their Step Trainer and accelerometer data is used in the training data for the machine learning model.
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
