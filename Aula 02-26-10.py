# comando input(): quero permitir que o usuário digite algo...

nome= input("Digite seu nome: ")

#comando de saída.. exibir na tela

idade= int(input("Digite sua idade:"))

#Comando de saída
print(f"Boa Noite, seu nome é: {nome}")
#Exibir idade
print(f"Sua idade é {idade}:".format(idade))
#Fazer uma equação  de dobro da idade informada

dobro= idade * 2
print("O dobro da idade informada é {}".format(dobro))
#Estrutura condicional- o famoso "SE" (if)
# Se a pessoa for maior de idade, mmostre "Você é maior, ótimo Já pode dirigir"
if (idade>=18):
  print("Você é maior de idade Parabéns!! Ja pdoe dirigir")
else: 
  print("Você é Xóven ainda, Xóven ainda...")
  #E se quiser perguntar o gênero (M= Masculino e F= Feminino)
#Mostre(... Hmm você precisa/precisou prestar o serviço obrigatório)

genero= input("Informe o gênero: M= Maculino; F=Feminino; I= Indefinido:")

if ( idade >= 18 and genero=="M"):
  print("... Hmm você irá prestar/prestou serviços militares")
  
else:
  print (idade<18 and genero=="M")
  print("Ta safe até ficar maior de idade "and(genero=="F") )
  print("Boaaa ta safe")


  
  
  
  