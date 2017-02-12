#coding = utf-8
from BeautifulSoup import BeautifulSoup
import urllib
import re
import os
import threading
import time
import pdb
import sys
import json

reload(sys) 
sys.setdefaultencoding('utf-8')

def read_web(suffix, pagenumber):
	_url = 'http://www.wikiart.org' + suffix + '/mode/all-paintings?json=2&page=%s' % pagenumber
	return  urllib.urlopen(_url)

def parse_web(suffix,artist):
	count=1
	f1=open('Artists-image-main-list/'+artist+'.txt','w')
	f2=open('Artists-image-download-list/'+artist+'.txt','w')
	while True:
		web=read_web(suffix,count)
		dic=json.load(web)
		painting_list= dic['Paintings']
		if painting_list==None:
			break
		else:
			for i in range(len(painting_list)):
				image_download_url=painting_list[i]['image']
				image_main_url=painting_list[i]['paintingUrl']
				f2.write(image_download_url)
				f2.write('\n')
				f2.flush()
				f1.write(image_main_url)
				f1.write('\n')
				f1.flush()
			count=count+1

			
	

#hrefs = item.findAll('a',{'title':re.compile('.*'),'href':re.compile('/en/.*')})

def get_image_list(lines):
	#for i in range(len(lines)):
	for i in range(len(lines)):
		suffix=lines[i]
		artist=lines[i][4:]
		parse_web(suffix,artist)
		print 'finished getting the painting list of %s\n' % artist




if __name__=="__main__":
	if not os.path.exists('Artists-image-main-list'):
		os.mkdir('Artists-image-main-list')
	if not os.path.exists('Artists-image-download-list'):
		os.mkdir('Artists-image-download-list')
	lines = []
	f=open('artists.txt')
	for l in f:
		l=l.strip()
		if not l:
			continue
		lines.append(l)
	get_image_list(lines)
