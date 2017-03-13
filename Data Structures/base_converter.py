from stacks_using_list import Stack

def base_con(num,base):
    s=Stack()
    while(num>0):
        rem=num%base
        s.push(rem)
        num//=base
    
    strin=''
    while s.is_empty() is False:
        strin+=str(s.pop())
        
    print strin
    

base_con(26,26)
        
        
    
