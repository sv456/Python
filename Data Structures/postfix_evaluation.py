from stacks_using_list import Stack

def postfix_eval(expr):
    s=Stack()
    lst=expr.split()
    ran=range(1000)
    l=' '.join(str(i) for i in ran)
    for i in lst:
        if i in l:
            s.push(int(i))
        else:
            data2=s.pop()
            data1=s.pop()
            res=eval(data1,data2,i)
            s.push(res)

    return s.pop()


def eval(op1,op2,op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op == '==':
        if int(op1)==int(op2):
            return 1
        else:
            return 0

print postfix_eval('17 10 + 3 * 2 +')
