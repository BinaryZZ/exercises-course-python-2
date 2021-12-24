print ('='*35)
print ('{:^35}'.format ('BEM VINDO AO BANCO BINARY'))
print ('='*35)
withdraw = 0 # Saque
withdraw = int(input('Que valor você deseja sacar? R$'))
fifty = withdraw // 50 # Carteira divide 50 por inteiro
withdraw += - (fifty*50) # Carteira subtrai valor da divisão por inteira de cinquenta
twenty = withdraw // 20 # Carteira divide 20 por inteiro
withdraw += - (twenty*20) # Carteira subtrai valor da divisão por inteira de vinte
ten = withdraw // 10 # Carteira divide 10 por inteiro
withdraw += - (ten*10) # Carteira subtrai valor da divisão por inteira de dez
one = withdraw // 1 # Carteira divide 1 por inteiro
withdraw += - (one*1) # Carteira subtrai valor de 1 dividido por inteiro

print (f'Total de {fifty} celulas de R$ 50\n'
       f'Total de {twenty} celulas de R$ 20\n'
       f'Total de {ten} celulas de R$ 10\n'
       f'Total de {one} celulas de R$ 1')

print('='*35)
print ('FIM DA OPERAÇÃO')
print('='*35)