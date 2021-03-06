from stacks_using_list import Stack

def postfix(expr):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['**']=4
    prec['+']=2
    prec['-']=2
    prec['(']=1
    ran=range(100)
    l=" ".join(str(i) for i in ran)
    token=expr.split()
    check=Stack()
    final_token=list()
    for char in token:
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or char in l:
            final_token.append(char)
        elif char=='(':
            check.push(char)

        elif char==')':
            data=check.pop()
            while data != '(':
                final_token.append(data)
                data=check.pop()

        else:
            while (not check.is_empty()) and (prec[check.peek()]>=prec[char]):
                data=check.pop()
                final_token.append(data)
            
            check.push(char)

    while not check.is_empty():
        final_token.append(check.pop())

    return " ".join(final_token)


print postfix('5 * 3 ** ( 4 - 2 )')
    
    
    
