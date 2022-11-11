''' Expérience de l'aiguille de Buffon
    https://fr.wikipedia.org/wiki/Aiguille_de_Buffon
    Sur un parquet composé de planches parallèles de largeur t, on lance des aiguilles de longueur l.
    Soit p la proportion d'aiguilles tombant à cheval sur deux planches,
    on a alors p ~ 2l/πt, soit π approximable par 2l/pt.
'''

import matplotlib.pyplot as plt
from math import cos, sin, pi
import random


def add_needle(t, l, x, y, th):
    """ t : largeur des planches
        l : longueur de l'aiguille
        x y : coordonées d'une extrémité
        th : extrémité de l'aiguille
    """
    x1 = x-l*sin(th)
    y1 = y-l*cos(th)
    if x//t != x1//t: # coupure
        if affichage :
            plt.plot([x, x1], [y, y1], 'r')
        return True
    else: # pas de coupure
        if affichage :
            plt.plot([x, x1], [y, y1], 'g')
        return False

npl = 15
ratio = 2 # ratio de la dimension d'affichage
t = 5 # largeur d'une planche
l = 4.5 # longeur d'une aiguille
N = 10**4

affichage = True
if N>10**3: affichage = False

longueur = npl*t
hauteur = longueur//ratio

if affichage :
    plt.plot([0, t, t, 0, 0], [0, 0, hauteur, hauteur, 0], 'r', label='coupure')
    plt.plot([0, t, t, 0, 0], [0, 0, hauteur, hauteur, 0], 'g', label='pas de coupure')
    plt.plot([0, longueur, longueur, 0, 0], [0, 0, hauteur, hauteur, 0], 'k')
    for k in range(npl):
        plt.plot([k*t, k*t], [0, hauteur], 'k')

results = 0
Lp = []
for i in range(N):
    x = random.uniform(t, longueur)
    y = random.uniform(l, hauteur-l)
    th = random.uniform(0, pi)
    b = add_needle(t, l, x, y, th)
    results += b
    if results!=0:
        Lp.append(2*l*i/(t*results))
    else:
        Lp.append(1)

p = results/N
print('%i/%i' %(results, N))
print('approximation de pi :', 2*l/(t*p))

if affichage :
    plt.axis('equal')
    plt.legend()

plt.figure(2)
plt.plot([i for i in range(N//100, N)], Lp[N//100:])
plt.title('Approximations successives de $\pi$')

plt.figure(3)
Lp2 = [abs(x-pi) for x in Lp]

# Lp2b = lisse_g(Lp2, 30)
# plt.semilogy([i for i in range(N//100, N)], Lp2b[N//100:], 'r', linewidth=2)
plt.semilogy([i for i in range(N//100, N)], Lp2[N//100:], 'b,', linewidth=.2)

plt.title('Erreur absolue avec $\pi$')
plt.show()