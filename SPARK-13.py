
# coding: utf-8

# In[1]:

#문제 S-13: spark-submi


# In[ ]:

pwd


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_spark_hello.py', u'print "---------BEGIN-----------"\nimport pyspark\nconf = pyspark.SparkConf().setAppName("myAppName1")\nsc   = pyspark.SparkContext(conf=conf)\nsc.setLogLevel("ERROR")\nprint "---------RESULT-----------"\nprint sc\nrdd = sc.parallelize(range(1000), 10)\nprint "mean=",rdd.mean()\nnums = sc.parallelize([1, 2, 3, 4])\nsquared = nums.map(lambda x: x * x).collect()\nfor num in squared:\n    print "%i " % (num)')


# In[ ]:

#도스 실행
get_ipython().system(u'/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/bin/spark-submit src/ds_spark_hello.py')


# In[3]:


get_ipython().run_cell_magic(u'writefile', u'src/ds_spark_mongo.py', u'import pyspark\nconf=pyspark.SparkConf()\nconf = pyspark.SparkConf().setAppName("myAppName")\nconf.set("spark.mongodb.input.uri","mongodb://127.0.0.1/test.my2?readPreference=primaryPreferred")\nconf.set("spark.mongodb.output.uri","mongodb://127.0.0.1/test.my2")\nsc = pyspark.SparkContext(conf=conf)\n#sc = pyspark.SparkContext()\nsc.setLogLevel("ERROR")\nprint sc._conf.getAll()\nsqlContext = pyspark.sql.SQLContext(sc)\nprint "---------write-----------"\nmyRdd = sc.parallelize([\n        ("js", 150),\n        ("Gandalf", 1000),\n        ("Thorin", 195),\n        ("Balin", 178),\n        ("Kili", 77),\n        ("Dwalin", 169),\n        ("Oin", 167),\n        ("Gloin", 158),\n        ("Fili", 82),\n        ("Bombur", None)\n    ])\nmyDf = sqlContext.createDataFrame(myRdd, ["name", "age"])\nprint myDf\nmyDf.write.format("com.mongodb.spark.sql.DefaultSource").mode("overwrite").save()\nprint "---------read-----------"\ndf = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource").load()\nprint df.printSchema()\ndf.registerTempTable("myTable")\nmyTab = sqlContext.sql("SELECT name, age FROM myTable WHERE age >= 100")\nmyTab.show()')


# In[ ]:

#도스 실행
get_ipython().system(u'/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/bin/spark-submit src/ds_spark_mongo.py')


# In[2]:


get_ipython().run_cell_magic(u'writefile', u'src/ds_spark_twitter.py', u'import pyspark\nconf=pyspark.SparkConf()\nconf = pyspark.SparkConf().setAppName("myAppName")\nconf.set("spark.mongodb.input.uri","mongodb://127.0.0.1/ds_rest_subwayPassengers_mongo_db.db_rest_subway?readPreference=primaryPreferred")\nconf.set("spark.mongodb.output.uri","mongodb://127.0.0.1/ds_rest_subwayPassengers_mongo_db.db_rest_subway")\nsc = pyspark.SparkContext(conf=conf)\n#sc = pyspark.SparkContext()\nsc.setLogLevel("ERROR")\nprint sc._conf.getAll()\nsqlContext = pyspark.sql.SQLContext(sc)\nprint "---------read-----------"\ndf = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource").load()\nprint df.printSchema()\ndf.registerTempTable("myTwitter")\nmyTab = sqlContext.sql("SELECT CardSubwayStatisticsService.row.RIDE_PASGR_NUM FROM myTwitter")\nprint type(myTab)\nmyTab.show()')


# In[ ]:

#도스 실행
get_ipython().system(u'/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/bin/spark-submit src/ds_spark_twitter.py')


# In[ ]:


print myTab.first()
print myTab.head()


# In[ ]:




# In[ ]:



