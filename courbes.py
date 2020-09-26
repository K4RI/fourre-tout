import matplotlib.pyplot as plt 
from math import log, cos, sin, pi


plt.figure(1)

def f(n):
    return 1/log(n)**2

N=1000

plt.plot([0,1],[0,0],[0,0],[0,1], color='black')
for n in range(3,N):
    plt.plot([0,1-f(n)], [1-f(n), 0])


plt.axis('equal')


########################################


plt.figure(2)


def Lissajous(p,q, phi, theta):
    return (a*sin(p*theta), b*sin(q*theta + phi))


N2= 5000
p, q = 74829405, 94930395*2**0.5
# q>=p
a, b = 1, 1
phi = 0

X, Y = [], []
for i in range(N2):
    x, y = Lissajous(p,q, phi, i*2*pi/N2)
    X.append(x)
    Y.append(y)

plt.plot(X,Y)
plt.axis('equal')
plt.show()

# p=q -> ellipse
# a=2b p=1 q=2 -> besace
# p/q irrationnel -> courbe dense dans le rectangle
