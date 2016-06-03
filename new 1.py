data=raw_input('enter hours:')
try:
    hrs=int(data)
except:
    print 'please enter number'
    exit()

data=raw_input('enter rate:')
try:
    rate=float(data)
except:
    print 'enter properly'
    exit()

if hrs<=40:
    print 'pay:',hrs*rate
else:
    print 'pay:',1.5*hrs*rate