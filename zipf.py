""" Prendre un texte, compter les occurences de ses mots les plus récurrents,
et régressionner linéairement pour mettre en évidence la loi de Zipf """

import matplotlib.pyplot as plt
from math import log10
from operator import itemgetter
import re
from random import random
from sklearn.linear_model import LinearRegression


def zipf(file):
    text = open(file, 'r', encoding='iso-8859-1').read().lower()
    text = text.replace('\n', ' ').replace(',', ' ').replace('.', ' ') \
               .replace(':', ' ').replace(';', ' ').replace('!', ' ') \
               .replace('?', ' ').replace('/', ' ').replace('~', ' ') \
               .replace('"', ' ').replace('#', ' ').replace('\r', ' ') \
               .replace('{', ' ').replace('(', ' ').replace('[', ' ') \
               .replace('-', ' ').replace('|', ' ').replace('_', ' ') \
               .replace('@', ' ').replace(')', ' ').replace(']', ' ') \
               .replace('=', ' ').replace('}', ' ')
    words = text.split(' ')
    words = [w for w in words if w!='']
    dict = {}
    for w in words:
        dict[w] = dict.get(w, 0) + 1
    Y = sorted(dict.values(), reverse=True)
    X = list(range(1, len(Y) + 1))

    Yv = sorted([(k, v) for (k, v) in dict.items()],
               key=itemgetter(1), reverse=True)
    # print(Yv[:20])

    a=1.5
    col = (random()/a, random()/a, random()/a)

    plt.loglog(X, Y, '+', color=col, label=file, markersize=3)

    Xl = [[log10(x)] for x in X]
    Yl = [[log10(y)] for y in Y]
    reg = LinearRegression().fit(Xl, Yl)
    Ypred = reg.predict(Xl)
    Yl2 = [10**y[0] for y in Ypred]
    plt.loglog(X, Yl2, '-.', linewidth=1, color=col,
               label=f'{reg.coef_[0][0] : .3f}x+{reg.intercept_[0] : .3f}')

zipf('testzipf1.txt')
# zipf('testzipf2_1.txt')
# zipf('testzipf2_2.txt')
# zipf('testzipf2_3.txt')
plt.xlabel("Classement en occurrences")
plt.ylabel("Nombre d'occurrences")
plt.legend()
plt.show()
