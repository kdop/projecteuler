import math

ps = 0
sp = 0
for n in range(1, 101):
    ps += n
    sp += n ** 2
ps = ps ** 2

print("power of sum is ", ps)
print("sum of power is ", sp)
print("difference is ", ps - sp)
    
