# Nome: Rafael Manteiga Balbino
# Matrícula: 201920649111

# Nome: Geovane de Araújo Carvalho Conceição
# Matrícula: 201310102711

import matplotlib.pyplot as plt
import numpy as np

# gera os pontos no intervalo dado para calcular o campo elétrico e plotar o fluxo
def gerapontos(inicio,fim,passo):
  x = np.arange(inicio,fim,passo)
  y = np.arange(inicio,fim,passo)
  return np.meshgrid(x,y)

def calculacampo(x,y):
  # cargas do problema
  q1,q2 = -10,10
  # posições das cargas
  q1x,q1y = -5,0
  q2x,q2y = 5,0

  # calcula campo eletrico
  Ex = q1*(x-q1x)/((y-q1y)**2+(x-q1x)**2)**1.5+q2*(x-q2x)/((y-q2y)**2+(x-q2x)**2)**1.5
  Ey = q1*(y-q1y)/((y-q1y)**2+(x-q1x)**2)**1.5+ q2*(y-q1y)/((y-q2y)**2+(x-q2x)**2)**1.5

  return Ex,Ey

x,y = gerapontos(-10,10,0.01)
Ex,Ey = calculacampo(x,y)
plt.streamplot(x,y,Ex,Ey)
plt.show()
