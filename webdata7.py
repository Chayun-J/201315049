
# coding: utf-8

# In[4]:

url = 'http://www.bbc.co.uk/sport/football/premier-league/results'


# In[5]:

import requests
r=requests.get(url)
_html=r.text


# In[6]:

import requests
r=requests.get(url)
_html=r.text


# In[7]:

_html.find('table-stats')


# In[8]:

def getIndicesOfAllTableStats(string, query):
    listindex=list()
    offset=0
    i = string.find(query, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(query, i + 1)
    return listindex


# In[9]:

param1=_html
param2='table-stats'
_indices=getIndicesOfAllTableStats(param1, param2)
print _indices


# In[10]:

from scrapy.selector import Selector
nodes=Selector(text=_html).xpath("//table[@class='table-stats']/tbody/tr[@class='report']/td[@class='match-details']/p")


# In[11]:

print nodes[0].extract()


# In[12]:

for node in nodes:
    home_team = node.xpath("span[@class='team-home teams']/a/text()").extract()
    score = node.xpath("span[@class='score']/abbr/text()").extract()
    away_team = node.xpath("span[@class='team-away teams']/a/text()").extract()
    if home_team and score and away_team:
        home_team = home_team[0].strip()
        score = score[0].strip()
        home_goals = int(score.split('-')[0])
        away_goals = int(score.split('-')[1])
        away_team = away_team[0].strip()
    print home_team, score, home_goals, away_goals, away_team


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



