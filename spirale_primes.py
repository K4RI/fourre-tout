import matplotlib.pyplot as plt 
from math import sin, cos

def isprime(u):
    if u in (0,1):
        return False
    if u==2:
        return True
    for i in ((2,)+tuple(range(3,int(u**0.5)+1,2))):
        if u%i==0:
            return False
    return True

N=int(2e5)
for i in range(N):
    if isprime(i):
        plt.plot(i*cos(i), i*sin(i), 'r,')

plt.show()
