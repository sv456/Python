def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory
        
def displayInventory(inven):
    cnt=0
    print 'Inventory:'
    for k,v in inven.items():
        print str(v) + ' '+k
        cnt+=v
    print "total items:",cnt

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
#print inv
displayInventory(inv)
