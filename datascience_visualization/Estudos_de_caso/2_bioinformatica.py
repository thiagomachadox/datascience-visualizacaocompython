entrada = open("sequence2.fasta").read()
saida = open("bacteria.html", "w")

#Criando dicionario vazio para armazenar valores
cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

#Problema na execuçao pois ele da o \n, entao:
entrada = entrada.replace("\n","")

for k in range(len(entrada) - 1): #menos 1 por conta do ultimo par nucleico
    cont[entrada[k]+entrada[k+1]] += 1

#html 
saida.write("<div>")
i=1

for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; color: #fff; height:100px; float:left; background-color:rgba(0,255, "+str(transparencia)+"')>"+k+"</div>")
    
    if i%4 == 0:
        saida.write("div style='clear:both'></div")

    i+=1

saida.close()