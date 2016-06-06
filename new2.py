v=raw_input('enter nuber between 0.0 to 1.0\n')
try:
    v = float(v)
except:
    print 'not correct'
    exit()
def func(var):
        if var<0.0 or var>1.0:
             print 'error'
        else:
            if var>=0.9:
                print 'A'
            elif var>=0.8 and var<0.9:
                print 'B'
            elif var>=0.7 and var<0.8:
                print 'C'
            elif var>=0.6 and var<0.7:
                 print 'D'
            else:
                print 'F'

func(v)