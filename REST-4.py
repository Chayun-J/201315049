
# coding: utf-8

# In[1]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX=str(1)
END_INDEX=str(5)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX)

print params[31:]


# In[ ]:

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url


# In[ ]:

import requests

data=requests.get(url).text
print data


# In[ ]:

print type(data.encode('utf-8'))


# In[ ]:

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text


# In[ ]:




# In[ ]:




# In[ ]:



