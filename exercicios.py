'''
Exercicio 3. Dado um numero pelo usuario, exibir o  anterior e posterior (EX: input = 20, resposta = 19 e 21
'''

coleta_numero = int(input("Digite o seu número:"))

maior = coleta_numero + 1
menor = coleta_numero - 1

print(f"O número digitado é {coleta_numero} e o seu maior é {maior} e seu menor é {menor}")

'''
Exercicio 4. Dados dois numeros pelo usuário, calcular a potência entre eles
'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

potencia = float(numero1 ** numero2)

print(f"A potência entre {numero1} e {numero2} é {potencia}")
'''
Exercicio 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5

'''

numero1 = int(input("Digite um número: "))
if numero1 % 5 == 0:
    multiplo = numero1 + 5
else:
    multiplo = numero1 + (5 - numero1 % 5)

print(f"O próximo múltiplo de 5 é {multiplo}.")


