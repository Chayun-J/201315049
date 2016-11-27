
# coding: utf-8

# In[1]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]


# In[ ]:

import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url


# In[ ]:

import requests
data=requests.get(url).text
print data


# In[ ]:

type(data)


# In[2]:

import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item    


# In[ ]:

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))


# In[ ]:

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text


# In[ ]:

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text

