
# coding: utf-8

# In[1]:

import urllib
url = "https://api.twitter.com/1.1/followers/list.json"

response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)


# In[2]:

print len(tfollower_json)
print type(tfollower_json)


# In[ ]:

for k,v in tfollower_json.iteritems():
    print k


# In[ ]:

for k,v in tfollower_json['users'][0].iteritems():
        print k


# In[ ]:

for i in tfollower_json['users']:
    print i['id'],i['screen_name']

