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

# Script generated for node customer_landing
customer_landing_node1734287049342 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_landing", transformation_ctx="customer_landing_node1734287049342")

# Script generated for node customers_who_agreed_to_share
SqlQuery0 = '''
select * from customer_landing
where sharewithresearchasofdate is not null;
'''
customers_who_agreed_to_share_node1734287077378 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"customer_landing":customer_landing_node1734287049342}, transformation_ctx = "customers_who_agreed_to_share_node1734287077378")

# Script generated for node Amazon S3
AmazonS3_node1734287365779 = glueContext.getSink(path="s3://udacity-stedi/customer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1734287365779")
AmazonS3_node1734287365779.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_trusted")
AmazonS3_node1734287365779.setFormat("json")
AmazonS3_node1734287365779.writeFrame(customers_who_agreed_to_share_node1734287077378)
job.commit()
