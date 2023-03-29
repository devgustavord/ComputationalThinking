# Entendendo o elif(ou então...)

# num = 0
#
# if num < 0:
#     print("número negativo")
# elif num == 0:
#     print("número zero")
# else:
#     print("número positivo")
#
# print("----------------------------------------")

# # comparar o num3 com os outros 2
# if num3 < num1:
#     print("n3 é o menor dentre todos")
# elif num3 == num1:
#     print("n3 é igual a n1")
# elif num3 == num2:
#     print("n3 é igual a n2")
# elif num1 < num3 < num2: # equivalente a num1 < num3 and num3 < num2
#     # entra aqui caso o 3 esteja entre 1 e 2
#     print("n3 está entre n1 e n2")
# elif num3 > num2:
#     print("n3 é maior que os outros n2")
#
# num1 = float(input("diga um número: "))
# num2 = float(input("diga o segundo número: "))
# num3 = float(input("diga um terceiro número: "))
#
# if num1 > num2 and num1 > num3:
#     print("n1 é o maior número de todos")
# elif num2 < num1 < num3:
#     print("n1 está entre n2 e n3")
# elif num1 < num2 and num1 < num3:
#     print("n1 é o menor número de todos")
# elif num1 == num2:
#     print("n1 é igual a n2")
# elif num1 == num3:
#     print("n1 é igual a n3")
#
# if num3 > num1 > num2:
#     print("n3 é maior que n1, e n1 é maior que n2")
# elif num3 > num2 > num1:
#     print("n3 é maior que n2, e n2 é maior que n1")
# elif num2 > num3 > num1:
#     print("n2 é maior que n3, e n3 é maior que n1")
# elif num1 > num3 > num2:
#     print("n1 é maior que n3, e n3 é maior que n2")
# elif num1 > num2 > num3:
#     print("n1 é maior que n2, e n2 é maior que n3")
# elif num2 > num1 > num3:
#     print("n2 é maior que n3, e n1 é maior que n3")
# elif num3 == num2 == num1:
#     print("n3 é igual a n2, e n2 é igual a n1")
# elif num3 == num2 > num1:
#     print("n3 é igual a n2, e n2 é maior que n1")
# elif num3 == num2 < num1:
#     print("n3 é igual a n2, e n2 é menor que n1")
# elif num3 == num1 > num2:
#     print("n3 é igual a n1, e n1 é maior que n2")
# elif num3 == num1 < num2:
#     print("n3 é igual a n1, e n1 é menor que n2")
# elif num1 == num2 > num3:
#     print("n1 é igual a n2, e n2 é maior que n3")
# elif num1 == num2 < num3:
#     print("n1 é igual a n2, e n2 é menor que n3")

# Match/Case
# uma comparação de igualdade

'''
sintaxe:

match variável:     #tente combinar a variável com os cases
    case 'condição':    #comparação de igualdade
        ação
'''
# num = 10
# match num:
#     case 0: #comparando se o num é igual a 0
#         print("O número é 0")
#     case 1:
#         print("O número é 1")
#     case 5:
#         print("O número é 5")
#     case _: # else
#         print("O número não é 0, nem 1, nem 5")

## utilizando comparação de desigualdade no match:

# num = 10
# match num:
#     case 0:
#         print("O num é 0")
#     case _ if num > 0:
#         print("O número é maior que 0")

## pegue a idade de duas pessoas se são iguais
## se não for, diga a diferença entre elas, sem que o número seja negativo (e sem usar abs)

nome1 = input("Digite seu nome: ")
nome2 = input("Digite seu nome: ")

idade1 = int(input(f"{nome1} digite a sua idade em anos: "))
idade2 = int(input(f"{nome2} digite a sua idade em anos: "))

if idade1 == idade2:
    print("Ambas idades são iguais")
elif idade1 > idade2:
    dif = idade1 - idade2
    print(f"{nome1} é mais velho com {dif} anos de idade a mais.")
else:
    dif = idade2 - idade1
    print(f"{nome2} é mais velho com {dif} anos de idade a mais.")




