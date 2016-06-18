import urllib
def read_txt():
    file=open("C:\Users\I326017\Desktop\Mobile CR.txt")
    contents=file.read()
    #print contents
    file.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    #print output
    connection.close()
    if "true" in output:
        print "Profanity alert"
    elif "false" in output:
        print "This document does not contain curse words"
    else:
        print "document not scanned properly"

read_txt()
