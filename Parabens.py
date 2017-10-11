"""Programa para gerar qual a idade do usuario"""
#Ano atual
anoAtual = 2017

#Aqui coleta a data de nascimento do usuario
dataNas = int(input("Digite o ano do seu nascimento:"))

#Calculo para gerar a idade
anos = (anoAtual - dataNas)
print("Você tem " + str(anos) + " Anos!")

#condições para gerar maior idade ou não
if anos < 18:
    print ("Você é de menor!")
elif(dataNas == 0):
    print ("Data de nascimento não é valido!")
else:
    print("Você é de maior!")




