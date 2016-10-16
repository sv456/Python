import bs4,requests,webbrowser,sys

print 'Googling'
try:
    res=requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
except:
    print 'error'
else:
    soup=bs4.BeautifulSoup(res.text)
    elem=soup.select('.r a')
    numOpen=min(5,len(elem))
    for i in range(numOpen):
        webbrowser.open("https://google.com"+elem[i].get('href'))
