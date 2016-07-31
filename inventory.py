inventory={'arrow':12,'gold coins':42,'rope':1,'torch':6,'dagger':1}
def displayInventory(inven):
    cnt=0
    print 'Inventory:'
    for k,v in inven.items():
        print str(v) + ' '+k
        cnt+=v
    return cnt

print 'total items:'+str(displayInventory(inventory))
        
