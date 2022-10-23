#Especificando variáveis
peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura ** 2)

#saída do resultado
print(f"O IMC dessa pessoa é  de {imc:.1f}")

#Condições

#Identificando usuário abaixo do peso
if imc <18.5:
    print('Você está abaixo do peso normal')

#Identificando usuário com seu peso ideal
elif 18.5 <= imc < 25:
    print('Parabéns, você esta na faixa de peso ideal')

#Identificando usuário com sobrepeso
elif 25 <=imc < 30:
    print('Você esta em SOBREPESO!')

#Identificando usuário em obesidade
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE!')
