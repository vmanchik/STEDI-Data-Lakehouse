import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
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

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node accelerometer landing
accelerometerlanding_node1734150984436 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="accelerometerlanding_node1734150984436")

# Script generated for node customer trusted
customertrusted_node1734150989551 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_trusted", transformation_ctx="customertrusted_node1734150989551")

# Script generated for node Join
Join_node1734154327557 = Join.apply(frame1=accelerometerlanding_node1734150984436, frame2=customertrusted_node1734150989551, keys1=["user"], keys2=["email"], transformation_ctx="Join_node1734154327557")

# Script generated for node SQL Query
SqlQuery4885 = '''
select timestamp, user, x, y, z
from myDataSource
'''
SQLQuery_node1734154893182 = sparkSqlQuery(glueContext, query = SqlQuery4885, mapping = {"myDataSource":Join_node1734154327557}, transformation_ctx = "SQLQuery_node1734154893182")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1734154893182, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1734153278126", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1734155037798 = glueContext.getSink(path="s3://udacity-stedi/accelerometer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1734155037798")
AmazonS3_node1734155037798.setCatalogInfo(catalogDatabase="stedi",catalogTableName="accelerometer_trusted")
AmazonS3_node1734155037798.setFormat("json")
AmazonS3_node1734155037798.writeFrame(SQLQuery_node1734154893182)
job.commit()