import numpy as np
import random
import matplotlib.pyplot as plt

T = float(input('Введите Т: '))
x = int(input('input size: '))
C_N = range(x)
matrix = np.zeros((x, x))
for i in range(x):
    for j in range(x):
        matrix[i][j] = random.choice([-1,1])
print(matrix)


mas = []
mas = matrix.copy()
for i in range(int(input('input iteration count: '))):
    E = E1 = 0
    for j in range(x):
        for k in range(x):
            E += matrix[j][k] * matrix[j][k - 1] + matrix[j - 1][k] * matrix[j][k]
            #E*=-1
    mas1 = []
    mas1 = matrix.copy()
    mas1[random.choice(C_N)][random.choice(C_N)] *= -1
    for j in range(x):
        for k in range(x):
            E1 += mas1[j][k] * mas1[j][k - 1] + mas1[j - 1][k] * mas1[j][k]
            #E1*=-1
    deltaE = -1 * (E1 - E)

    if deltaE <= 0:
        matrix = mas1.copy()
        mas = matrix.copy()
    else:
        
        P = random.random()
        W = np.exp(-deltaE/T)
        if P <= W:
            mas = matrix.copy()
        else:
            matrix = mas.copy()
    #print(matrix)
    plt.clf()
    plt.imshow(matrix)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff()




