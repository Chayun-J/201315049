{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5980"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from urllib import urlopen\n",
    "keyword='python'\n",
    "resp = urlopen('https://www.google.com/search?q='+keyword)\n",
    "html=resp.read()\n",
    "len(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "error\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "p=re.compile('.*(error).*')\n",
    "print p.search(html).group(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import webbrowser\n",
    "webbrowser.open('http://www.google.com/search?q=python')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "302  {'Date': 'Mon, 10 Oct 2016 07:29:46 GMT', 'Content-Length': '261', 'Content-Type': 'text/html; charset=UTF-8', 'Location': 'http://www.google.co.kr/?gfe_rd=cr&ei=akP7V4OzBMHC8gfi9oHIDA', 'Cache-Control': 'private'}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "resp = requests.head(\"http://www.google.com\")\n",
    "print resp.status_code, resp.text, resp.headers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date: Mon, 10 Oct 2016 07:29:55 GMT\r\n",
      "Expires: -1\r\n",
      "Cache-Control: private, max-age=0\r\n",
      "Content-Type: text/html; charset=EUC-KR\r\n",
      "P3P: CP=\"This is not a P3P policy! See https://www.google.com/support/accounts/answer/151657?hl=en for more info.\"\r\n",
      "Server: gws\r\n",
      "X-XSS-Protection: 1; mode=block\r\n",
      "X-Frame-Options: SAMEORIGIN\r\n",
      "Set-Cookie: NID=88=GmRkylv_6DHalO17oU6_9QEpXsYcbMa1f4MhSK_HQeHEMUqjiNCfrFlbcTkZFNEe5JllW6j-jiO8EODtvhLBdnhflmhWzQ7TxJmwWAJOwrEyU39-mdiHs9rswusdab45; expires=Tue, 11-Apr-2017 07:29:55 GMT; path=/; domain=.google.co.kr; HttpOnly\r\n",
      "Accept-Ranges: none\r\n",
      "Vary: Accept-Encoding\r\n",
      "Connection: close\r\n",
      "\n",
      "http://www.google.co.kr/index.html?gfe_rd=cr&ei=c0P7V7j7JceQ8QeQu5iwBQ\n"
     ]
    }
   ],
   "source": [
    "import urllib2\n",
    "class HeadRequest(urllib2.Request):\n",
    "     def get_method(self):\n",
    "         return \"HEAD\"\n",
    "\n",
    "response = urllib2.urlopen(HeadRequest(\"http://google.com/index.html\"))\n",
    "print response.info()\n",
    "print response.geturl()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Python-urllib/1.17'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 파이썬에서 사용하는 기본 User Agent\n",
    "from urllib import URLopener\n",
    "URLopener.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'My new User-Agent'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 연습으로 자신의 User Agent 설정\n",
    "from urllib import FancyURLopener\n",
    "class MyOpener(FancyURLopener):\n",
    "    version = 'My new User-Agent'\n",
    "MyOpener.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 리눅스 Firefox User Agent 예\n",
    "# 맥 Safari User Agent 예\n",
    "class MyOpener(FancyURLopener):\n",
    "    #version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'\n",
    "    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'\n",
    "MyOpener.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "myopener = MyOpener()\n",
    "page = myopener.open('http://www.google.com/search?q=python')\n",
    "html=page.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "file://localhostC:\\Users\\TM\\Documents\\mygoogle.html\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "f=open('mygoogle.html','w')\n",
    "f.write(html)\n",
    "f.close()\n",
    "import webbrowser\n",
    "mygoogle='file://'+'localhost'+os.path.join(os.getcwd(), 'mygoogle.html')\n",
    "print mygoogle\n",
    "webbrowser.open(mygoogle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "51\n",
      "https://www.google.co.kr/intl/ko/options/\n",
      "https://accounts.google.com/ServiceLogin?hl=ko&amp;passive=true&amp;continue=https://www.google.co.k\n",
      "https://www.google.com/url?q=/chrome/browser/desktop/index.html%3Fhl%3Dko%26brand%3DHLDY%26utm_sourc\n",
      "https://www.google.co.kr/webhp?hl=ko&amp;sa=X&amp;ved=0ahUKEwin2a2C3M_PAhWBLY8KHX7hAd0QPAgD\n",
      "https://www.python.org/\n",
      "https://www.python.org/\n",
      "https://www.python.org/\n",
      "https://webcache.googleusercontent.com/search?q=cache:Fvb7Gz_c4rwJ:https://www.python.org/+&amp;cd=2\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=https://www.python.org/&amp;prev=sear\n",
      "https://www.python.org/downloads/\n",
      "https://webcache.googleusercontent.com/search?q=cache:mKMOugLFVo8J:https://www.python.org/downloads/\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=https://www.python.org/downloads/&amp\n",
      "https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC\n",
      "https://webcache.googleusercontent.com/search?q=cache:OL25IRr7kSMJ:https://ko.wikipedia.org/wiki/%25\n",
      "https://en.wikipedia.org/wiki/Python_(programming_language)\n",
      "https://webcache.googleusercontent.com/search?q=cache:3wRBXLyvECcJ:https://en.wikipedia.org/wiki/Pyt\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=https://en.wikipedia.org/wiki/Python_\n",
      "https://wikidocs.net/6\n",
      "https://webcache.googleusercontent.com/search?q=cache:LmCkGjF_ShkJ:https://wikidocs.net/6+&amp;cd=6&\n",
      "https://tutorial.djangogirls.org/ko/python_introduction/\n",
      "https://webcache.googleusercontent.com/search?q=cache:9o-y50p1vcYJ:https://tutorial.djangogirls.org/\n",
      "https://www.codecademy.com/learn/python\n",
      "https://webcache.googleusercontent.com/search?q=cache:VieTLWvITEcJ:https://www.codecademy.com/learn/\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=https://www.codecademy.com/learn/pyth\n",
      "https://www.codecademy.com/ko/tracks/python-ko\n",
      "https://webcache.googleusercontent.com/search?q=cache:cCt2AOEUzsYJ:https://www.codecademy.com/ko/tra\n",
      "https://www.tutorialspoint.com/python/\n",
      "https://webcache.googleusercontent.com/search?q=cache:mWd-kiWxLAYJ:https://www.tutorialspoint.com/py\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=https://www.tutorialspoint.com/python\n",
      "https://translate.google.co.kr/translate?hl=ko&amp;sl=en&amp;u=http://planetpython.org/&amp;prev=sea\n",
      "https://support.google.com/websearch?p=ws_settings_location&amp;hl=ko\n",
      "https://www.google.com/search?q=python&amp;gws_rd=cr,ssl&amp;ei=3UP7V7LACcjlvgTRxbToBg&amp;fg=1\n",
      "https://myaccount.google.com/?utm_source=OGB\n",
      "https://www.google.co.kr/webhp?tab=ww&amp;ei=3UP7V-vxIov_vgTXoa2oCw&amp;ved=0EKkuCAEoAQ\n",
      "https://maps.google.co.kr/maps?hl=ko&amp;tab=wl\n",
      "https://www.youtube.com/?gl=KR\n",
      "https://play.google.com/?hl=ko&amp;tab=w8\n",
      "https://news.google.co.kr/nwshp?hl=ko&amp;tab=wn&amp;ei=3UP7V-vxIov_vgTXoa2oCw&amp;ved=0EKkuCAUoBQ\n",
      "https://mail.google.com/mail/?tab=wm\n",
      "https://drive.google.com/?tab=wo\n",
      "https://www.google.com/calendar?tab=wc\n",
      "https://plus.google.com/?gpsrc=ogpy0&amp;tab=wX\n",
      "https://translate.google.co.kr/?hl=ko&amp;tab=wT\n",
      "https://photos.google.com/?tab=wq\n",
      "https://www.google.co.kr/intl/ko/options/\n",
      "https://docs.google.com/document/?usp=docs_alc\n",
      "https://books.google.co.kr/bkshp?hl=ko&amp;tab=wp&amp;ei=3UP7V-vxIov_vgTXoa2oCw&amp;ved=0EKkuCA0oDQ\n",
      "https://www.blogger.com/?tab=wj\n",
      "https://www.google.com/contacts/?hl=ko&amp;tab=wC\n",
      "https://hangouts.google.com/\n",
      "https://www.google.co.kr/intl/ko/options/\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "p=re.compile('href=\"(https://.*?)\"')\n",
    "#p=re.compile('.*href.*')\n",
    "res=p.findall(html)\n",
    "print len(res)\n",
    "for item in res:\n",
    "    print item[:100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "q=python+programming+tutorials\n"
     ]
    }
   ],
   "source": [
    "import urllib2\n",
    "import urllib\n",
    "googleurl = 'https://www.google.com/search'\n",
    "keyValues = {'q' : 'python programming tutorials'}\n",
    "request = urllib.urlencode(keyValues)\n",
    "print request\n",
    "request = request.encode('utf-8') # data should be bytes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<urllib2.Request instance at 0x0000000003D72EC8>\n",
      "https://www.google.com/search?q=python+programming+tutorials\n",
      "<bound method Request.get_method of <urllib2.Request instance at 0x0000000003D72EC8>>\n"
     ]
    }
   ],
   "source": [
    "req = urllib2.Request(googleurl+'?'+request)\n",
    "print req\n",
    "\n",
    "print req.get_full_url()\n",
    "\n",
    "print req.get_method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "HTTPError",
     "evalue": "HTTP Error 403: Forbidden",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-d561d904ac74>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murllib2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmyopener\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[0;32m    152\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    153\u001b[0m         \u001b[0mopener\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 154\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    155\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    156\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0minstall_opener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mopener\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mopen\u001b[1;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[0;32m    433\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mprocessor\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprocess_response\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprotocol\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    434\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 435\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    436\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    437\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mhttp_response\u001b[1;34m(self, request, response)\u001b[0m\n\u001b[0;32m    546\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m200\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mcode\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    547\u001b[0m             response = self.parent.error(\n\u001b[1;32m--> 548\u001b[1;33m                 'http', request, response, code, msg, hdrs)\n\u001b[0m\u001b[0;32m    549\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    550\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36merror\u001b[1;34m(self, proto, *args)\u001b[0m\n\u001b[0;32m    465\u001b[0m             \u001b[0mhttp_err\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    466\u001b[0m         \u001b[0margs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mproto\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 467\u001b[1;33m         \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    468\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    469\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36m_call_chain\u001b[1;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[0;32m    405\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    406\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 407\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    408\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    409\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mhttp_error_302\u001b[1;34m(self, req, fp, code, msg, headers)\u001b[0m\n\u001b[0;32m    652\u001b[0m         \u001b[0mfp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    653\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 654\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    655\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    656\u001b[0m     \u001b[0mhttp_error_301\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mhttp_error_303\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mhttp_error_307\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mhttp_error_302\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mopen\u001b[1;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[0;32m    433\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mprocessor\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprocess_response\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprotocol\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    434\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 435\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    436\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    437\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mhttp_response\u001b[1;34m(self, request, response)\u001b[0m\n\u001b[0;32m    546\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m200\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mcode\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    547\u001b[0m             response = self.parent.error(\n\u001b[1;32m--> 548\u001b[1;33m                 'http', request, response, code, msg, hdrs)\n\u001b[0m\u001b[0;32m    549\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    550\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36merror\u001b[1;34m(self, proto, *args)\u001b[0m\n\u001b[0;32m    471\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mhttp_err\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    472\u001b[0m             \u001b[0margs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'default'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'http_error_default'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0morig_args\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 473\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    474\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    475\u001b[0m \u001b[1;31m# XXX probably also want an abstract factory that knows when it makes\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36m_call_chain\u001b[1;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[0;32m    405\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    406\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 407\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    408\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    409\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\TM\\Anaconda4\\lib\\urllib2.pyc\u001b[0m in \u001b[0;36mhttp_error_default\u001b[1;34m(self, req, fp, code, msg, hdrs)\u001b[0m\n\u001b[0;32m    554\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mHTTPDefaultErrorHandler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBaseHandler\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    555\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mhttp_error_default\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 556\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_full_url\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    557\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    558\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mHTTPRedirectHandler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBaseHandler\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mHTTPError\u001b[0m: HTTP Error 403: Forbidden"
     ]
    }
   ],
   "source": [
    "resp = urllib2.urlopen(req)\n",
    "resp = myopener.open(req)\n",
    "html = resp.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{{About|the programming language|the snake genus|Python (genus)|other uses|Python (disambiguation)}}\n",
      "{{Use dmy dates|date=August 2015}}\n",
      "{{Infobox programming language\n",
      "|name                   = Python\n",
      "|logo                   = Python logo and wordmark.svg\n",
      "|logo size              = 260px\n",
      "|paradigm               = [[multi-paradigm programming language|multi-paradigm]]: [[object-oriented programming|object-oriented]], [[imperative programming|imperative]], [[functional programming|functional]], [[procedural programming|procedural]], [[reflective programming|reflective]]\n",
      "|released               = {{Start date and age|1991|02|20|df=yes}}<ref>{{cite web|url=http://python-history.blogspot.com/2009/01/brief-timeline-of-python.html|title=The History of Python: A Brief Timeline of Python|work=[[Blogger (service)|Blogger]]|date=2009-01-20|accessdate=2016-03-20}}</ref>\n",
      "|designer               = [[Guido van Rossum]]\n",
      "|developer              = [[Python Software Foundation]]\n",
      "|latest release version = 3.5.2 / {{Start date and age|2016|06|27|df=yes}}<ref>{{cite web |url=http://blog.python.org/2016/06/python-352-and-python-345-are-now.html |title=Python 3.5.2 and Python 3.4.5 are now available |website=Python Insider |publisher=The Python Core Developers |first=Larry |last=Hastings |date=2016-06-27 |accessdate=2016-06-28}}</ref><br>2.7.12 / {{Start date and age|2016|06|28|df=yes}}<ref>{{cite web |url=http://blog.python.org/2016/06/python-2712-released.html |title=Python 2.7.12 released |website=Python Insider |publisher=The Python Core Developers |first=Benjamin |last=Peterson |date=2016-06-28 |accessdate=2016-06-28}}</ref>\n",
      "|latest preview version = 3.6.0b1 / {{Start date and age|2016|09|12df=yes}}<ref name=\"Python Release Python 3.6.0b1\">{{cite web |url=https://www.python.org/downloads/release/python-360b1/.html |title=Python Release Python 3.6.0b1|publisher=Python Software Foundation|accessdate=17 September 2016}}</ref><!-- <br>2.7.9rc1 / {{Start date and age|2014|11|26|df=yes}}<ref>{{cite web |url=https://www.python.org/downloads/release/python-279rc1/ |title=Python 2.7.9 rc1 Release |publisher=Python Software Foundation |accessdate=26 November 2014}}</ref -->\n",
      "|latest preview date    = \n",
      "|typing                 = [[duck typing|duck]], [[dynamic typing|dynamic]], [[strong typing|strong]], [[gradual typing|gradual]] (as of Python 3.5)<ref>{{cite web|url=https://lwn.net/Articles/627418/|title=Type hinting for Python|publisher=LWN.net|date=24 December 2014|accessdate=5 May 2015}}</ref>\n",
      "|implementations        = [[CPython]], [[IronPython]], [[Jython]], [[MicroPython]], [[PyPy]]\n",
      "|dialects               = [[Cython]], [[RPython]], [[Stackless Python]]\n",
      "|influenced             = [[Boo (programming language)|Boo]], [[Cobra (programming language)|Cobra]], [[CoffeeScript]],<ref>{{cite web|url=http://coffeescript.org/|title=CoffeeScript borrows chained comparisons from Python}}</ref> [[D (programming language)|D]], [[F Sharp (programming language)|F#]], [[Falcon (programming language)|Falcon]], [[Genie (programming language)|Genie]],<ref>{{cite web \n",
      "|url=https://wiki.gnome.org/action/show/Projects/Genie\n",
      "|title=Genie Language - A brief guide \n",
      "|accessdate=2015-12-28}}</ref> [[Go (programming language)|Go]], [[Groovy (programming language)|Groovy]], [[JavaScript]],<ref>{{cite web\n",
      "|title = Perl and Python influences in JavaScript\n",
      "|date= 24 February 2013\n",
      "|website= www.2ality.com\n",
      "|url= http://www.2ality.com/2013/02/javascript-influences.html\n",
      "|accessdate= 15 May 2015}}</ref><ref>{{cite web\n",
      "|title = Chapter 3: The Nature of JavaScript; Influences\n",
      "|last=Rauschmayer\n",
      "|first=Axel\n",
      "|website=O'Reilly, Speaking JavaScript\n",
      "|url= http://speakingjs.com/es5/ch03.html\n",
      "|accessdate= 15 May 2015}}</ref> [[Julia (programming language)|Julia]],<ref name=Julia/> [[Nim (programming language)|Nim]], [[Ruby (programming language)|Ruby]],<ref name=\"bini\"/> [[Swift (programming language)|Swift]],<ref name=\"lattner2014\">{{cite web|url=http://nondot.org/sabre/|title=Chris Lattner's Homepage|last=Lattner|first=Chris|date=3 June 2014|accessdate=3 June 2014|publisher=Chris Lattner|quote=The Swift language is the product of tireless effort from a team of language experts, documentation gurus, compiler optimization ninjas, and an incredibly important internal dogfooding group who provided feedback to help refine and battle-test ideas. Of course, it also greatly benefited from the experiences hard-won by many other languages in the field, drawing ideas from Objective-C, Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list.}}</ref>\n",
      "|operating system       = [[Cross-platform]]\n",
      "|license                = [[Python Software Foundation License]]\n",
      "|website                = {{URL|https://www.python.org/}}\n",
      "|wikibooks              = Python Programming\n",
      "|influenced_by          = [[ABC (programming language)|ABC]],<ref name=\"faq-created\"/> [[ALGOL 68]],<ref name=\"98-interview\"/> [[C (programming language)|C]],<ref name=\"AutoNT-1\"/> [[C++]],<ref name=\"classmix\"/> [[Dylan (prog\n"
     ]
    }
   ],
   "source": [
    "import urllib\n",
    "keyword='Albert_Einstein'\n",
    "keyword='Python (programming language)'\n",
    "s = urllib.urlopen('http://en.wikipedia.org/w/index.php?action=raw&title='+keyword).read()\n",
    "#print s.find('Python is a widely used general-purpose')\n",
    "print s[:5000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "import requests\n",
    "\n",
    "r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')\n",
    "# build the DOM Tree\n",
    "tree = lxml.html.fromstring(r.text)\n",
    "# print the parsed DOM Tree\n",
    "#print lxml.html.tostring(tree)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<Element div at 0x4049e58>]\n"
     ]
    }
   ],
   "source": [
    "sel = CSSSelector('#mw-content-text > div:nth-child(1)')\n",
    "# Apply the selector to the DOM tree.\n",
    "results = sel(tree)\n",
    "print results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<div role=\"note\" class=\"hatnote\">This article is about the programming language. For the snake genus, see <a href=\"/wiki/Python_(genus)\" title=\"Python (genus)\">Python (genus)</a>. For other uses, see <a href=\"/wiki/Python_(disambiguation)\" class=\"mw-redirect mw-disambig\" title=\"Python (disambiguation)\">Python (disambiguation)</a>.</div>\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# print the HTML for the first result.\n",
    "match = results[0]\n",
    "print lxml.html.tostring(match)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This article is about the programming language. For the snake genus, see \n"
     ]
    }
   ],
   "source": [
    "# print the text of the first result.\n",
    "print match.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This article is about the programming language. For the snake genus, see \n"
     ]
    }
   ],
   "source": [
    "for result in results:\n",
    "    print result.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
