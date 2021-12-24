sum = 0 # soma
count = 0 # contador
print (f'Bem vindo ao Super Contador!!!\nTodos os números digitados serão somados\nPara ver a soma de todos os números apenas digite 999')
while True: # loop
    number = int (input('Digite um número: ')) # Recebe um numero
    if number == 999: # se o numero for 999
        print ('No total foram inseridos {} números e a soma deles totalizou {}' .format(count,sum))
        break; # parar
    sum += number # soma recebe o numero inserido
    count += 1 # contador recebe +1
#adicionar contagem numero
#se digitar 999 break
