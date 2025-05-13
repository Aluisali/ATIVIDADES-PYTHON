# Oh lula meu presidente
ano_atual= 2025
data_nascimento = int(input("Digite o seu ano de nascimento:"))
idade = ano_atual-data_nascimento
print (f" Você tem {idade} anos.")
if idade<16:
    print ("Você não pode votar!")
elif idade<18 or idade >70:
    print (" Seu voto é facultativo!")
elif idade >=18:
    print (" Seu voto é obrigatorio!")
           
    

 
  
