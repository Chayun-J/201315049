
# coding: utf-8

# In[1]:

import os
import findspark

home=os.getenv("HOME")
spark_home=os.path.join(home,"Downloads/spark-1.6.0-bin-hadoop2.6")
findspark.init(spark_home)


# In[ ]:

import pyspark
conf=pyspark.SparkConf()
conf = pyspark.SparkConf().setAppName("myAppName")
sc = pyspark.SparkContext(conf=conf)


# In[ ]:

print sc


# In[2]:

sc.version   


# In[ ]:

sc.master


# In[ ]:

sc._conf.get("spark.jars.packages")


# In[ ]:

sc._conf.getAll()

