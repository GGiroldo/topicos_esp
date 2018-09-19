########## 3 ##########
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2

print('O resultado da soma é: {}' .format(soma))
'''
########## 10 ##########
'''
f = float(input('Digite o grau de Farenheit: '))

cvrt = (f - 32) / 180

print('O valor em Celcius será: {}'.format(cvrt))
'''
########## 14 ##########

vH = float(input('Digite o valor da hora trabalhada: '))
hM = int(input('Digite o numero de horas trabalhada no mes: '))

calcSalarioB = (vH * hM)
calcIRENDA = (calcSalarioB*7.5)/100
calcINSS = (calcSalarioB*8)/100
calcSIND = (calcSalarioB*1)/100
calcSalarioL = (calcSalarioB - calcIRENDA - calcINSS - calcINSS)
