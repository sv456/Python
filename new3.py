total = 0
cnt = 0
avg = 0

def calculate(d):
    global total
    total += d
    global cnt
    cnt+=1
    global avg
    avg=float(total)/cnt


def call():
    print 'total:', total, 'count:', cnt, 'average:', avg


while True:
    data = raw_input('enter the number')
    if data=='done':
        call()
        break
    else:
        try:
            data=int(data)
            calculate(data)
        except:
             print "Invalid input"
             continue
