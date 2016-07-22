import requests
from BeautifulSoup import BeautifulSoup
url="http://www.cricbuzz.com/live-cricket-scores/16643/bt-vs-snp-14th-match-caribbean-premier-league-2016"
page=requests.get(url)
html=page.content
soup=BeautifulSoup(html)
#print soup
scores=soup.find('div',attrs={'class':'cb-col cb-col-67 cb-scrs-wrp'})
for r in scores.findAll('div'):
    print r.prettify()
