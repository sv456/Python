import platform as pl

profile=['processor','architecture','system','uname','linux_distribution','machine','platform']
for i in profile:
    if hasattr(pl,i):
        print i+":"+str(getattr(pl,i)())
