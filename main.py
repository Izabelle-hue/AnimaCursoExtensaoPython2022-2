# Meu primeiro projeto Python!!
# print()= comando de saida
print("Hello Human")
#String é um alfa numerico... uma frase..
nome = "Izabelle Souza"
idade = 21
curso = "compute engineering"
# sem as "" aspas são valores quânticos e tem que ser um número inteiro
#Exibir o nome (que esta dentro da variável nome)
print(nome)
print(idade)
print(curso)
#Para exibir uma frase que completa o conteúdo de uma variável   
print("Meu nome é "+nome)
print("Minha idade é "+str(idade))
print(f"Meu curso é {curso}")
print("Minha idade é {} anos".format(idade))
#para não dar erro, na concatenação se usa para converter uma variavel inteiro para string OU DO OUTRO JEITO= print f(Minha idade é{idade})
#FRASE: Exibir mais de uma varável em uma frase 
print("Meu nome é {} e tenho {} anos".format(nome,idade))