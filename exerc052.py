n = int(input('Digite um número: ')) # Recebe um numero

mult = 0 # Recebe valor de mult na repetição
for c in range(1,n+1):
    if n % c == 0: # Se o numero recebido dividido pelo numero gerado for igual a zero
        mult += 1 # Somar +1 em mult

if mult == 2: # Se mult for igual a dois
    print ('O número \033[36m{}\033[m é primo' .format (n))
elif mult < 2: # se mult for menor que 2
    print ('O número \033[36m{}\033[m não é primo' .format (n))