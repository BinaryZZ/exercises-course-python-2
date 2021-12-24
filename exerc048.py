s = 0 # Receber os valores do for
for c in range (1,501,2): # Repeticao
    if c % 3 == 0: # Passar apenos os numeros divisiveis por 3
        s+= c # Somar todos os numeros recebidos em s de for
print (s)