## https://www.youtube.com/watch?v=mZBwsm6B280

# Question : Quelle est la distribution de la distance entre deux points pris aléatoirement sur un cercle ?


from numpy import sin, cos, pi, arange, quantile, arccos, sqrt
import matplotlib.pyplot as plt
from random import random
from statistics import median, mean

plt.figure(figsize=(8, 8))

# circle1 = plt.Circle((0, 0), 1, color='k', fill=False, linewidth=2)
# plt.gca().add_patch(circle1)
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

plt.axis('equal')

lengths=[]

N=2000 # nombre de paires simulées
for _ in range(N):
    t = random()
    x1, y1 = cos(2*pi*t), sin(2*pi*t)
    t = random()
    x2, y2 = cos(2*pi*t), sin(2*pi*t)

    # plt.pause(1e-6)
    d = sqrt((y2-y1)**2 + (x2-x1)**2)
    lengths.append(d)
    plt.plot([x1,x2], [y1,y2], linewidth=0.5, color=(1,d/2,0))

print('calculs ok\n')

plt.figure(2)

h=0.01 # le pas de l'histogramme de distribution
interv=arange(0, 2, h)
a, _, _ = plt.hist(lengths, interv, color = 'pink', edgecolor = 'green', label='Dist° des écarts')
integ = lambda x: 2/sqrt(4-x**2) * (N*h) / pi
plt.plot(interv, integ(interv), label="(théorique)", color='k', linestyle='-.')

# partie théorique sur la distribution
# [-1; 1] proba cos(t)<x : 1 - arccos(x)/π
# [-1; 1] proba cos(t)=x : 1/√(1-x²)
#  [0; 4] proba 2-2cos(t)=x : 2/√(4x-x²)
#  [0; 2] proba √2-2cos(t)=x : 2/√(4-x²)
# (à normaliser par des constantes bien sûr)

plt.legend()



ro = lambda x: int(x*1000)/1000

q1, me, mo, q3 = quantile(lengths, 1/4), mean(lengths), median(lengths), quantile(lengths, 3/4)
print('1er quartile :', ro(q1))
print('MOYENNE :', ro(me))
print('MEDIANE :', ro(mo))
print('3ème quartile :', ro(q3))

print("\n(approximation de trois : %f)" %quantile(lengths, 2/3)**2)
# note : quartile(2/3) ≈ √3 (cf. la vidéo)

ymax=a[-1]
plt.plot([q1,q1], [0, ymax])
plt.plot([me,me], [0, ymax])
plt.plot([mo,mo], [0, ymax])
plt.plot([q3,q3], [0, ymax])

plt.show()



## En utilisant le module Animation de Matplotlib
# import matplotlib.animation as animation

# line, = plt.plot([], [])
# def animate(i):
#     # ...
#     line.set_data([x1,x2], [y1,y2])
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, interval=2, repeat=False)
# plt.show()