import random

pontos_usuario = 0
pontos_comput = 0

options = ['r', 't', 'p']

while True:
  escolha_usuar = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

  if escolha_usuar == 'q':
    break

  if escolha_usuar not in options:
    continue

  computer_choice = random.randint(0,2)

  computer_options = options[computer_choice]

  print('O computador escolheu ' + computer_options)

  if escolha_usuar == computer_options:
    print('==========================')
    print('Empate!')
    print('==========================')

  elif escolha_usuar == 'r' and computer_options == 't':
    print('==========================')
    print("Você ganhou!")
    print('==========================')
    pontos_usuario = pontos_usuario + 1
    
  elif escolha_usuar == 'p' and computer_options == 'r':
    print('==========================')
    print("Você ganhou!")
    print('==========================')
    pontos_usuario = pontos_usuario + 1

  elif escolha_usuar == 't' and computer_options == 'p':
    print('==========================')
    print("Você ganhou!")
    print('==========================')
    pontos_usuario = pontos_usuario + 1

  else:
    print('==========================')
    print("Você perdeu!")
    print('==========================')
    pontos_comput = pontos_comput + 1


print('==========================')
print('Sua pontuação: ' + str(pontos_usuario))
print('==========================')
print('Pontuação do computador: ' + str(pontos_comput))
print('==========================')

if pontos_comput > pontos_usuario:
  print('VOCÊ FOI DERROTADO!!!')

elif pontos_comput == pontos_usuario:
  print('==========================')
  print('Empate')
  print('==========================')

else:
  print('Vitória!!')

print("Goodbye!")
