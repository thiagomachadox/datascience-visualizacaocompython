#Grafico de barras
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

#Variaveis a serem acessadas na plotagem
titulo = "Grafico de barras"
eixox = "Eixo x"
eixoy = "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Plotagem
plt.bar(x,y)
plt.show()