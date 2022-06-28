""" Représente les décimales d1,d2,d3... d'un nombre réel
    en tournant successivement de d1, puis d2, puis d3...
    Les nombres rationnels produisent un motif périodique.
    https://twitter.com/matthen2/status/1433081884402233347 """

import turtle
import random
from decimal import *


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
b=10

pas=9
speed=500

getcontext().prec = acc
x=strings(Decimal(1)/Decimal(3**6))
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
    print("%i/%i %i"%(cpt, n, int(digit)))
    pen.left(360*int(digit)/b)
    pen.forward(pas)
    cpt+=1

window.exitonclick()
