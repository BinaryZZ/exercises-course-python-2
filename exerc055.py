list = [] # Lista
for c in range (0,5): # Repetição
    weight = float(input('Digite o seu peso: ')) # Receber o peso
    list.append(weight) # Acrescentar o peso na lista
print ('O maior peso inserido foi de : {:.1f}\nJá o menor peso inserido foi de : {:.1f}' .format(max(list),min(list)))