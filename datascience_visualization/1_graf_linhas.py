#Grafico de linhas
import matplotlib.pyplot as plt 

x = [1, 2, 5, 7]
y = [2, 3, 5, 7]


#Titulo
plt.title("Gráfico de Linhas em Python")

#Labels
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.plot(x,y)
plt.show()