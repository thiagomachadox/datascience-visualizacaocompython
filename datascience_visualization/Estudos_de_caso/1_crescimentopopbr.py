#Crescimento da população brasileira 1980-2016
#DataSUS

import matplotlib.pyplot as plt 
dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))


titulo = "Evolução da população brasileira: 1980-2016"
eixox = "Ano"
eixoy = "População x100.000.000"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.bar(x, y, color = "#e4e4e4")
plt.plot(x,y, marker = "o", color = "k")
#plt.show()
plt.savefig("populacao_brasileira", dpi=300)