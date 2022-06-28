""" Approxime l'aire sous une courbe / dans un cercle
    en intégrant par méthode de Monte-Carlo
    https://www.facebook.com/groups/983623345353229/posts/1539201199795438/?comment_id=1539339899781568 """

import matplotlib.pyplot as plt
import numpy as np
import random as rd

##

X=np.linspace(0,1,1000)
Y=X**2
plt.plot(X,Y)

u=.1
plt.axis("EQUAL")
plt.xlim(-u,1+u)
plt.ylim(-u,1+u)
plt.axhline(color='k', linewidth=.5)
plt.axvline(color='k', linewidth=.5)

N=5000

verts, rouges = 0,0
for _ in range(N):
    x=rd.uniform(0,1)
    y=rd.uniform(0,1)
    size=2
    if y<x**2:
        plt.plot(x,y, 'g.', markersize=size)
        verts+=1

    else:
        plt.plot(x,y, 'r.', markersize=size)
        rouges+=1
plt.plot(0,0, 'g.', markersize=size, label='Points sous la courbe')
plt.plot(0,0, 'r.', markersize=size, label='Points au-dessus de la courbe')
plt.legend(fontsize='small', loc='upper right')

print("Nombre de points : %i \n(sous la courbe : %i / au-dessus de la courbe : %i)"%(N, verts, rouges))
print("Proportion de points sous la courbe y=x^2 : %.4f" %(verts/N))
print("Aire totale de l'espace possible des points : 1")
print("-----> Donc aire sous la courbe approx° : %.4f" %(verts/N))

plt.show()




##
circle1 = plt.Circle((0, 0), 1, facecolor=(0, 0, 1, 0.2), edgecolor='b', linewidth=3)
plt.gca().add_patch(circle1)

u=1.1
plt.axis("EQUAL")
plt.xlim(-u,u)
plt.ylim(-u,u)

N=5000

verts, rouges = 0,0
for _ in range(N):
    x=rd.uniform(-1,1)
    y=rd.uniform(-1,1)
    size=2
    if x**2+y**2<1:
        plt.plot(x,y, 'g.', markersize=size)
        verts+=1

    else:
        plt.plot(x,y, 'r.', markersize=size)
        rouges+=1
plt.plot(0,0, 'g.', markersize=size, label='Points dans le cercle')
plt.plot(0,0, 'r.', markersize=size, label='Points hors du cercle')
plt.legend(fontsize='small', loc='upper right')

print("Nombre de points : %i \n(dans le cercle : %i / hors du cercle : %i)"%(N, verts, rouges))
print("Proportion de points dans le cercle : %.4f" %(verts/N))
print("Aire totale de l'espace possible des points : 4")
print("-----> Donc aire du cercle approx° : %.4f" %(4*verts/N))

plt.show()
