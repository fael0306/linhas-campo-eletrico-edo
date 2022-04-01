# Nome: Rafael Manteiga Balbino
# Matrícula: 201920649111

# Nome: Geovane de Araújo Carvalho Conceição
# Matrícula: 201310102711

import random
import matplotlib.pyplot as plt

ponto = []
 
def plotar(ponto):
    plt.title("Gráfico")
    plt.plot(ponto,".")
    plt.show()
    
def geraponto(x,y):
    Ey = (y/pow((pow((x+5),2)+pow(y,2)),1.5))+(y/pow((pow((x-5),2)+pow(y,2)),1.5))
    Ex = ((x+5)/pow((pow((x+5),2)+pow(y,2)),1.5))+((x-5)/pow((pow((x-5),2)+pow(y,2)),1.5))
    return (Ey/Ex)
   
for k in range(0,51):
    x = random.randint(-100,100)
    while x==0:
        x = random.randint(-100,100)
    y = random.randint(-100,100)
    while ((x==-5 or x==5) and y==0):
        y = random.randint(-100,100)
    ponto.append(geraponto(x,y))
plotar(ponto)
