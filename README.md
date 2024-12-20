# STEDI Human Balance Analytics Lakehouse Project

## Introduction
The STEDI team wants to use motion sensor data to train a machine learning model to accurately detect steps in real-time. They require a data lakehouse solution. Not all early adopters have agreed to share their data, so the team needs a scalable and flexible architecture to handle varying data sources and volumes. The team wants both the source and destination files reside on an S3 bucket with different subderectories for raw data files, trusted data files, and final curated data files.

The diagram below demonstrates the lakehouse architecture.

![datalake](./images/lakehouse.png)

## Data Files
There are three JSON files:
- **Customer data:** Includes consent to release information for research purposes. There are 956 rows in the raw JSON customer data file.
- **Data from step trainer:** A motion sensor that records the distance of the object detected. The step trainer file contains 28,680 rows.
- **Accelerometer data:** Uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions. The accelerometer file has 81,273 rows.

## Requirements
The original data is transformed into SQL tables in three different zones: 
1. Landing Zone
   - Glue tables **customer_landing**, **accelerometer_landing**, and **step_trainer_landing**
   - Include SQL scripts for the three tables
3. Trusted Zone
   - Glue tables for **customer_trusted** and **accelerometer_trusted**
   - Verification of records in the customer_trusted glue table
5. Curated
   - Glue table **customers_curated** with matched records of customers who have accelerometer data and have agreed to share their data for research
   - Glue table **machine_learning_curated** that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data

## Project Steps
AWS Glue Configuration
   - Create an S3 Bucket and load raw data into the landing subdirectory.
      - Use CloudShell and enter the following command: aws s3 mb s3://your-bucket-name
   - Create an S3 Gateway Endpoint to allow S3 traffic from your Glue Jobs into your S3 buckets
     - Describe vpcs: aws ec2 describe-vpcs
     - Describe routing table: aws ec2 describe-route-tables
     - Create an S3 gateway endpoint: aws ec2 create-vpc-endpoint --vpc-id _______ --service-name com.amazonaws.us-west-2.s3 --route-table-ids _______
   - Create the Glue Service Role in IAM and grant access to the S3 bucket and attach general Glue policy

## Data in Each Zone
### Landing Zone
#### **1. Customer Records (from the website)**

Contains the following fields:

- serialnumber
- sharewithpublicasofdate
- birthday
- registrationdate
- sharewithresearchasofdate
- customername
- email
- lastupdatedate
- phone
- sharewithfriendsasofdate

#### **2. Step Trainer Records (data from the motion sensor):**

Contains the following fields:

- sensorReadingTime
- serialNumber
- distanceFromObject

#### **3. Accelerometer Records (from the mobile app):**

Contains the following fields:

- timeStamp
- user
- x
- y
- z
  
#### **4. Glue table customer_landing:**
![customer_landing](./images/glue_table_customer_landing.png)

#### **5. Glue table accelerometer_landing:**
![accelerometer_landing](./images/glue_table_accelerometer_landing.png)

#### **6. Glue table step_trainer_landing:**
![step_trainer_landing](./images/glue_table_step_trainer_landing.png)


### Trusted Zone


#### **1. Glue table customer_trusted:**
![customer_trusted](./images/glue_table_customer_trusted.png)
#### **2. Glue table accelerometer_trusted:**
![customer_trusted](./images/glue_table_accelerometer_trusted.png)
#### **3. Glue table step_trainer_trusted:**
![step_trainer_trusted](./images/glue_table_step_trainer_trusted.png)

### Curated Zone
#### **1. Glue table customer_curated:**
![customer_curated](./images/glue_table_customer_curated.png)
#### **2. Glue table machine_learning_curated:**
![machine_learning_curated](./images/glue_table_machine_learning.png)

### Counts by Zone
The image below serves to validate record counts for each of the tables.
![counts by zone](./images/counts_by_zone.png)

