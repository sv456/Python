def collatz(num):
    try:
        num=int(num)
        if num%2==0:
           return num//2
        else:
           return 3*num+1
    except ValueError:
           print 'entered value is not integer'

n=raw_input('enter a value:')
print collatz(n)
           
       
