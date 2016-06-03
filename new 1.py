data=raw_input('enter hours:')
try:
    hrs=int(data)
except:
    print 'please enter number'
    


data=raw_input('enter rate:')
if isinstance(data,float):
    rate=data
else:
    print 'enter properly'
    exit()
if hrs<=40:
    print 'pay:',hrs*rate
else:
    print 'pay:',1.5*hrs*rate