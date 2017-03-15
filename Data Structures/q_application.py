from queue import Queue

def hot_potato(namelist,num):
    s=Queue()
    for name in namelist:
        s.enqueue(name)
    while s.size()>1:
        for i in range(num):
            s.enqueue(s.dequeue())
        s.dequeue()

    return s.dequeue()

print hot_potato(['Sandesh','Meghana','Manish','Ananya'],2)
