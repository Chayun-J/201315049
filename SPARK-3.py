
# coding: utf-8

# In[1]:

celsius = [39.2, 36.5, 37.3, 37.8]
def c2f(c):
    f=list()
    for i in c:
        _f=(float(9)/5)*i + 32
        f.append(_f)
    return f

print c2f(celsius)


# In[ ]:

celsius = [39.2, 36.5, 37.3, 37.8]

def c2f(c):
    return (float(9)/5)*c + 32

f=map(c2f, celsius)
print f


# In[ ]:

map(lambda c:(float(9)/5)*c + 32, celsius)


# In[ ]:

sentence = 'Hello World'
words = sentence.split()
print words


# In[ ]:

sentence = "Hello World"
map(lambda x:x.split(),sentence)


# In[2]:

sentence = ["Hello World"]
map(lambda x:x.split(),sentence)


# In[ ]:

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result


# In[ ]:

reduce(lambda x, y: x+y, range(1,101))


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'data/ds_spark_wiki.txt', u"Wikipedia\nApache Spark is an open source cluster computing framework.\n\uc544\ud30c\uce58 \uc2a4\ud30c\ud06c\ub294 \uc624\ud508 \uc18c\uc2a4 \ud074\ub7ec\uc2a4\ud130 \ucef4\ud4e8\ud305 \ud504\ub808\uc784\uc6cc\ud06c\uc774\ub2e4.\nOriginally developed at the University of California, Berkeley's AMPLab,\nthe Spark codebase was later donated to the Apache Software Foundation,\nwhich has maintained it since.\nSpark provides an interface for programming entire clusters with\nimplicit data parallelism and fault-tolerance.")


# In[ ]:

textFile = sc.textFile("data/ds_spark_wiki.txt")


# In[3]:

textFile.first()


# In[ ]:

words=textFile.map(lambda x:x.split(' '))


# In[ ]:

words.collect()


# In[4]:

textFile.map(lambda s:len(s)).collect()


# In[ ]:

_sparkLine=textFile.filter(lambda line: "Spark" in line)


# In[ ]:

print _sparkLine.count()


# In[ ]:

_line = textFile.filter(lambda line: u"스파크" in line)


# In[5]:

print _line.first()


# In[ ]:

_aList=[1,2,3]
rdd = sc.parallelize(_aList)


# In[ ]:

rdd.take(3)


# In[ ]:

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
print squared


# In[ ]:

a=["this is","a line"]
_rdd=sc.parallelize(a)

words=_rdd.map(lambda x:x.split())
print words.collect()


# In[ ]:

_upper=_rdd.map(lambda x:x.replace("a","AA"))
_upper.take(10)


# In[6]:

's'.upper()


# In[ ]:

pluralRDD =words.map(lambda x: x[0].upper())
print pluralRDD.collect()


# In[ ]:

pluralRDD =words.map(lambda x: [i.upper() for i in x])
print pluralRDD.collect()


# In[ ]:

pluralRDD =words.map(lambda x: [i.upper() for i in x]).collect()
print pluralRDD
    


# In[ ]:

wordsLength = words    .map(len)    .collect()
print wordsLength


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'./data/ds_spark_2cols.csv', u'35, 2\n40, 27\n12, 38\n15, 31\n21, 1\n14, 19\n46, 1\n10, 34\n28, 3\n48, 1\n16, 2\n30, 3\n32, 2\n48, 1\n31, 2\n22, 1\n12, 3\n39, 29\n19, 37\n25, 2')


# In[ ]:

inp_file = sc.textFile("./data/ds_spark_2cols.csv")
numbers_rdd = inp_file.map(lambda line: line.split(','))


# In[ ]:

numbers_rdd.take(10)


# In[ ]:

data_home=os.path.join(home,"Code/git/else/uber-tlc-foil-response")
filePath=os.path.join(data_home,"Uber-Jan-Feb-FOIL.csv")


# In[ ]:

_fub = sc.textFile(filePath)


# In[7]:

type(_fub)


# In[ ]:

_fub.count()


# In[ ]:

_fub.first()


# In[ ]:

_dub = _fub.map(lambda line: line.split(","))


# In[ ]:

type(_dub)


# In[ ]:





_row0keys=_dub.map(lambda row: row[0]).distinct().collect()


# In[ ]:





print _row0keys


# In[ ]:

_dub.filter(lambda row: "B02512" in row).count()


# In[8]:

_dub.filter(lambda row: "B02512" in row).filter(lambda row: int(row[3])>2000).collect()


# In[ ]:

_noheader = _fub.filter(lambda line: "base" not in line).map(lambda line:line.split(","))
_noheader.count()


# In[ ]:

_noheader.map(lambda x: (x[0], int(x[3]))).reduceByKey(lambda k,v: k + v).collect()

