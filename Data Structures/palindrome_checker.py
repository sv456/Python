from dequeue import Dequeue

def palin_check(string):
    d=Dequeue()
    for ch in string:
        d.addRear(ch)

    equals=True
    while d.size()>1 and equals:
        if d.removeFront() is d.removeRear():
            pass
        else:
            equals=False

    return equals

print palin_check('adama')
        
        
    
