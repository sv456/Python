from stacks_using_list import Stack

def parchecker(str_check):
    s=Stack()
    index=0
    balanced=True
    while index<len(str_check) and balanced:
        if str_check[index]=='(' or str_check[index]=='{' or str_check[index]=='[':
            s.push(str_check[index])
        else:
            if s.is_empty():
                balanced=False
            else:
                top=s.pop()
                if top=='(' and str_check[index]==')':
                    pass
                elif top=='[' and str_check[index]==']':
                    pass
                elif top=='{' and str_check[index]=='}':
                    pass
                else:
                    balanced=False
                

        index+=1
    if s.is_empty() is False:
        balanced=False
    if balanced:
        print 'entered string is balanced'

    else:
        print 'not balanced'

            
parchecker('[(())')
