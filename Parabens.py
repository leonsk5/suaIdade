"""Programa para gerar qual a idade do usuario"""
# Ano atual
dtAno = input('Digite o Ano atual: ')
if dtAno.isspace() or dtAno.isalpha():
    print('Caracteres incorretos!')
else:
 dtNas = input("Digite o ano do seu nascimento:")
 if dtNas.isspace() or dtNas.isalpha():
   print('Caracteres incorretos!')

# Calculo para gerar a idade
 idade = int(dtAno) - int(dtNas)

 print('Você tem {} Anos!'.format(idade))

# condições para gerar maior idade ou não
 if idade < 18:
    print("Você é de menor!")
 
 if idade > 18:
  print("Você é de maior!")




