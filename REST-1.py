
# coding: utf-8

# In[1]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr


# In[ ]:

type(geostr)


# In[ ]:

import json
geojson=json.loads(geostr)


# In[ ]:

type(geojson)


# In[ ]:

print geojson['ip']


# In[ ]:

geojson.get('ip')


# In[ ]:

country=geojson.get('country_code')


# In[2]:

print country.decode('utf-8')


# In[ ]:

import json
import urllib

def getCountry(ipAddress):
    response = urllib.urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("39.118.87.152"))


# In[ ]:

import requests
send_url = 'http://freegeoip.net/json/39.118.87.152'
r = requests.get(send_url)


# In[ ]:

j=json.loads(r.text)


# In[ ]:

type(j)


# In[ ]:

print j.keys()


# In[ ]:

print j['city']


# In[ ]:

for k,v in j.iteritems():
    print k,"\t: ",v


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



