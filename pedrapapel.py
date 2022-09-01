print("""
Escolha uma aleternativa \n
1- Pedra \n 
2- Papel \n
3- Tesoura \n
""")
from random import randint
PC = randint(1,3)
escolha = int(input())
print(f'o computador escolheu {PC}')
if (escolha == PC):
  print("empate")
elif(( escolha == 1 ) and (PC == 2)):
  print("computador wins")
elif(( escolha == 1 ) and (PC == 3)):
  print("Você ganhou")
elif(( escolha == 2 ) and (PC == 1)):
  print("você ganhou")
elif(( escolha == 2 ) and (PC == 3)):
  print("computador wins")
elif(( escolha == 3 ) and (PC == 1)):
  print("computador wins")
elif(( escolha == 3 ) and (PC == 2)):
  print("Você ganhou")
else:
  print("Jogou algo errado")
  

