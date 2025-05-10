#IMPORTAR DA BIBLIOTECA
import random
numero_secreto = random.randint (1,10)
tentativas = 0
contagem_tentativas = 0
print ("==Bem-vindo ao jogo de número secreto==")
print ("Tente advinhar o número secreto entre 1 e 10.")
#WHILE= ENQUANTO
while tentativas != numero_secreto:
    numero = int(input("Digite um número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero ==numero_secreto:
        print ("Parabéns, você acertou o número secreto")
        print (f"Você precisou de {contagem_tentativas} tentativas.")
        break
    # É IGUAL SENAO SE 
    elif numero< numero_secreto:
        print ("O número secreto é maior.")
    else:
        print ("O número secreto é menor.")
