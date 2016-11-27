
# coding: utf-8

# In[1]:

timeline = _client.statuses.home_timeline()


# In[ ]:

print type(timeline)
print len(timeline)


# In[ ]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]


# In[ ]:

from pymongo import MongoClient
_mclient = MongoClient()
_db=_mclient.ds_twitter
_table=_db.home_timeline


# In[2]:

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    _table.insert_one(tweet)


# In[ ]:

url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=2"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    print tweet['id'],tweet['text']


# In[ ]:

print home_timeline[0]['created_at']
print home_timeline[0]['id']


# In[ ]:

import urllib
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
myparam={'max_id':'532386310086881280'}
mybody=urllib.urlencode(myparam)

response, content = client.request(url+"?"+mybody, method="GET")
home_timeline = json.loads(content)


# In[ ]:

import urllib
myparam={'max_id':'534949539757555713','since_id':'532386310086881280'}

mybody=urllib.urlencode(myparam)

response, content = client.request(url+"?"+mybody, method="GET")
home_timeline = json.loads(content)


# In[ ]:



