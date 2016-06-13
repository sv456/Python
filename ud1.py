import webbrowser
import time
n=1

while n<=3:
    time.sleep(6)
    print "this program started on ",time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=Jx2yQejrrUE")
    n+=1
