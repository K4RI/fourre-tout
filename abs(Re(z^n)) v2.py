from math import sqrt, log, cos
from numpy import arctan

reals=[]
reals_appr=[]
imags=[]
coss=[]
iss=[]

theta=arctan(7**2)

z=complex(1,sqrt(7))/2
x=1

for i in range(650):
    reals.append(abs(x.real))
    # reals.append(x.real)
    imags.append(x.imag)
    if i%2==0:
        reals_appr.append(sqrt(2)**i)
    else:
        reals_appr.append((i*(2**-3/2))*sqrt(2)**i)
    coss.append(abs(cos(i*arctan(theta))))
    # print(x)
    iss.append(i)
    x=x*z

from matplotlib import pyplot as plt

for i in range(len(reals)-1):
    if reals[i+1]<reals[i]:
        print(i)

# plt.plot(iss, reals)
# plt.plot(iss, reals_appr)
# plt.plot(iss, coss)
plt.plot(reals, imags)
plt.show()

