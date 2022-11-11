# Problème présenté dans la planche n°135 de la série de webcomics 'xkcd'. (https://xkcd.com/135/)

# Vous êtes au centre d'un triangle équilatéral de 20 mètres de côté, avec un raptor dans chaque coin. Ils ont une accélération de 4m/s² et une vitesse maximale de 25m/s, sauf celui du haut ayant une vitesse maximale de 10m/s. Vous avez une vitesse constante de 6m/s. Les raptors vont courir dans votre direction. Vers quel angle courir pour maximiser son temps de survie ?

# Des solutions proposées ici :
# https://www.youtube.com/watch?v=NYjPPj2pi-A
# https://www.youtube.com/watch?v=be6JYkT312o

from math import sqrt, cos, sin, pi, radians
import matplotlib.pyplot as plt


triangle = 20
ar = 4
vm1, vm2, vm3 = 25, 25, 10
v0 = 6

def survie(theta, seuil = .5):
    theta = radians(theta)

    x0, y0 = 0, 0
    # Par le théorème d'Al-Kashi, les trois raptors sont à distance 20/√3 ≃ 11.547 mètres.
    r = triangle/sqrt(3)
    x1, y1 = r*sqrt(3)/2, -r/2
    x2, y2 = -r*sqrt(3)/2, -r/2
    x3, y3 = 0, r
    x0l, y0l, x1l, y1l, x2l, y2l, x3l, y3l = [x0], [y0], [x1], [y1], [x2], [y2], [x3], [y3]
    v1, v2, v3 = 0, 0, 0

    t = 0
    tl = [t]
    d1, d2, d3 = r, r, r
    dt = 1e-3

    while min(min(d1, d2), d3) > seuil: #v0*dt :
        # chaque raptor i court vers l'humain à la vitesse v_i
        # alors que l'humain fonce en ligne droite
        t+=dt
        v1 = min(vm1, ar*t)
        v2 = min(vm2, ar*t)
        v3 = min(vm3, ar*t)

        x0, y0 = v0*cos(theta)*t, v0*sin(theta)*t

        d1 = sqrt((x1-x0)**2 + (y1-y0)**2)
        x1 += v1*(x0-x1)/d1 * dt
        y1 += v1*(y0-y1)/d1 * dt

        d2 = sqrt((x2-x0)**2 + (y2-y0)**2)
        x2 += v2*(x0-x2)/d2 * dt
        y2 += v2*(y0-y2)/d2 * dt

        d3 = sqrt((x3-x0)**2 + (y3-y0)**2)
        x3 += v3*(x0-x3)/d3 * dt
        y3 += v3*(y0-y3)/d3 * dt

        tl.append(t)
        x0l.append(x0)
        y0l.append(y0)
        x1l.append(x1)
        y1l.append(y1)
        x2l.append(x2)
        y2l.append(y2)
        x3l.append(x3)
        y3l.append(y3)

    if d1 < min(d2, d3):
        ind = 1
    elif d2<d3:
        ind = 2
    else:
        ind = 3

    return t, ind, x0l, y0l, x1l, y1l, x2l, y2l, x3l, y3l


def plot_survie(theta=60):
    ''' Affiche le scénario d'une course d'angle θ. '''
    t, _, x0l, y0l, x1l, y1l, x2l, y2l, x3l, y3l = survie(theta)
    plt.plot([x1l[0], x2l[0], x3l[0], x1l[0]], [y1l[0], y2l[0], y3l[0], y1l[0]], 'k-')
    plt.plot(x0l, y0l, 'b', label='humain ($t_{survie}=$%.2f s)' %t)
    plt.plot(x1l, y1l, 'r', label='raptor bas-droite')
    plt.plot(x2l, y2l, 'm', label='raptor bas-gauche')
    plt.plot(x3l, y3l, 'y', label='raptor haut')
    plt.title('Fuite à θ=%i°' %theta)
    plt.axis('equal')
    plt.legend()
    plt.show()


def optima_locaux(T):
    mins, maxs = [], []
    n = len(T)
    for i in range(1, n-1):
        if T[i-1]>T[i]<=T[i+1]:
            mins.append(i)
        if T[i-1]<T[i]>=T[i+1]:
            maxs.append(i)
    return mins, maxs


def plot_360():
    ''' Affiche les zones atteignables par l'humain selon son angle de course.
        La couleur du trait correspond au raptor l'ayant attrapé.

        Dans un second temps, affiche le temps de survie en fonction
        de l'angle de course, avec les optima locaux. '''
    TH = [th for th in range(360)]
    T, X, Y, I = [], [], [], []
    for th in TH:
        if th%10==0: print(th)
        t, ind, x0l, y0l = survie(th)[:4]
        T.append(t)
        X.append(x0l[-1])
        Y.append(y0l[-1])

        if ind==1:
            plt.plot(x0l, y0l, 'r')
        elif ind==2:
            plt.plot(x0l, y0l, 'm')
        else:
            plt.plot(x0l, y0l, 'y')
        I.append(ind)
    # plt.plot(X,Y)
    x0l, y0l, x1l, y1l, x2l, y2l, x3l, y3l = survie(0)[2:]
    plt.plot([x1l[0], x2l[0], x3l[0], x1l[0]], [y1l[0], y2l[0], y3l[0], y1l[0]], 'k-')

    plt.figure(2)
    plt.plot(TH, T, label = 'Temps de survie')
    mins, maxs = optima_locaux(T)
    rouges_x, rouges_y = [TH[m] for m in mins], [T[m] for m in mins]
    verts_x, verts_y = [TH[m] for m in maxs], [T[m] for m in maxs]
    plt.plot(rouges_x, rouges_y, 'ro', label='minima locaux %s' %str(rouges_x))
    plt.plot(verts_x, verts_y, 'go', label='maxima locaux %s' %str(verts_x))

    plt.xlabel('angle de course')
    plt.legend()
    plt.show()


plot_survie(30)
plot_survie(90)
plot_survie(150)
plot_survie(210)
plot_survie(270)
plot_survie(330)

plot_360()