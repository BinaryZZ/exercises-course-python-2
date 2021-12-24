#_______________VARIABLES____________#

product_price = float(input('Digite o valor do produto: ')) #valor do produto

print ('Digite o método de pagamento de acordo com as opções do menu:\n'  #Menu
       '-\033[36m1\033[m à vista em \033[34mdinheiro\033[m ou \033[34mcheque\033[m com \033[33m10%\033[m de desconto','\n'
       '-\033[36m2\033[m à vista no \033[34mcartão\033[m com \033[33m5%\033[m de desconto','\n'
       '-\033[36m3\033[m em até 2x \033[33msem juros\033[m no \033[34mcartão\033[m','\n'
       '-\033[36m4\033[m em 3x ou mais no \033[34mcartão\033[m com \033[33m20%\033[m de juros')

method = int (input('Método de pagamento: '))

#______________CONDICTIONS_____________#

if method == 1:         #método de pagamento 1
    print ('O pagamento com 10% de desconto será de R${:.2f} reais\n'
           .format(product_price*0.90))

elif method == 2:       #método de pagamento 2
    print ('O pagamento com 5% de desconto será no valor de R${} reais'
           .format(product_price*0.95))

elif method == 3:       #método de pagamento 3
    print('O pagamento será em duas parcelas de R${:.2f} reais' .format(product_price,product_price / 2))

elif method == 4:       #método de pagamento 4
    parcel = int(input('Digite a quantidade de parcelas: '))
    if parcel <= 2:     #se as parcelas forem iguais ou menor que 2
        print ('Só aceitamos em 3 ou mais vezes para este método de pagamento')
    else:
        print('O pagamento do valor de R${:.2f} reais será em {} parcelas de R${} reais'.format(product_price, parcel, (product_price * 1.20) / parcel))