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

# Script generated for node customer_trusted
customer_trusted_node1734329676604 = glueContext.create_dynamic_frame.from_catalog(
  database="stedi", 
  table_name="customer_trusted", 
  transformation_ctx="customer_trusted_node1734329676604"
)

# Script generated for node accelerometer_landing
accelerometer_landing_node1734329679152 = glueContext.create_dynamic_frame.from_catalog(
  database="stedi", 
  table_name="accelerometer_landing", 
  transformation_ctx="accelerometer_landing_node1734329679152"
)

# Script generated for node SQL Query to merge records
SqlQuery0 = '''
select distinct customername,
email,
phone, 
birthday,
serialnumber,
registrationdate,l
astupdatedate,
sharewithresearchasofdate,
sharewithpublicasofdate,
sharewithfriendsasofdate

from customer_trusted  
join accelerometer_landing on accelerometer_landing.user = customer_trusted.email
'''
SQLQuerytomergerecords_node1734329847277 = sparkSqlQuery(
  glueContext, query = SqlQuery0, 
  mapping = {"customer_trusted":customer_trusted_node1734329676604, "accelerometer_landing":accelerometer_landing_node1734329679152}, transformation_ctx = "SQLQuerytomergerecords_node1734329847277")

# Script generated for node Amazon S3
AmazonS3_node1734330190053 = glueContext.getSink(
  path="s3://udacity-stedi/customer/curated/", 
  connection_type="s3", 
  updateBehavior="UPDATE_IN_DATABASE", 
  partitionKeys=[], enableUpdateCatalog=True, 
  transformation_ctx="AmazonS3_node1734330190053"
)
AmazonS3_node1734330190053.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_curated")
AmazonS3_node1734330190053.setFormat("json")
AmazonS3_node1734330190053.writeFrame(SQLQuerytomergerecords_node1734329847277)

job.commit()
