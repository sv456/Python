from timeit import Timer

def test1():
    l=[]
    for i in range(2000):
        l+=[i]

def test2():
    l=[]
    for i in range(2000):
        l.append(i)

def test3():
    l=[i for i in range(2000)]

def test4():
    l=list(range(2000))

t1=Timer("test1()","from __main__ import test1")
print "concat",t1.timeit(number=1000),"milliseconds"

t2=Timer("test2()","from __main__ import test2")
print "append",t2.timeit(number=1000),"milliseconds"

t3=Timer("test3()","from __main__ import test3")
print "comrehension",t3.timeit(number=1000),"milliseconds"

t4=Timer("test4()","from __main__ import test4")
print "constructor",t4.timeit(number=1000),"milliseconds"
