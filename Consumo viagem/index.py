destino =(input('Para onde você deseja ir?'))
distancia = int(input('Qual a distância total?'))
km = int(input('Quantos km por litros seu automóvel faz?'))
gasolina = float(input('Qual o valor atual da gasolina ou alcóol?'))

consumo = (distancia / km) * gasolina

print(f'Você gastara de gasolina {consumo:.2f} para chegar até {destino}')


