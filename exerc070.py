print ('='*35)
print ('{:^35}'.format ('BEM VINDOS AO COMPRAS ONLINE!'))
print ('='*35)

total = 0 # Recebe total
products_over_1000 = 0 # Recebe produtos acima de mil reais
cheaper = 0 # recebe valor do produto mais barato
cheaper_product = str('') # Recebe nome do produto mais barato
keep = str('') # Recebe condição de continuar

while True:
    keep = 'z' # Keep recebe 'z'
    product_name = str(input('Nome do produto: ')) # Recebe nome do produto
    price = float(input('Valor do produto: ')) # Recebe preço do produto
    total += price # Recebe valor total
    if price > 1000: # Se o preço for maior que mil
        products_over_1000 += 1 # Adicionar +1 em produtos acima de mil
    if cheaper == 0: # Se valor do produto mais barato for igual a zero
        cheaper = price # mais barato recebe preço
        cheaper_product = product_name # produto mais barato recebe o nome
    elif cheaper != 0 and price < cheaper: # se o produto mais barato for diferente de zero e o valor do produto for menor que o menor valor de produto já registrado
        cheaper = price # produto mais barato recebe preço
        cheaper_product = product_name # produto mais barato recebe nome

    while keep not in 'sn': # se nao houver 'sn' na resposta ficar em loop
        keep = str(input('Deseja continuar as compras? [S/N] ').lower()) # keep recebe resposta de condição de parada
    if keep == 'n': # se keep for igual a n
        break; #parar

print ('='*25)
print ('{:^25}'.format ('FIM DA COMPRA!'))
print ('='*25)
print (f'O total da compra foi R${total:.2f} reais\nTemos {products_over_1000} produtos custando mais de R$1000.00 reais\nO produto mais barato foi {cheaper_product} que custa {cheaper:.2f}')