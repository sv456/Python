def create_stack():
    stack=list()
    return stack

def is_empty(lst):
    if len(lst)==0:
        return 0

def push(lst,data):
    lst.append(data)

def pop(lst):
    if is_empty(lst)==0:
        print 'stack is empty'
        return
    print lst.pop()

if __name__=='__main__':
    l=create_stack()
    push(l,2)
    push(l,3)
    push(l,4)
    push(l,5)
    pop(l)
    pop(l)
    pop(l)
    pop(l)
    pop(l)    
    
