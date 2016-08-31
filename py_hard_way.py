from sys import argv

script,file=argv
txt=open(file,'w')
print "we will empty the file"
txt.truncate()
line1=raw_input("enter in first line:")
line2=raw_input("second line:")
print "will be writing in file"
txt.write(line1+"\n"+line2)
txt.close
