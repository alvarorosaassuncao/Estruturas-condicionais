# PROJETO PAR OU IMPAR.
while True:
  try:
    valor = int(input('Digite um valaor:'))
    if valor % 2 == 0:
      print('Numero PAR')
    else:
      print('Numero ÍMPAR')
    
  except:
      print('Digite apenas números')
