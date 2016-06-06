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
def cal_pay(h,r):
    if h<=40:
         print 'pay:',h*r
    else:
        print 'pay:',1.5*h*r

cal_pay(hrs,rate)