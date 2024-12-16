CREATE EXTERNAL TABLE `machine_learning_curated`(
  `sensorreadingtime` bigint, 
  `serialnumber` string, 
  `distancefromobject` int, 
  `user` string, 
  `timestamp` bigint, 
  `x` double, 
  `y` double, 
  `z` double)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://udacity-stedi/machine_learning/'
TBLPROPERTIES (
  'CreatedByJob'='machine_learning_curated', 
  'CreatedByJobRun'='jr_091b4baa9454d22a24be5fad80e0c6526e9119a5b0b686746d5bcbc3b5ff7cda', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
