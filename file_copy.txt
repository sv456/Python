from sys import argv
from os.path import exists

script,from_file,to_file=argv
print "contents of %r will be copied to %r" %(from_file,to_file)
print "out file exists : %s" % exists(to_file)
print "ctrl-c to exit , enter to continue"
raw_input()
txt=open(from_file)
data=txt.read()
print "data to be transferred is %d bytes long" %len(data)
txt1=open(to_file,'w')
txt1.write(data)
print "copy done"
txt.close()
txt1.close()
