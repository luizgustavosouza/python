#1015 - URI ONLINE JUDGE | Distancia  Euclidiana entre dois pontos
import math

from math import sqrt

coord1=input().split()

x1=float(coord1[0])
y1=float(coord1[1])

coord2=input().split()

x2=float(coord2[0])
y2=float(coord2[1])

coord1 = (x2-x1)**2
coord2 = (y2-y1)**2

distancia= sqrt(coord1+coord2)

print("%2.4f" %distancia)