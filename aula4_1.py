#Subprogramas
import random


def trocar(valores,pos1,pos2):
    if 0<=pos1<len(valores) and 0<=pos2<len(valores):
        temp=valores[pos1]
        valores[pos1]=valores[pos2]
        valores[pos2]=temp
    return None

#Programa Principal

amigas=["Ane", "Carolzinha","Lu", "Fernandinha","Jessica"]
trocar(amigas,1,3)
print(amigas)
trocar(amigas,0,2)
print(amigas)
trocar(amigas,2,3)
print(amigas)
trocar(amigas,4,1)
print(amigas)
trocar(amigas,3,0)
print(amigas)
trocar(amigas,2,0)