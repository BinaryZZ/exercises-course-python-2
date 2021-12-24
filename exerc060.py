n = int(input('Digite um número e receba seu fatorial: ')) # valor a ser recebido
x = 0
xx = 0
attempt = 0
result = 0
print ('O fatorial de {}! é:' .format(n))
while attempt == 0:
    attempt = 1
    x = n
    xx = n-1
    break;
while attempt == 1:
    attempt += 1
    result += x * xx
    print(n, 'x', xx, end=' x ')
    x += -1
    xx += -1
while attempt == 2:
    result = result * xx
    print(xx , end = ' x ')
    xx += -1
    if xx == 1:
        print('1 = {}' .format(result))
        break;