
# coding: utf-8

# In[1]:

q = '#류현진'
count = 100
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets 
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']


# In[ ]:

print len(statuses)
print type(statuses)


# In[ ]:

print statuses[0].keys()


# In[2]:

import urllib
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)


# In[ ]:

print type(tsearch_json)
print tsearch_json.keys()
print len(tsearch_json['statuses'])


# In[ ]:

len(tsearch_json['statuses'][0])


# In[ ]:

for i,tweet in enumerate(tsearch_json['statuses']):
    #print tweet[u'user'][u'name']
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])


# In[ ]:




# In[ ]:




# In[ ]:



