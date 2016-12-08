
# coding: utf-8

# In[1]:

#S.6: DataFrame


# In[3]:

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


# In[ ]:

from pyspark.sql import Row
Person = Row('name', 'height')
rows = [Person('kim', 170), Person('lee', 175), Person('lim', 180),]
#rowsRdd = sc.parallelize(rows)
#rowsDf = sqlCtx.createDataFrame(rowsRdd)

rowsDF=sqlCtx.createDataFrame(rows)


# In[ ]:

rowsDF.printSchema()


# In[ ]:

rowsDF.where(rowsDF.height < 175)    .select([rowsDF.name, rowsDF.height]).show()


# In[ ]:


rowsDF.groupby(rowsDF.height).max().show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



