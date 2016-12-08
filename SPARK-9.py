
# coding: utf-8

# In[1]:

#문제 S-9: 정량데이터 분석


# In[ ]:

df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)


# In[ ]:

df.printSchema()


# In[ ]:

from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)


# In[ ]:

df1=model.transform(df)


# In[ ]:


df1.printSchema()


# In[ ]:

df1.show()


# In[2]:

labelIndexer = StringIndexer(inputCol="age", outputCol="att1")
model=labelIndexer.fit(df1)
df2=model.transform(df1)


# In[ ]:

labelIndexer = StringIndexer(inputCol="f1", outputCol="att2")
model=labelIndexer.fit(df2)
df3=model.transform(df2)


# In[ ]:

labelIndexer = StringIndexer(inputCol="f2", outputCol="att3")
model=labelIndexer.fit(df3)
df4=model.transform(df3)


# In[ ]:


labelIndexer = StringIndexer(inputCol="f3", outputCol="att4")
model=labelIndexer.fit(df4)
df5=model.transform(df4)


# In[ ]:

df5.printSchema()


# In[ ]:

df5.show()


# In[ ]:

##vector assembler


# In[ ]:

from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

va = VectorAssembler(inputCols=["att1","att2","att3","att4"],outputCol="features")
df6 = va.transform(df5)


# In[3]:

df7=df6.withColumnRenamed('labels','label')


# In[ ]:


df7.printSchema()


# In[ ]:

trainDf=df7.select('label','features')


# In[ ]:


trainDf.printSchema()


# In[ ]:

trainDf.show()


# In[ ]:

from pyspark.mllib.regression import LabeledPoint
trainRdd = trainDf.map(lambda row: LabeledPoint(row.label,row.features))


# In[ ]:

trainRdd.first()


# In[ ]:

from pyspark.sql.functions import udf
from pyspark.mllib.linalg import Vectors,VectorUDT
myudf=udf(lambda x: Vectors.dense(x), VectorUDT())
_trainDf2=trainDf.withColumn('dvf',myudf(trainDf.features))


# In[ ]:

##machine learning test


# In[4]:

trainDf.show()


# In[ ]:

from pyspark import SparkContext, SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier

li1 = StringIndexer(inputCol="cls", outputCol="_label")
li2 = StringIndexer(inputCol="age", outputCol="att1")
li3 = StringIndexer(inputCol="f1", outputCol="att2")
li4 = StringIndexer(inputCol="f2", outputCol="att3")
li5 = StringIndexer(inputCol="f3", outputCol="att4")
va = VectorAssembler(inputCols=["att1","att2","att3","att4"],outputCol="_features")

dt = DecisionTreeClassifier(labelCol="_label", featuresCol="_features")
pipeline = Pipeline(stages=[li1,li2,li3,li4,li5,va,dt])
model = pipeline.fit(df)
predictions = model.transform(df)

# Select example rows to display.
predictions.select("prediction", "_label", "_features").show()


# In[ ]:

from pyspark.ml.classification import NaiveBayes
nb = NaiveBayes(smoothing=1.0, modelType="multinomial")
model = nb.fit(trainDf)


# In[ ]:

from pyspark.sql import Row
test0 = sc.parallelize([Row(features=Vectors.dense([1.0,0.0,1.1,1.2]))]).toDF()
result = model.transform(test0).head()
result.prediction


# In[ ]:

from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint

def parseLine(line):
    parts = line.split(',')
    label = float(parts[0])
    features = Vectors.dense([float(x) for x in parts[1].split(' ')])
    print features
    return LabeledPoint(label, features)

data = sc.textFile('/home/jsl/Downloads/spark-1.6.0-bin-hadoop2.6/data/mllib/sample_naive_bayes_data.txt').map(parseLine)

# Split data aproximately into training (60%) and test (40%)
training, test = data.randomSplit([0.6, 0.4], seed=0)


# In[ ]:

model = NaiveBayes.train(training, 1.0)


# In[ ]:

* 위에서 내가 가공한 데이터


# In[ ]:




# In[ ]:



