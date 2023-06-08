import matplotlib.pyplot as plt
import numpy as np

def gerar_pontos(inicio, fim, passo):
    x = np.arange(inicio, fim, passo)
    y = np.arange(inicio, fim, passo)
    return np.meshgrid(x, y)

def calcular_campo(x, y):
    q1, q2 = -10, 10
    q1x, q1y = -5, 0
    q2x, q2y = 5, 0

    denom1 = ((y - q1y) ** 2 + (x - q1x) ** 2) ** 1.5
    denom2 = ((y - q2y) ** 2 + (x - q2x) ** 2) ** 1.5

    Ex = q1 * (x - q1x) / denom1 + q2 * (x - q2x) / denom2
    Ey = q1 * (y - q1y) / denom1 + q2 * (y - q1y) / denom2

    return Ex, Ey

x, y = gerar_pontos(-10, 10, 0.01)
Ex, Ey = calcular_campo(x, y)
plt.streamplot(x, y, Ex, Ey)
plt.show()
