
# coding: utf-8

# In[1]:

import requests
import re
weatherurl='http://openAPI.seoul.go.kr:8088/sample/xml/RealtimeWeatherStation/1/5/'
data=requests.get(weatherurl).text
print data
p=re.compile('<SAWS_TA_AVG>(.+?)</SAWS_TA_AVG>')
res=p.findall(data)
for item in res:
    print item


# In[2]:

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'중구'

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,STN_NM)
print params[31:]


# In[3]:

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url


# In[ ]:

import requests

data=requests.get(url).text
print data


# In[ ]:



