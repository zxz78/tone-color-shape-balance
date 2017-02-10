#coding=UTF-8
from BeautifulSoup import BeautifulSoup
import urllib
import re
import os

def read_web(alpha):
	_url = 'http://www.wikiart.org/en/alphabet/' + alpha
	return  urllib.urlopen(_url).read().decode('utf-8','ignore')

if __name__ == "__main__":
	#page = read_web()
	artists_list = []
	begin = ord('a')
	for i in range(1):
		print 'Loading Page ' + chr(begin + i)
		page = read_web(chr(begin + i))
		soup = BeautifulSoup(page)
		article=soup.findAll('article')
		cates = article[0].findAll('li')
		for item in cates:
			hrefs = item.findAll('a',{'title':re.compile('.*'),'href':re.compile('/en/.*')})
			if len(hrefs)==1:
				print len(hrefs[0].get('href'))
				artists_list.extend(hrefs[0].get('href'))
				artists_list.extend('\n')
			

	
	f = open('artists.txt','w')
	for artist in artists_list:
		f.write('%s' % artist)
		f.flush()
	f.close()