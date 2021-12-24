result = 0 # Recebe resultado
c = 1 # Recebe valor a ser multiplicado
attempt = 0 # Recebe tentativas
plural = str('') # recebe valor plural

while c != 11: # Enquanto valor a ser multiplicado for diferente de 11
    if c == 1: # Se valor a ser multiplicado for igual a 1
        print ('='*40)
        n = int(input(f'Você quer ver a tabuada de qual valor? ')) # Recebe um numero
        print('=' * 40)
        if n < 0: # Se o numero digitado for 0 ou menor
            break; # Parar
        attempt += 1 # Tentativas recebe 1
        if attempt > 1: # se attempt for maior que 1
            plural = 's' # plural recebe s
    result = n * c # Resultado recebe numero inserido vezes numero a ser multiplicado
    print (f'{n} x {c} = {result}', end = '\n')
    c += 1 # Numero a ser multiplicado recebe 1
    if c == 11: # Se numero a ser multiplicado for igual a 11
        c += -10 # Subtrair -10 de c

print (f'Você consultou por {attempt} tabuada{plural}.' if attempt >= 1 else 'Você não consultou nenhuma tabuada.')
