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

url_lists=[]
count=0
path = raw_input("Input the artist list(for example: vittore-carpaccio.lst)\n")
if os.path.exists('Artists-image-download-list/' + path):
	f=open('Artists-image-download-list/' + path)
	for l in f:
		l=l.strip()
		if not l:
			continue
		url_lists.append(l)
	f.close()
	artist=os.path.basename('Artists-image-download-list/' + path)[:-4]
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
			print 'Finish %s %d' % (_dirname, _count + 1)