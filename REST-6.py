
# coding: utf-8

# In[1]:

import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'


# In[ ]:

_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    #print _api
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1


# In[ ]:

_type='json'


# In[ ]:

_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)


# In[2]:

data=requests.get(_api).text
print data


# In[3]:

import json
jd = json.loads(data)
#print jd['STATION_NM']
#for key,value in jd.items():
#    print "---",key,value

print jd['SearchSTNBySubwayLineService']['row'][0]
#n=len(jd['SearchSTNBySubwayLineService']['row'])
#for i in range(0,n):
#    print jd['SearchSTNBySubwayLineService']['row'][i]
for item in jd['SearchSTNBySubwayLineService']['row']:
    print item.keys()
    for i in item.keys():
        if i=='STATION_NM':
            print ''.join(item.values())
            print item.values()[1]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



