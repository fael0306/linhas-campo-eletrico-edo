# Nome: Rafael Manteiga Balbino
# Matrícula: 201920649111

# Nome: Geovane de Araújo Carvalho Conceição
# Matrícula: 201310102711

import random
import matplotlib.pyplot as plt
import numpy as np

ponto = []

# Função usada para plotar o gráfico
def plotar(ponto):
    plt.title("Campo Elétrico")
    plt.plot(ponto,".")
    plt.show()

# Função que gera pontos a serem plotados a partir de uma entrada e a função
def geraponto(x,y):
    Ey = (y/pow((pow((x+5),2)+pow(y,2)),1.5))+(y/pow((pow((x-5),2)+pow(y,2)),1.5))
    Ex = ((x+5)/pow((pow((x+5),2)+pow(y,2)),1.5))+((x-5)/pow((pow((x-5),2)+pow(y,2)),1.5))
    return (Ey/Ex)

for k in range(0,51):
    x = random.randint(0,50)
    #O domínio da função não inclui onde x=0 nem os pontos (-5,0) e (5,0)
    while x==0:
        x = random.randint(0,50)
    y = random.randint(0,50)
    while ((x==-5 or x==5) and y==0):
        y = random.randint(0,50)
    ponto.append(geraponto(x,y))
plotar(ponto)
