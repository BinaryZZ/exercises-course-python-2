sum = 0 # Recebe somatória
attempt = 0 # Recebe tentativas

while True:
    n = int(input('Digite um valor (digite *999* para parar):\n ')) # Recebe um número
    if n == 999: # Se o número recebido for igual a 999
        print (f'A soma dos {attempt} valores foi de {sum}' if attempt >= 1 else 'Você não digitou nenhum valor.')
        break; # Parar
    sum += n # Soma recebe + n
    attempt += 1 # Tentativas recebe + 1

