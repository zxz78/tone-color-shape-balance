#coding=UTF-8
import urllib
import sys
import os
import threading
import time
import pdb
import sys
import signal
import sys
from BeautifulSoup import BeautifulSoup
import urllib
import re
reload(sys) 
sys.setdefaultencoding('utf-8')


url_lists=[]
count=0

#get the single image url for a specific artist

def get_image_url(allimage_path_file):
	f=open(allimage_path_file)
	suffix_list=[]
	for l in f:
		l=l.strip()
		if not l:
			continue
		index_head = l.find('images')
		index_tail = l.find('(')
		if index_tail==-1:
			index_tail=l.find('.jpg')
		suffix=l[index_head+7:index_tail]
		print type(suffix)
		print suffix
		suffix_list.append(suffix)
	f.close()
	artist=os.path.basename(allimage_path_file)[:-4]
	suffix_file='suffix_list/%s.txt' % artist
	f=open(suffix_file,'w')
	for i in range(len(suffix_list)):
		f.write(suffix_list[i])
		f.write('\n')
	f.close()
	image_page_file = 'image_page_file/%s.txt' % artist
	f=open(image_page_file,'w')
	for i in range(len(suffix_list)):
		f.write('https://www.wikiart.org/en/'+suffix_list[i])
		f.write('\n')
	f.close()
	return suffix_list

def get_details(image_page_file,path):
	f=open(image_page_file)
	image_list=[]
	for l in f:
		l=l.strip()
		if not l:
			continue
		image_list.append('http://www.wikiart.org'+l)
	f.close()
	detail_list = []
	f=open('/Volumes/test/detail/%s.txt' % path,'w')
	for i in range(len(image_list)):
		print 'loading image %s:' % image_list[i]
		page= urllib.urlopen(image_list[i]).read().decode('utf-8','ignore')
		soup = BeautifulSoup(page)
		#url = soup.find(attrs={"property":"og:url"})['content']
		#detail=url+'$$'
		#title = soup.find(attrs={"property":"og:title"})['content']
		#detail=title+'$$'
		#image_type = soup.find(attrs={"property":"og:type"})['content']
		#detail=detail+image_type+'$$'
		#image = soup.find(attrs={"property":"og:image"})['content']
		#detail=detail+image+'$$'
		description = soup.find(attrs={"property":"og:description"})['content']
		detail=description+'$$'
		image_width = soup.find(attrs={"property":"og:image:width"})['content']
		detail=detail+image_width+'$$'
		image_height = soup.find(attrs={"property":"og:image:height"})['content']
		detail=detail+image_height+'$$'
		
		f.write(detail)
		f.write('\n')
		f.flush()
		detail_list.append(detail)
	f.close()
		



		






'''if os.path.exists(allimage_path_file):
	f=open('lists/' + path)
	for l in f:
		l=l.strip()
		if not l:
			continue
		url_lists.append(l)
	f.close()
	artist=os.path.basename('lists/' + path)[:-4]
	_dirname = '/Volumes/test/Images/%s' % artist
	if not os.path.exists(_dirname):
		os.makedirs(_dirname)

	while count < len(url_lists):
		_url = url_lists[count]
		_count = count
		count += 1
		filename=_url[_url.rfind('/'):]
		_path = (_dirname + filename)
		exists = os.path.exists(_path)
		if not exists:
			print "Downloading %s %d" % (_dirname, _count + 1)
			urllib.urlretrieve(_url,_path)
			print 'Finish %s %d' % (_dirname, _count + 1)'''






if __name__ == '__main__':
	path = raw_input("Input the artist list(for example: vittore-carpaccio.lst)\n")
	#allimage_path_file = 'lists/' + path
	#allimage_page_file = get_image_url(allimage_path_file)
	get_details('Artists-image-main-list/'+path[:-4]+'.txt',path[:-4])

'''a='http://uploads2.wikipaintings.org/images/vincent-van-gogh/a-girl-in-a-wood-1882.jpg'
index_head = a.find('images')
index_tail = a.find('(')
if index_tail==-1:
	index_tail=a.find('.jpg')
suffix=a[index_head+7:index_tail]
print suffix'''



