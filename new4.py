num=list()
while(True):
    inp=raw_input('enter a number')
    if inp=='done':break
    val=int(inp)
    num.append(val)

max=max(num)
min=min(num)
print "max: ",max ,"min: ",min