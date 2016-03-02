__author__ = 'gkannappan'


#import requests


import urllib
import urllib2

from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
user_agent_mac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
headers = { 'User-Agent' : 'Mozilla/5.0' }

#URL = 'http://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python'
URL = 'http://www.ichangemycity.com/bangalore/complaints'


req = urllib2.Request(URL, None, headers)
#response = urllib2.urlopen(URL)

#html = response.read
html = urllib2.urlopen(req).read()

#print html

soup = BeautifulSoup(html, 'html.parser')

#f = requests.get(URL)

print(soup.prettify())
