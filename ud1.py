import webbrowser
import time
n=1
print "this program started on ",time.ctime()
while n<=3:
    time.sleep(6)
    webbrowser.open("https://www.youtube.com/watch?v=Jx2yQejrrUE")
    n+=1
