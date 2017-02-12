#coding=utf-8 
from PIL import Image
import os

path = "/Volumes/test/Images/michelangelo"
files=os.listdir(path)
s=[]
count=1
for file in files:
	img = Image.open("/Volumes/test/Images/michelangelo/"+file)
	dir=file[:-4]
	img.save("/Volumes/test/ImagesPPM/michelangelo/"+dir+".ppm")
	print count
	count=count+1