
"""Programa para gerar qual a idade do usuario"""
#Ano atual
dtAno = intput('Digite o Ano atual: ')
if dtAno.isspace() or dtAno.isalpha():
    pirnt('Caracteres incorretos!')
    
#Aqui coleta o ano de nascimento do usuario
dtNas = input("Digite o ano do seu nascimento:")
if dtNas.isspace() or dtNas.salpha():    
   pirnt('Caracteres incorretos!')
    
#Calculo para gerar a idade
idade = int(dtAno) - int(dtNas)

print('Você tem {} Anos!'.format(idade))

#condições para gerar maior idade ou não
if idade < 18:
    print ("Você é de menor!")
elif(dtNas >= 0000):
    print ("Data de nascimento não é valido!")
else:
    print("Você é de maior!")




