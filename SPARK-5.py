
# coding: utf-8

# In[11]:

#json 파일 읽기


# In[ ]:

# %load /home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json
{"name":"Michael"}
{"name":"Andy", "age":30}
{"name":"Justin", "age":19}


# In[ ]:




# In[2]:

pDF= sqlCtx.read.json("/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[4]:

type(pDF)


# In[5]:

pDF.filter(pDF['age'] > 21).show()


# In[13]:

pDF.registerTempTable("people")
sqlCtx.sql("select name from people").show()


# In[ ]:

#twitter json을 읽을 경우


# In[7]:

twitterDF= sqlCtx.read.json("src/ds_twitter_1_noquote.json")


# In[8]:

twitterDF.printSchema()


# In[ ]:

twitterDF.select('text').show()


# In[15]:

twitterDF.registerTempTable("twitter")
sqlCtx.sql("select text from twitter").show()


# In[ ]:

#json frm url


# In[ ]:

import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")


# In[9]:

wc=r.json()


# In[ ]:

type(wc)


# In[ ]:

wcDF=sqlCtx.createDataFrame(wc)


# In[ ]:

wcDF.printSchema()


# In[14]:

wcDF.registerTempTable("wc")
sqlCtx.sql("select Club,Team,Year from wc").show(1)


# In[ ]:

#json frm url


# In[ ]:

import json
import requests
_url="https://health.data.ny.gov/api/views/jxy9-yhdk/rows.json?accessType=DOWNLOAD"
_json=requests.get(_url).json()


# In[ ]:

json.keys()


# In[10]:

_jsonList=_json['data']
print len(_jsonList)


# In[ ]:

_json['data'][0]


# In[ ]:

_df=sqlCtx.createDataFrame(_json['data'])
_df.count()


# In[ ]:

_df.printSchema()


# In[ ]:

_df.filter(_df['_10'] == u'GAVIN').show(2)


# In[16]:

_df.registerTempTable("babyNames")
sqlCtx.sql("select distinct(_10) from babyNames").show(5)


# In[ ]:

#read from text


# In[ ]:

# %load /home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.txt
Michael, 29
Andy, 30
Justin, 19


# In[ ]:

from pyspark.sql import Row
lines = sc.textFile("/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))

schemaPeople = sqlCtx.createDataFrame(people)
schemaPeople.registerTempTable("people")


# In[ ]:


# The results of SQL queries are RDDs and support all the normal RDD operations.
teenNames = teenagers.map(lambda p: "Name: " + p.name)
for teenName in teenNames.collect():
  print(teenName)


# In[17]:

schemaString = "name age"

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

sqlCtx.createDataFrame(people,schema)


# In[18]:

#csv


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'data/ds_spark.csv', u'1,2,3,4\n11,22,33,44\n111,222,333,444')


# In[ ]:


from pyspark.sql import SQLContext

sqlContext = SQLContext(sc)
df = sqlContext.read.format('com.databricks.spark.csv')    .options(header='true', inferschema='true').load('data/ds_spark.csv')

df.show()

df.withColumnRenamed('1','label')

