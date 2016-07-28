bday={'Megha':'20 oct','Amma':'15 Jul','Dad':'31 Nov'}
while True:
    name=raw_input('enter the name for their b\'day and if not leave blank:')
    if name=='':
        break
    else:
        if name in bday:
            print name+'\'s bday is on '+bday[name]
        else:
            print 'info not present'
            day=raw_input('enter their bday:')
            bday[name]=day
            print 'db updated'
                   
