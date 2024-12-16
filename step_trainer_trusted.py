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

# Script generated for node step_trainer_landing
step_trainer_landing_node1734341260287 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_landing", transformation_ctx="step_trainer_landing_node1734341260287")

# Script generated for node accelerometer_trusted
accelerometer_trusted_node1734341296121 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_trused", transformation_ctx="accelerometer_trusted_node1734341296121")

# Script generated for node SQL Query
SqlQuery0 = '''
select sensorReadingTime,serialNumber,distancefromobject

from step_trainer_landing 
join accelerometer_trusted
on accelerometer_trusted.timestamp = step_trainer_landing.sensorReadingTime
'''
SQLQuery_node1734341355821 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"accelerometer_trusted":accelerometer_trusted_node1734341296121, "step_trainer_landing":step_trainer_landing_node1734341260287}, transformation_ctx = "SQLQuery_node1734341355821")

# Script generated for node Amazon S3
AmazonS3_node1734341548977 = glueContext.getSink(path="s3://udacity-stedi/step_trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1734341548977")
AmazonS3_node1734341548977.setCatalogInfo(catalogDatabase="stedi",catalogTableName="step_trainer_trusted")
AmazonS3_node1734341548977.setFormat("json")
AmazonS3_node1734341548977.writeFrame(SQLQuery_node1734341355821)
job.commit()
