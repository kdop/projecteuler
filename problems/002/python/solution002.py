s = 0
fibcurr = 1
fibprev = 0
tmp = 0

while fibcurr < 4000000:
    if fibcurr % 2 == 0:
        s += fibcurr
        print(fibcurr, "added")
    else:
        print(fibcurr)
        
    tmp = fibcurr
    fibcurr += fibprev
    fibprev = tmp

print("\nanswer = ", s)
