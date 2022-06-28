""" z_{n+1} = log(z_n)
    Ça fait une sorte de spirale pentagonale ? """

from cmath import log, phase
import matplotlib.pyplot as plt
from scipy.special import lambertw

n = 10
X, Y = [], []

N = 123
for i in range(N):
    X.append(n.real)
    Y.append(n.imag)
    n = log(n)

plt.plot(X, Y)
z = -lambertw(-1).conjugate()
plt.plot(z.real, z.imag, 'o')

zf = X[-1]+1j*Y[-1]
L = [phase(x+y*1j-zf) for (x, y) in zip(X, Y)]
L2 = [L[i+1]-L[i] for i in range(N-1)]
plt.figure(2)
plt.plot(range(N-1), L2)
plt.show()

L3 = [i for i in range(N-1) if L2[i] > 0]
L4 = [L3[i+1]-L3[i] for i in range(len(L3)-1)]
print(L3)
print(L4)
