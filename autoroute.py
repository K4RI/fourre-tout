## coder un programme qui simule des autoroutes 
# en supposant que le joueur fait dise "plus haut" en-dessous de la valeur médiane, et "plus bas" au-dessus
# selon la longueur de l'autoroute, combien de gorgées boira-t-il ?

from random import shuffle, choice
from statistics import median, mean
from numpy import quantile, arange
from matplotlib import pyplot as plt
from math import log

def jeu(Nc, difficulte):
    paquet = 4*[i for i in range(1,Nc+1)]
    shuffle(paquet)
    L = paquet[:difficulte]
    paquet = paquet[difficulte:]
    b_jeu = True #on continue la partie
    while b_jeu:
        i=0
        pts=0
        while i<difficulte:
            if len(paquet)==0: # si le paquet est vide on reprend les cartes en-dessous et on mélange
                paquet = 4*[i for i in range(1,Nc+1)]
                for x in L:
                    paquet.remove(x)
                shuffle(paquet)
            attente=L[i] #la carte à comparer
            # print('\n', pts, 'points', L, attente)
            if attente==(Nc+1)/2:
                choix=choice(['plus','moins'])
            elif attente>Nc/2:
                choix='moins'
            else:
                choix='plus'
            pioche = paquet[0] #carte piochée
            del paquet[0]

            # print(choix, pioche)

            if (pioche>attente and choix=='plus') or (pioche<attente and choix=='moins'):
                L[i]=pioche
                i+=1
                # print('ui',i)
            elif pioche==attente:
                L[i]=pioche
                pts+=2*(i+1)
                i=0
                # print('ARGH')
            else:
                L[i]=pioche
                pts+=(i+1)
                i=0
                # print('nn', 0)
            # # # # # # # # # # # # # # # # # # if len(paquet)==0
        return pts #nbre de gorgées bues au total

def jeu_peage(Nc, difficulte): ########### OUAI S'OCCUPER DE CA ######################
    i_cach=Nc//2+1
    cache=True
    paquet = 4*[i for i in range(1,Nc+1)]
    shuffle(paquet)
    L = paquet[:difficulte]
    paquet = paquet[difficulte:]
    b_jeu = True #on continue la partie
    while b_jeu:
        b_tour=True #on avance dans le tour
        i=0
        pts=0
        while i<difficulte:
            if len(paquet)==0:
                paquet = 4*[i for i in range(1,Nc+1)]
                for x in L:
                    paquet.remove(x)
                shuffle(paquet)
            attente=L[i] #la carte à comparer
            # print('\n', pts, 'points', L, attente)
            if attente==(Nc+1)/2:
                choix=choice(['plus','moins'])
            elif attente>Nc/2:
                choix='moins'
            else:
                choix='plus'
            pioche = paquet[0] #carte piochée
            del paquet[0]

            # print(choix, pioche)

            if (pioche>attente and choix=='plus') or (pioche<attente and choix=='moins'):
                L[i]=pioche
                i+=1
                # print('ui',i)
            elif pioche==attente:
                L[i]=pioche
                pts+=2*(i+1)
                i=0
                # print('ARGH')
            else:
                L[i]=pioche
                pts+=(i+1)
                i=0
                # print('nn', 0)
            # # # # # # # # # # # # # # # # # # if len(paquet)==0
        if i==difficulte:
            return pts #nbre de pts et si on a vidé le paquet


## # # # # # # # # # # # # # # # # # # # PARTIE I : difficulté fixe (histogrammes)

# sur N tests pour des longueurs de nmin à nmax, la fréquence de boisson (ordonnée) de tel nombre de gorgées (abscisse)


N_jeux=1000 # nbre de tests
Nc=13 # 4 familles de valeurs 1 à Nc

plt.clf()
plt.figure(1)

nmin,nmax = 1, 9

for difficulte in range(nmin,nmax+1):

    Lt=[]

    for i in range(N_jeux):
        pts = jeu(Nc, difficulte)
        Lt.append(pts)
        if i%(N_jeux//10)==0:
            print(i)

    Lt.sort()

    # print(Lt)
    print('\n\nNombre 2 jeux :', N_jeux)
    n=len(Lt)

    from collections import Counter
    z=Counter(Lt)
    for j in range(20):
        print(j, ':', 100*z[j]/len(Lt), '%')

    print('---------------------')
    print('min :', min(Lt))
    print('1er quartile :', quantile(Lt, 1/4))
    print('MEDIANE :', median(Lt))
    print('MOYENNE :', mean(Lt))
    print('3ème quartile :', quantile(Lt, 3/4))
    print('max :', max(Lt))

    Lred=Lt[:7*n//8]
    interv=arange(Lred[0]-0.5, Lred[-1]+0.5, 1)
    plt.subplot(330+difficulte)
    plt.hist(Lred, interv, color = 'pink', edgecolor = 'green')
    plt.title('Taille = ' + str(difficulte))

plt.tight_layout()

## # # # # # # # # # # # # # # # # # # # PARTIE II : difficulté variable (courbes)

# sur N tests pour des longueurs de nmin à nmax, les indicateurs statistiques sur le nombre de gorgées bues


N_jeux=1000
Nc=13 # 4 familles de valeurs 1 à Nc

plt.figure(2)

nmin,nmax = 1, 9

L_Q1=[]
L_med=[]
L_moys=[]
L_Q3=[]
L_zeros=[]

for difficulte in range(nmin,nmax+1):
    Lt=[]
    explose=0
    for i in range(N_jeux):
        pts = jeu(Nc, difficulte)
        Lt.append(pts)
    Lt.sort()
    print(difficulte) #, Lt, explose, '\n')
    L_Q1.append(quantile(Lt, 1/4))
    L_med.append(median(Lt))
    L_moys.append(mean(Lt))
    L_Q3.append(quantile(Lt, 3/4))
    L_zeros.append(100*Lt.count(0)/len(Lt))
    # # L_Q1.append(log(quantile(Lt, 1/4)))
    # L_med.append(log(median(Lt)))
    # L_moys.append(log(mean(Lt)))
    # L_Q3.append(log(quantile(Lt, 3/4)))
    # # L_zeros.append(100*Lt.count(0)/len(Lt))

plt.plot(range(nmin,nmax+1), L_Q1)
plt.plot(range(nmin,nmax+1), L_med)
plt.plot(range(nmin,nmax+1), L_moys)
plt.plot(range(nmin,nmax+1), L_Q3)
plt.plot(range(nmin,nmax+1), L_zeros)
plt.legend(['1er quartile', 'médiane', 'moyenne', '3ème quartile', 'proportion de zéros'],loc='best')
plt.xlabel("Taille de l'autoroute")
plt.ylabel("Nombre de gorgées")

plt.show()
