#Boxplot

import matplotlib.pyplot as plt 
import random

v = []

for i in range(250):
    numero_aleatorio = random.randint(0,10)
    v.append(numero_aleatorio)


plt.title("Boxplot")
plt.boxplot(v)
plt.show()