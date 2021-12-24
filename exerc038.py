num1 = int(input('Digite o primeiro número: ')) #recebe primeiro numero
num2 = int(input('Digite o segundo número: ')) #recebe segundo numero

if num1 > num2: #se o primeiro numero for maior que o segundo numero
    print('O primeiro número é maior!')
elif num2 > num1: #se o segundo numero for maior que o primeiro numero
    print ('O segundo número é maior!')
elif num1 == num2: # se o primeiro numero for igual ao segundo numero
    print('Não existe número maior!')