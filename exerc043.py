#__________VARIABLES_________#

height = float(input('Digite a sua altura separado por ponto, ex: 1.70:  ')) #Digite a sua altura
weight = float(input('Digite o seu peso separado por ponto, ex: 60.5: ')) #Digite o seu peso
imc = weight/(height * height) #Cálculo IMC

#________FUNCTIONS_______#

if imc < 18.5: #se for menor que 18.5
    print ('\033[33mAbaixo do peso\033[m')
elif imc >= 18.5 and imc < 25: #se for igual ou maior que 18.5 e menor que 25
    print ('\033[32mPeso ideal\033[m')
elif imc >= 25 and imc < 30: # se for igual ou maior que 25 e menor que 39
    print ('\033[33mSobrepeso\033[m')
elif imc >= 30 and imc < 40: # se for igual ou maior que 30 e menor que 40
    print ('\033[31mObesidade\033[m')
elif imc >= 40: #se for igual ou maior que 40
    print ('Obesidade mórbida')
