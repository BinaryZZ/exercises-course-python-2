import datetime # Importando Biblioteca
year = datetime.date.today().year

people = 0 # Quantidade de pessoas
adult = 0 # Quantidade de adultos
non_adult = 0 # Quantidade de não adultos
for c in range(0, 6): # Repetição
    people += 1 # Adicionar +1 em pessoa
    birthday = int(input('Digite o seu ano de nascimento: ')) # Receber ano de nascimento
    if year - birthday >= 21: # Se o ano de nascimento for igual ou maior a 21
        adult += 1 # Somar +1 em adulto
    elif year - birthday < 21: # Se for menor de 21 anos
        non_adult += 1 # Somar +1 em não adulto

print ('Das \033[36m{}\033[m pessoas \033[36m{}\033[m já atingiram a maioridade e \033[36m{}\033[m ainda não atingiram a maioridade.'
       .format (people,adult,non_adult))