import requests,bs4

try:
    res=requests.get("https://automatetheboringstuff.com/chapter11/")
    res.raise_for_status()
except Exception as exce:
    print "error is %r" %exce
else:
    print "download successful"
    print res
    bs=bs4.BeautifulSoup(res.text,"lxml")
    pelement=bs.select('p')
    print len(pelement)
    print pelement[1].getText()
    
        

