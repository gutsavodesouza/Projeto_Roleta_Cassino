print("ESCOLHA UMA OPÇÃO DE APOSTA")
print("1 - Única")
print("2 - Dupla")
print("3 - Rua")
print("4 - Six")
print("5 - Coluna")
print("6 - Dúzia")
print("7 - Par ou Ímpar")


# Jogador 1
opcao1 = int(input("Opção de aposta (Jogador 1): "))
num1 = int(input("Número em que vai apostar (Jogador 1): "))
valor1 = float(input("Valor da aposta (Jogador 1): "))

# Jogador 2
opcao2 = int(input("Opção de aposta (Jogador 2): "))
num2 = int(input("Número em que vai apostar (Jogador 2): "))
valor2 = float(input("Valor da aposta (Jogador 2): "))

 # Jogador 3
opcao3 = int(input("Opção de aposta (Jogador 3): "))
num3 = int(input("Número em que vai apostar (Jogador 3): "))
valor3 = float(input("Valor da aposta (Jogador 3): "))


sorteado = int(input("Digite o número sorteado: "))


vitoria1 = 0
vitoria2 = 0
vitoria3 = 0

#  Jogador 1
if opcao1 == 1 and sorteado == num1:
    vitoria1 = valor1 * 35

elif opcao1 == 2 and (sorteado == num1 or sorteado == num1 + 1):
    vitoria1 = valor1 * 17

elif opcao1 == 3 and num1 <= sorteado <= num1 + 2:
    vitoria1 = valor1 * 11

elif opcao1 == 4 and num1 <= sorteado <= num1 + 5:
    vitoria1 = valor1 * 5

elif opcao1 == 5 and ((num1 == 1 and sorteado % 3 == 1) or (num1 == 2 and sorteado % 3 == 2) or (num1 == 3 and sorteado % 3 == 0)):
    vitoria1 = valor1 * 2

elif opcao1 == 6 and ((num1 == 1 and 1 <= sorteado <= 12) or (num1 == 13 and 13 <= sorteado <= 24) or (num1 == 25 and 25 <= sorteado <= 36)):
    vitoria1 = valor1 * 2

elif opcao1 == 7 and ((num1 == 0 and sorteado != 0 and sorteado % 2 == 0) or (num1 == 1 and sorteado % 2 == 1)):
    vitoria1 = valor1 * 1

#  Jogador 2
if opcao2 == 1 and sorteado == num2:
    vitoria2 = valor2 * 35

elif opcao2 == 2 and (sorteado == num2 or sorteado == num2 + 1):
    vitoria2 = valor2 * 17

elif opcao2 == 3 and num2 <= sorteado <= num2 + 2:
    vitoria2 = valor2 * 11

elif opcao2 == 4 and num2 <= sorteado <= num2 + 5:
    vitoria2 = valor2 * 5

elif opcao2 == 5 and ((num2 == 1 and sorteado % 3 == 1) or (num2 == 2 and sorteado % 3 == 2) or (num2 == 3 and sorteado % 3 == 0)):
    vitoria2 = valor2 * 2

elif opcao2 == 6 and ((num2 == 1 and 1 <= sorteado <= 12) or (num2 == 13 and 13 <= sorteado <= 24) or (num2 == 25 and 25 <= sorteado <= 36)):
    vitoria2 = valor2 * 2

elif opcao2 == 7 and ((num2 == 0 and sorteado != 0 and sorteado % 2 == 0) or (num2 == 1 and sorteado % 2 == 1)):
    vitoria2 = valor2 * 1

#  Jogador 3
if opcao3 == 1 and sorteado == num3:
    vitoria3 = valor3 * 35

elif opcao3 == 2 and (sorteado == num3 or sorteado == num3 + 1):
    vitoria3 = valor3 * 17

elif opcao3 == 3 and num3 <= sorteado <= num3 + 2:
    vitoria3 = valor3 * 11

elif opcao3 == 4 and num3 <= sorteado <= num3 + 5:
    vitoria3 = valor3 * 5

elif opcao3 == 5 and ((num3 == 1 and sorteado % 3 == 1) or (num3 == 2 and sorteado % 3 == 2) or (num3 == 3 and sorteado % 3 == 0)):
    vitoria3 = valor3 * 2

elif opcao3 == 6 and ((num3 == 1 and 1 <= sorteado <= 12) or (num3 == 13 and 13 <= sorteado <= 24) or (num3 == 25 and 25 <= sorteado <= 36)):
    vitoria3 = valor3 * 2

elif opcao3 == 7 and ((num3 == 0 and sorteado != 0 and sorteado % 2 == 0) or (num3 == 1 and sorteado % 2 == 1)):
    vitoria3 = valor3 * 1


banca = (valor1 + valor2 + valor3) - (vitoria1 + vitoria2 + vitoria3)


print("Sorteado: ", sorteado)
print("Jogador 1 ganhou: R$", vitoria1)
print("Jogador 2 ganhou: R$", vitoria2)
print("Jogador 3 ganhou: R$", vitoria3)
print("Caixa da banca: R$", banca)
