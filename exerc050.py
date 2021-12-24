np = 0 # Recebe os valores do for
for c in range (0,6): # Repetição
    n = int(input('Digite um número: ')) # Recebe valor inserido
    if n % 2 == 0: # Se o valor for dividido por 2
        np += n # np + np recebe n (que é o valor inserido)

print ('A soma dos números pares é de {}' .format(np))
print (np)