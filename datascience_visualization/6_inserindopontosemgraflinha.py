#Grafico Scatterplot
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
#variavel do tamanho dos x no plt.scatter()
z = [30, 40 , 50, 100]

#Variaveis a serem acessadas na plotagem
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo x"
eixoy = "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Plotagem
plt.scatter(x,y, label = "pontos", color = "#31b404", marker = "o", s=z) #s recebe z
plt.plot(x,y, label = "linha", color = "k", linestyle = "--")
plt.legend()
plt.show()