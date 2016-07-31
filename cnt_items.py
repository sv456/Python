allguests={'Alice':{'Apples':5,'Cups':3},
      'Bob':{'Cups':2,'Oranges':6},
      'Cat':{'Lemons':3,'Apples':7}}
def cnt_items(guests,item):
    cnt=0
    for k,v in guests.items():
        cnt+=v.get(item,0)
    return cnt

print 'Apples- '+ str(cnt_items(allguests,'Apples'))
