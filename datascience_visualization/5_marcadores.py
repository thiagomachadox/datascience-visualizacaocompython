#Grafico Scatterplot
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

#Variaveis a serem acessadas na plotagem
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo x"
eixoy = "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Plotagem
plt.scatter(x,y, label = "Meus pontos", color = "g", marker = "x", s=100)
plt.plot(x,y, label = "Minha linha", color = "k", linestyle = "--")
plt.legend()
plt.show()