import urllib2
from BeautifulSoup import BeautifulSoup
url="http://www.cricbuzz.com/live-cricket-scores/16466/ire-vs-afg-2nd-odi-afghanistan-tour-of-ireland-2016"
page=urllib2.urlopen(url)
soup=BeautfulSoup(page)
print soup
