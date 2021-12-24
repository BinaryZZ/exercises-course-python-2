import random # Biblioteca
sum = 0 # Soma
attempt = 0 # Tentativa
result = 0 # Resultado
plural = str('') # Recebe plural
eo = ('aaaa') # recebe par ou impar
print ('-='*20)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print ('-='*20)
while True: # loop
    eo = 'zzz' # da valor zzz para par ou impar
    n = int(input('Digite um valor: ')) # recebe um numero
    while eo not in 'PpIi': # enquanto par ou impar nao houver valor 'PpIi
        eo = str(input('Par ou ímpar? [P/I] ')).lower() # recebe par ou impar
        if eo == 'p': # se a resposta for par
            result = 1 # resultado recebe 1
        elif eo == 'i': # se aresposta for impar
            result = 2 # resultado recebe 2

    print ('=' *30)
    pc = random.randrange(1,10) # pc escolhe um numero aleatório de 1 a 10
    sum = n + pc # soma recebe numero inserido + escolha do pc

    if result == 1 and sum%2 == 0 or result == 2 and sum%2 == 1: # validação de vitória
        attempt += 1 # tentativa recebe 1
        if attempt == 2: # se tentativa for maior que 2
            plural = 'es' # plural recebe 'es'
        print ('DEU PAR!') # Deu par
        print ('PARABÉNS, VOCÊ VENCEU!')
        print('-=' * 20)

    elif result == 1 and sum%2 == 1 or result == 2 and sum%2 == 0: # validação de derrota
        print ('DEU IMPAR!') # Deu ímpar
        print (f'VOCÊ PERDEU!')
        print('-=' * 20)
        print (f'GAME OVER! Você venceu {attempt} vez{plural}' if attempt >=1 else 'GAME OVER! Você não venceu nenhuma vez :(')
        break;