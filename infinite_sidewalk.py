# Problème présenté sur le site Jane Street (https://www.janestreet.com/numberphile/) et découvert en outro d'une vidéo de Numberphile (https://youtu.be/rBU9E-ZOZAI)

# On a un trottoir infini aux cases indexées par 0,1,2... et labellées par 1,1,2,2,3,3... Depuis une case labellée k, on peut effectuer k pas vers l'avant ou vers l'arrière. En combien d'étapes atteint-on la case d'indice n ?

from math import log10
from sklearn.linear_model import LinearRegression
import networkx as nx



def first_steps(N, croise=True):
    ''' Simule toutes les possibilités de N pas, et consigne les cases visitées dans un graphe orienté. '''
    steps = dict() # clés = cases, valeurs = nombre de pas pour l'atteindre
    G = nx.DiGraph()
    steps[0]=0
    G.add_node(0, subset=0)
    steps[1]=1
    G.add_node(1, subset=1)
    G.add_edge(0, 1)
    to_check = [1] # les tous derniers ajoutés, à partir desquels faire les prochains pas
    Ln = [1, 1]
    for k in range(2, N+1): # pour tout entier k
        to_check_next = []
        for x in to_check: # pour chaque nombre de la colonne k-1
            d = x//2 + 1
            m, M = x-d, x+d # on regarde les cases atteignables
            if m not in steps.keys():
                if not croise:
                    steps[m]=k
                to_check_next.append(m)
                G.add_node(m, subset=k) # et on l'ajoute à la colonne k du graphe
                G.add_edge(x, m)
            if M not in steps.keys():
                if not croise:
                    steps[M]=k
                to_check_next.append(M)
                G.add_node(M, subset=k)
                G.add_edge(x, M)
        if croise:
            for m in to_check_next:
                    steps[m]=k
        Ln.append(len(to_check_next))
        to_check = to_check_next
    layout = nx.multipartite_layout(G)
    if N<=15:
        nx.draw(G, layout, node_size=300, with_labels=True, font_size=7) # , font_weight='bold'
    return steps, Ln

def effectifs(steps, Ln):
    ''' Pour tout n, combien de cases sont atteignables en exactement n étapes ? '''
    plt.figure(2)
    a=1.5
    col = (random()/a, random()/a, random()/a)
    X = [i for i in range(N+1)]
    plt.semilogy(X, Ln, '+', color=col, label="Effectif atteint à l'étape n", markersize=6)
    Xl = [[x] for x in X]
    Yl = [[log10(x)] for x in Ln]
    reg = LinearRegression().fit(Xl, Yl)
    Ypred = reg.predict(Xl)
    Y2 = [10**y[0] for y in Ypred]
    plt.semilogy(X, Y2, '-.', linewidth=1, color=col,
               label=f'{10**reg.intercept_[0] : .3f} * ({10**reg.coef_[0][0] : .3f})^n')
    print('%.3f * (%.3f)^n' % (10**reg.intercept_[0], 10**reg.coef_[0][0]))
    plt.legend()

def liste_steps(steps):
    ''' Affiche pour chaque case le nombre d'étapes pour l'atteindre. '''
    ns = list(steps.keys()) # à partir de notre liste steps...
    ns.sort()
    s = 0
    while ns[s]==s: # on trouve le plus grand s tel que tous les [|0;s-1|] aient été atteint
        s+=1 # (pour qu'il n'y ait pas de trou dans la figure suivante)
    X = [i for i in range(s)]
    Y = [steps[x] for x in X]
    plt.figure(3)
    plt.plot(X, Y, 'k+', label="Nombre d'étapes pour arriver jusqu'à n")
    plt.legend() # puis on affiche le nombre d'étapes pour les atteindre

_, _ = first_steps(15, croise=False)
N = 45
steps, Ln = first_steps(N, croise=False)
effectifs(steps, Ln)
liste_steps(steps)

# En ne faisant que des pas en avant, on obtient la suite définie par récurrence : M_{n+1} = 3*M_n//2 + 1
# M_n est encadré par les suites arithmético-géométriques [3/2 ; 1/2] et [3/2 ; 1]
# Donc 1+(3/2)^n <= M_n <= 2+2*(3/2)^n

# Empiriquement, il semblerait effectivement que M_n ∼ c*(3/2)^n avec c ≃ 1.612 :
def majorants_mask(N=1400):
    X = [i for i in range(N+1)]
    Y = [0]
    for _ in range(N):
        Y.append((3*Y[-1])//2 + 1)
    a=1.5
    col = (random()/a, random()/a, random()/a)
    plt.figure(4)
    Xl = [[x] for x in X[1:]]
    Yl = [[log10(x)] for x in Y[1:]]
    reg = LinearRegression().fit(Xl, Yl)
    Ypred = reg.predict(Xl)
    Y2 = [10**y[0] for y in Ypred]
    plt.semilogy(X[1:], Y2, '-.', linewidth=1, color=col,
               label=f'{10**reg.intercept_[0] : .3f} * ({10**reg.coef_[0][0] : .3f})^n')
    plt.semilogy(X, Y, '+', color=col, label = 'majorants', markersize=5)
    print('%.10f * (%.3f)^n' % (10**reg.intercept_[0], 10**reg.coef_[0][0]))
    plt.legend()

majorants_mask()

plt.show()
# Or puisque l'on cherche le n nécessaire pour attendre N, c'est plutôt à la réciproque qu'on s'intéresse.
# C*√log(N-2) <= e_N <= C*log(N-1), avec C = 1/log(3/2) ≃ 2.47
# et d'après la piste empirique, e_n ∼ C * ᶜ√log(N)