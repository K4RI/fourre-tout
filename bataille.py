#coder un bail qui calcule le temps moyen d'une partie de bataille
# http://www.lifl.fr/%7Ejdelahay/pls/1995/030.pdf
from random import shuffle
from math import log,log10
from matplotlib import pyplot as plt
from statistics import median


def coup(L, paquet1, paquet2):
    L.append(paquet1[0])
    L.append(paquet2[0])
    p1=paquet1[0]
    p2=paquet2[0]
    del paquet1[0]
    del paquet2[0]
    if p1==p2 and len(paquet1)>0 and len(paquet2)>0:
        L.append(paquet1[0])
        L.append(paquet2[0])
        del paquet1[0]
        del paquet2[0]
        if len(paquet1)>0 and len(paquet2)>0:
            coup(L, paquet1, paquet2)
    elif p1>p2:
        paquet1.extend(L)
        del L[:]
    else:
        paquet2.extend(L)
        del L[:]




def jeu(N_cartes): #TODO nooooon il faut un paquet qu'on divise en deeeeeeux >>>>>:( 08/01/20
    paquet1 = 4*[i for i in range(1,N_cartes+1)]
    paquet2 = 4*[i for i in range(1,N_cartes+1)]
    shuffle(paquet1)
    shuffle(paquet2)
    L=[]
    tour=0
    while len(paquet1)>0 and len(paquet2)>0 and tour<tourmax:
        coup(L, paquet1, paquet2)
        tour+=1
    return tour

def mean(L):
    return sum(L)/len(L)


tourmax=10**5

## HISTOGRAMME POUR N_CARTES FIXE
N_jeux=5000

Lt=[]
explose=0
explosel=[]

N_cartes=5

for i in range(N_jeux):
    tour=jeu(N_cartes)
    if tour<tourmax:
        Lt.append(log10(tour))
    # else:
        # explosel.append(i)
        # explose+=1
    if i%100==0:
        print(i)



Lt.sort()
# print(Lt)
print(mean(Lt))
print(min(Lt))
print(max(Lt))
print(explose, explosel, N_jeux)

plt.hist(Lt, bins = 75, color = 'pink', edgecolor = 'green')
plt.show()

## NBRE MOYEN DE TOURS EN FCT DE N_CARTES

L_moys=[]
N_jeux=500

nmin,nmax = 3, 9

for N_cartes in range(nmin,nmax+1):
    Lt=[]
    explose=0
    for i in range(N_jeux):
        tour=jeu(N_cartes)
        if tour<tourmax:
            Lt.append(tour)
        else:
            explose+=1
    Lt.sort()
    print(N_cartes,Lt, explose, '\n')
    L_moys.append(median(Lt))

plt.plot(range(nmin,nmax+1), L_moys)
plt.show()
# numpy.polyfit(range(nmin,nmax+1), L_moys, ???)  approx polynomiale

