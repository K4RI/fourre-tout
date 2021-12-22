## https://twitter.com/matthen2/status/1433081884402233347

import turtle
import random
from decimal import *

# Représenter sous forme de motifs réguliers la périodicité du développement décimal des nombres rationnels.


strings = lambda x: str(int(x)) + str(x-int(x))[2:]


def numberToBase(n, b):
    n = int(n)
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


acc=1000
b=10 # la base arithmétique utilisée (par défaut, 10)

pas=9
speed=500

getcontext().prec = acc # précision du module décimal
x=strings(Decimal(1)/Decimal(3**6)) # la fraction du nombre rationnel à représenter (ici, le nombre 1/3⁶)
print("%s en base %i s'écrit"%(x, b))
x=numberToBase(x,b)
print(x)




window = turtle.Screen()

pen = turtle.Turtle()
pen.speed(speed)
pen.color("black")
pen.pendown()

n=len(x)
cpt=0
for digit in x:
    cpt+=1
    print("%i/%i %i"%(cpt, n, int(digit)))
    pen.left(360*int(digit)/b)
    pen.forward(pas)

window.exitonclick()