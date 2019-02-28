import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import os
import json
import sys
import ctypes
import time


def getFullPathOfImage(imageFilename):
    return os.path.dirname(os.path.realpath("one_plus_stored_backgrounds/" + imageFilename)) + "\\" + imageFilename

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://photos.oneplus.com/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
imageList = []
for tag in tags:
    line = tag.get('href', None)
    if(re.search('\S+.jpg',line)):
        imageList.append(line)

if not os.path.exists("one_plus_stored_backgrounds"):
    os.makedirs("one_plus_stored_backgrounds")

imageSuffix = int(round(time.time() * 1000))
imageFilename = "bg_" + str(imageSuffix) + ".jpg"
print(imageFilename)
open("one_plus_stored_backgrounds/" + imageFilename, "wb").write(urllib.request.urlopen(imageList[0]).read())

ctypes.windll.user32.SystemParametersInfoW(20, 0, getFullPathOfImage(imageFilename) , 0)
