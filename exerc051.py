first_term = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))

print ('As 10 primeiras progressões de {} progressões de 5 são:' .format(first_term))

for c in range(first_term,10*reason,reason):
    print (c, end = ' -> ' )