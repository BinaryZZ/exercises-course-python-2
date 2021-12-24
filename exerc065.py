sum = 0 # Soma
count = 0 # contador
maximum = 0 # Maximo
minimum = 0 # Minimo

while True:
    n = int(input('Digite um número: ')) # Recebe um valor
    sum += n # Soma recebe n
    count += 1 # Contador recebe mais um
    if n > maximum: # Se o numero inserido for maior que maximum
        maximum = n # Maximum recebe numero inserido
    elif n < minimum: # Se numero inserido for menor que maximum
        minimum = n # Minimum recebe numero inserido
    e = str(input('Você quer continuar?\nPara continuar digite qualquer outra coisa:\nPara parar digite n ou N\n'))
    if e.lower() == 'n': # Se a resposta for igual a n
        print ('Foram digitados {} números\nA média dos números inseridos foi de {}\nA soma de todos números inseridos foi de {}\nO maior número foi {} e o menor número foi {}'.format(count,sum/count,sum,maximum,minimum))
        break; # Parar