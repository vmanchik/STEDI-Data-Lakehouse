import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node accelerometer_trusted
accelerometer_trusted_node1734345843797 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_trusted", transformation_ctx="accelerometer_trusted_node1734345843797")

# Script generated for node step_trainer_trusted
step_trainer_trusted_node1734345841034 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_trusted", transformation_ctx="step_trainer_trusted_node1734345841034")

# Script generated for node SQL Query
SqlQuery0 = '''
select distinct *
from step_trainer_trusted 
join accelerometer_trusted 
on accelerometer_trusted.timestamp = step_trainer_trusted.sensorreadingtime
'''
SQLQuery_node1734345936733 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"step_trainer_trusted":step_trainer_trusted_node1734345841034, "accelerometer_trusted":accelerometer_trusted_node1734345843797}, transformation_ctx = "SQLQuery_node1734345936733")

# Script generated for node Amazon S3
AmazonS3_node1734348531941 = glueContext.getSink(path="s3://udacity-stedi/machine_learning/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1734348531941")
AmazonS3_node1734348531941.setCatalogInfo(catalogDatabase="stedi",catalogTableName="machine_learning_curated")
AmazonS3_node1734348531941.setFormat("glueparquet", compression="snappy")
AmazonS3_node1734348531941.writeFrame(SQLQuery_node1734345936733)
job.commit()
