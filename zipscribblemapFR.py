""" Relier toutes les communes de France
    par ordre de code postal
    https://eagereyes.org/zipscribble-maps/interactive-zipscribble-map """


import matplotlib.pyplot as plt
import numpy as np
import random as rd

with open('villes_utf8.csv', 'r') as f:
    data = f.readlines()

coords = []
for line in data:
    l = line.split(';')
    coords.append((int(l[8]), int(l[9]), int(l[2])))

coords.sort(key=lambda tup: tup[2])
coords = np.array(coords)
N = len(coords)

plt.figure(1)
plt.clf()


def randomColor(a=1.3):
    return (rd.random()/a, rd.random()/a, rd.random()/a)


def plot_villes():
    deps = [tup[2]//1000 for tup in coords]
    cuts = [0]

    for i in range(N-1):
        if deps[i] != deps[i+1]:
            cuts.append(i+1)
    cuts.append(N)

    for i in range(len(cuts)-1):
        interv = range(cuts[i], cuts[i+1])
        col = randomColor()
        plt.plot(coords[interv, 0], coords[interv, 1], linewidth=.1, color=col)


def afficher_carte(): # 48956 segments
    Xf, Yf = [], []
    with open('france_vect.txt', 'r') as f:
        liste_vects=f.readlines()
    for v in liste_vects[:-1]:
        coords=v.split()
        Xf.append(int(coords[0])*2373 + 55638)
        Yf.append((-int(coords[1])+500)*2373 + 6049647)
    plt.plot(Xf, Yf, color='black', linewidth=.2)

# afficher_carte()
plot_villes()

# plt.savefig('zipscribblemapFR.svg')
plt.savefig('zipscribblemapFR.jpg', dpi=1200)
plt.show()
