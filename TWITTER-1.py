
# coding: utf-8

# In[1]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client






<twitter.api.Twitter object 


# In[ ]:

_client.statuses.update(status="Hello Twitter 1 160924")


# In[ ]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[2]:

client = oauth.Client(consumer, token)


# In[ ]:

help(client.request)


# In[ ]:

import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 160924'})
response,content=client.request(url,method='POST',body=mybody)


# In[ ]:

import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)


# In[ ]:



