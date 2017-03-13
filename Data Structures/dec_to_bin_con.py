from stacks_using_list import Stack

def dec_to_bin(num):
    s=Stack()
    while(num>0):
        rem=num%2
        s.push(rem)
        num//=2
    
    strin=''
    while s.is_empty() is False:
        strin+=str(s.pop())
        
    print strin
    

dec_to_bin(233)
        
        
    
