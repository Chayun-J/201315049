{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib\n",
    "keyword='비오는'\n",
    "f = urllib.urlopen(\"http://music.naver.com/search/search.nhn?query=\"+keyword+\"&x=0&y=0\")\n",
    "mydata = f.read();"
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
      "--- 비 오는 거리\n",
      "131002\n",
      "title=\"검색어 입력\" value=\"비오는\" maxlength=\"50\" accesskey=\"s\"\n",
      "title=\"비오는날\" alt=\"비오는날\"\n",
      "title=\"비오는 금요일\" alt=\"비오는 금요일\"\n",
      "title=\"비 오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"1집 비오는 거리\" class=\"_album NPI=a:album,r:1,i:682\"><span class=\"ellipsis\"\n",
      "title=\"비오는 날 수채화\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 날 수채화 1 OST\" class=\"_album NPI=a:album,r:2,i:33001\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" class=\"_album NPI=a:album,r:3,i:656486\"><span class=\"ellipsis\"\n",
      "title=\"비오는거리\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 거리\" class=\"_album NPI=a:album,r:4,i:761336\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리\" class=\"_album NPI=a:album,r:5,i:442032\"><span class=\"ellipsis\"\n",
      "title=\"비오는 날 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 날\" class=\"_album NPI=a:album,r:6,i:649010\"><span class=\"ellipsis\"\n",
      "title=\"비오는날 (동요) (멜로디 MR)\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 압구정\" ><span class=\"ellipsis\"\n",
      "title=\"김현주의 비오는 거리\" class=\"_album NPI=a:album,r:10,i:117082\"><span class=\"ellipsis\"\n",
      "title=\"비오는 밤에\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리  (Feat. 핫펠트)\" ><span class=\"ellipsis\"\n",
      "title=\"뉴에이지 연가 : 비 오는 날의 거리, 추억, 그리고 아름다운 재즈 피아노(Pop 올드 팝, 클래식, 영화 OST 베스트 연주 음악)\" class=\"_album NPI=a:album,r:13,i:636985\"><span class=\"ellipsis\"\n",
      "title=\"비오는 남산\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 오솔길\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 금요일\"\n",
      "title=\"비오는 금요일\" alt=\"비오는 금요일\" class=\"NPI=a:artist,r:,i:271713\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비오는 카페\"\n",
      "title=\"유ㄹish.1 - 비오는 거리\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비오는 압구정\"\n",
      "title=\"비오는 날에\"\n",
      "title=\"비오는 거리 (Feat. 단비)\"\n",
      "title=\"비오는 날의 수채화\"\n",
      "title=\"[cover] 비오는 거리 - 줄리\"\n",
      "title=\"비 오는 날의 분수\"\n",
      "title=\"비 오는 날, 생각나는 그 노래\"\n",
      "title=\"비오는 날 [데모]\"\n",
      "title=\"비오는 밤에\"\n"
     ]
    }
   ],
   "source": [
    "pos = mydata.find(\"트랙 리스트\")\n",
    "if (pos>0):\n",
    "    pos = mydata.find(\"_title title NPI=\", pos);\n",
    "    pos = mydata.find(\"title=\",pos+20)\n",
    "    pos2 = mydata.find(\"\\\"\", pos+8)\n",
    "    print \"---\",mydata[pos+7:pos2]\n",
    "print len(mydata)\n",
    "\n",
    "import re\n",
    "p=re.compile('title=\".*비.?오는.*\"')\n",
    "#res=p.search(data)\n",
    "res=p.findall(mydata)\n",
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "\n",
    "html = lxml.html.fromstring(mydata)\n",
    "#tree=lxml.etree.parse('myhtml')\n",
    "# construct a CSS Selector -> \n",
    "sel = CSSSelector('#content > div:nth-child(4) \\\n",
    "    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \\\n",
    "    > table > tbody > tr:nth-child(2) > td.name > a.title')\n",
    "# Apply the selector to the DOM tree.\n",
    "results = sel(html)"
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
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(results)"
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
      "비 오는 거리\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    #print lxml.html.tostring(item)\n",
    "    print item.text_content()"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "비 오는 거리\n",
      "비오는 날 수채화\n",
      "비 오는 날\n",
      "비오는거리\n",
      "비 오는 거리\n",
      "비오는 날 (Inst.)\n",
      "비오는날 (동요) (멜로디 MR)\n",
      "비오는 거리\n",
      "비오는 압구정\n",
      "One More Time\n",
      "비오는 밤에\n",
      "비 오는 거리  (Feat. 핫펠트)\n",
      "Yesterday (비틀즈 예스터 데이 : CF `시몬스침대`)\n",
      "비오는 남산\n",
      "비오는 오솔길\n"
     ]
    }
   ],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "\n",
    "html = lxml.html.fromstring(mydata)\n",
    "#tree=lxml.etree.parse('myhtml')\n",
    "# construct a CSS Selector -> \n",
    "sel = CSSSelector('#content > div:nth-child(4) \\\n",
    "    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \\\n",
    "    > table > tbody > tr > td.name > a.title')\n",
    "# Apply the selector to the DOM tree.\n",
    "results = sel(html)\n",
    "\n",
    "for item in results:\n",
    "    #print lxml.html.tostring(item)\n",
    "    print item.text_content()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "import requests\n",
    "\n",
    "keyword='비오는'\n",
    "r = requests.get(\"http://music.naver.com/search/search.nhn?query=\"+keyword+\"&x=0&y=0\")\n",
    "\n",
    "_html = lxml.html.fromstring(r.text)"
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
       "153208"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(lxml.html.tostring(_html))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(results)"
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
      "비 오는 거리\n",
      "비오는 날 수채화\n",
      "비 오는 날\n",
      "비오는거리\n",
      "비 오는 거리\n",
      "비오는 날 (Inst.)\n",
      "비오는날 (동요) (멜로디 MR)\n",
      "비오는 거리\n",
      "비오는 압구정\n",
      "One More Time\n",
      "비오는 밤에\n",
      "비 오는 거리  (Feat. 핫펠트)\n",
      "Yesterday (비틀즈 예스터 데이 : CF `시몬스침대`)\n",
      "비오는 남산\n",
      "비오는 오솔길\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    #print lxml.html.tostring(item)\n",
    "    print item.text_content()"
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
      "<tr class=\"_tracklist_move {TRACK_TYPE}\" style=\"display:none;\" trackdata=\"{TRACK_DATA}\">\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"chk\"><input type=\"checkbox\" title=\"&#49440;&#53469;\" class=\"_chkbox_item input_chk {TRACK_CHECK_NCLICKS}\"> </td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"order\">{TRACK_NUM}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"name\">\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{PLAY_TOGGLE}\r\n",
      "\t\t\t\t\t\t\t\t{ADD_TOGGLE}\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t<span class=\"_ico_title ico_title\"><img height=\"18\" width=\"23\" alt=\"TITLE\" src=\"http://static.naver.net/nmusic/201008/blank.gif\"></span>\r\n",
      "\t\t\t\t\t\t\t\t<span class=\"_ico_19 ico19\"><img height=\"18\" width=\"13\" src=\"http://static.naver.net/nmusic/201008/blank.gif\"></span>\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{TRACK_SONG_NAME}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t<td class=\"_artist artist {NO_ELL}\">\r\n",
      "\r\n",
      "\r\n",
      "                                   {ARTIST}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "                            <td class=\"album\">\r\n",
      "                                {ALBUM}\r\n",
      "                            </td>\r\n",
      "                        \r\n",
      "                        \r\n",
      "                        \t<td class=\"like\">\r\n",
      "\t\t\t\t\t\t\t\t<div class=\"u_likeit_list_module\">\r\n",
      "\t\t\t\t\t\t\t\t\t<a href=\"javascript:void(0)\" title=\"&#51339;&#50500;&#50836;\" class=\"u_likeit_list_btn u_type_img NPI=a:favo,r:1,i:\" data-sid=\"MUSIC\" data-did=\"MUSIC\" data-cid=\"TRACK_\" data-likeit=\"0\"><span class=\"u_ico\"></span><em class=\"u_txt\"></em><em class=\"u_cnt\"></em></a>\r\n",
      "\t\t\t\t\t\t\t\t</div>\r\n",
      "                        \t</td>\r\n",
      "                        \r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"video\">{MUSIC_VIDEO}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"lyric\">{LYRIC}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"get\">{SCRAP_ROW}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"radio\">{RADIO}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"buy\">\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{MP3_BUY_LAYER_BTN}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t<div style=\"display:none;\" class=\"_buy_layer buy_layer\">\r\n",
      "\t\t\t\t\t\t\t\t\t<ul>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{MP3_BUY_LIST}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{MUSIC_SPRING}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{BELL_SOUND}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{CONNECTION_SOUND}</li>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t\t</ul>\r\n",
      "\t\t\t\t\t\t\t\t\t<span class=\"bg\"></span>\r\n",
      "\t\t\t\t\t\t\t\t</div>\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t</tr>\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\t\n"
     ]
    }
   ],
   "source": [
    "from lxml.cssselect import CSSSelector\n",
    "\n",
    "sel = CSSSelector('table[summary] > tbody > ._tracklist_move')\n",
    "# Apply the selector to the DOM tree.\n",
    "results = sel(_html)\n",
    "print lxml.html.tostring(results[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_selName = CSSSelector('.name > a.title')\n",
    "_selArtist = CSSSelector('._artist.artist')\n",
    "_selAlbum= CSSSelector('.album > a')\n",
    "_name=_selName(results[1])\n",
    "_artist=_selArtist(results[1])\n",
    "_album=_selAlbum(results[1])"
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
      "비 오는 거리\n",
      "이승훈\n",
      "1집 비오는 거리\n"
     ]
    }
   ],
   "source": [
    "print _name[0].text_content()\n",
    "print _artist[0].text_content().strip()\n",
    "print _album[0].text_content()"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이승훈 --- 비 오는 거리 --- 1집 비오는 거리\n",
      "강인원 --- 비오는 날 수채화 --- 비오는 날 수채화 1 OST\n",
      "오소연 --- 비 오는 날 --- 비 오는 날\n",
      "유레이 --- 비오는거리 --- 비오는 거리\n",
      "소울스타 (SoulstaR) --- 비 오는 거리 --- 비 오는 거리\n",
      "김민우 --- 비오는 날 (Inst.) --- 비오는 날\n",
      "동요시대 --- 비오는날 (동요) (멜로디 MR) --- 동요 MR반주 5\n",
      "서영은 --- 비오는 거리 --- 1집 Romantic 1\n",
      "브라운 아이즈 --- 비오는 압구정 --- 2집 Reason 4 Breathing?\n",
      "Richard Marx --- One More Time --- 김현주의 비오는 거리\n",
      "루드 페이퍼(Rude Paper) --- 비오는 밤에 --- 1집 Paper Spectrum\n",
      "베이빌론(Babylon) --- 비 오는 거리  (Feat. 핫펠트) --- BETWEEN US\n",
      "Romantisch Jazzkapelle --- Yesterday (비틀즈 예스터 데이 : CF `시몬스침대`) --- 뉴에이지 연가 : 비 오는 날의 거리, 추억, 그리고 아름다운 재즈 피아노(Pop 올드 팝, 클래식, 영화 OST 베스트 연주 음악)\n",
      "조영순 --- 비오는 남산 --- 무진장 트롯트 골든 1＆2\n",
      "김겨울 --- 비오는 오솔길 --- 파랑새 창작동요 4집\n"
     ]
    }
   ],
   "source": [
    "_selName = CSSSelector('.name > a.title')\n",
    "_selArtist = CSSSelector('._artist.artist')\n",
    "_selAlbum= CSSSelector('.album > a')\n",
    "for item in results:\n",
    "    #print lxml.html.tostring(item)\n",
    "    _name=_selName(item)\n",
    "    _artist=_selArtist(item)\n",
    "    _album=_selAlbum(item)\n",
    "    if _name:\n",
    "        print _artist[0].text_content().strip(),\n",
    "        print \"---\",\n",
    "        print _name[0].text_content(),\n",
    "        print \"---\",\n",
    "        print _album[0].text_content()"
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
