#coding=UTF-8
from BeautifulSoup import BeautifulSoup
import urllib
import re
import os

heda_url= "http://www.the-athenaeum.org/art/list.php?m=a&s=tu&aid=1886"
page = urllib.urlopen(heda_url).read().decode('utf-8','ignore')
soup=BeautifulSoup(page)
print soup.prettify