''' Pour tout entier naturel k non-nul, σ(k) est la somme des diviseurs de k.
    https://fr.wikipedia.org/wiki/Fonction_somme_des_diviseurs
    On calcule la somme des σ(k) pour k allant de 1 à n,
    somme équivalente à (π²/12) * n².
'''

import matplotlib.pyplot as plt
from math import pi, log10

def sdiv(n): # O(n) modulos
    s = 0
    for i in range(1, n+1):
        if n%i==0:
            s+=i
    return s

def lisse_a(L,n): # O(len(L)) divisions
    somp=sum(L[:n+1])
    L2 = []
    for i in range(n):
        L2.append(somp/(n+1+i))
        somp+=L[n+i+1]
    for i in range(n, len(L)-n-1):
        L2.append(somp/(2*n+1))
        somp+=(L[i+n+1]-L[i-n]) # marche jusqu'à i=len(L)-1-n
    for i in range(n+1):
        L2.append(somp/(2*n+1-i))
        somp-=L[-(2*n+1-i)]
    return L2

def prod(L):
    if len(L)==1:
        return L[0]
    return L[0]*prod(L[1:])

def lisse_g(L,n): # O(len(L)) puissances
    somp=prod(L[:n+1])
    L2 = []
    for i in range(n):
        L2.append(somp**(1/(n+1+i)))
        somp*=L[n+i+1]
    for i in range(n, len(L)-n-1):
        L2.append(somp**(1/(2*n+1)))
        somp*=(L[i+n+1]/L[i-n]) # marche jusqu'à i=len(L)-1-n
    for i in range(n+1):
        L2.append(somp**(1/(2*n+1-i)))
        somp/=L[-(2*n+1-i)]
    return L2



x = pi**2/12
def ssdiv(N):
    s = 0
    Y = []
    for i in range(1,N+1): # O(N²) modulos
        s+=sdiv(i)
        Y.append(s)
    X = [i for i in range(1,N+1)]

    Y2 = [abs(Y[i-1]/i**2 - x) for i in range(1, N+1)] # O(N) divisions
    plt.plot(X, Y2, 'b,', linewidth=.2, label = r'$\epsilon_n = \frac{\pi^2}{12} - \frac{1}{n^2} \sum_{k=1}^n \sigma(k)$')

    Y3 = lisse_g(Y2, 30) # O(N) puissances
    plt.semilogy(X, Y3, 'r', linewidth=.5, label = '$O(10^{-log(n)}) = O(1/n)$')
    plt.legend()

    # Y = lisse_a(Y, 100)
    # print(len(Y))
    # Y2 = [abs(Y[i-1]/i**2 - x) for i in range(1, n+1)]
    # plt.semilogy(X, Y2, 'r', linewidth=.5)
    plt.show()

ssdiv(10**4)