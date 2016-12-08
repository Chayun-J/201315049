
# coding: utf-8

# In[1]:

#문제 S-7: Kolmogorov-Smirnov 검증


# In[ ]:

from pyspark.mllib.stat import Statistics

parallelData = sc.parallelize([1.0, 2.0, 5.0, 4.0, 3.0, 3.3, 5.5])

# run a KS test for the sample versus a standard normal distribution
testResult = Statistics.kolmogorovSmirnovTest(parallelData, "norm", 0, 1)
print(testResult)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



