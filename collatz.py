''' https://youtu.be/V3VAhulI8K8?t=89
    Temps de vol de la conjecture de Syracuse,
    tracés en semilogx, bleu pour les impairs et orange pour les pairs.
    Ça fait des bandes bien alignées hmmm bizarre
    '''

import matplotlib.pyplot as plt


def steps(n, t=0):
    if n<=0:
        return 0
    if n==1:
        return t
    elif n%2==0:
        return steps(n//2, t+1)
    else:
        return steps(3*n+1, t+1)

N = 10**5
X1 = [i for i in range(1, N, 2)]
X2 = [i for i in range(2, N, 2)]
Y1 = [steps(x) for x in X1]
Y2 = [steps(x) for x in X2]

plt.plot(X1, Y1, '.', markersize=2)
plt.plot(X2, Y2, '.', markersize=2)
plt.show()
