print (f'='*30)
print ('{:^30}' .format('cadastro de pessoas').upper())
print (f'='*30)
question = str('zzz') # Recebe condição de parada
adult = 0 # Recebe quantidade de adultos
man = 0 # Recebe quantidade de homens
womanunder20 = 0 # Recebe mulheres com menos de 20 anos
gender = str ('z') # Recebe gênero

while True:
    question = 'z' # condição de parada recebe 'z
    gender = 'z' # Gênero recebe 'z'
    age = int(input('Idade: ')) # Recebe idade
    if age >= 18: # Se a idade for maior que 18
        adult += 1 # Adulto recebe
    while gender not in 'mf': # Loop enquanto genero nao conter 'mf'
        gender = str(input('Sexo: [M/F]').lower()) # Recebe gênero
        if gender == 'm': # Se gênero for masculino
            man += 1 # homem recebe +1
    if gender == 'f' and age < 20: # Se gênero for feminino e idade for menor que 20
        womanunder20 += 1 # mulher abaixo de 20
    while question not in 'sn': #Enquanto condição de parada não conter s ou n
        question = str(input('Quer continuar? [S/N]: ').lower()) # Recebe condição de parada
    if question == 'n': # Se a resposta for n
        print ('====== FIM DO PROGRAMA ======')
        print (f'Total de pessoas com mais de 18 anos: {adult}\nAo todo temos {man} homens cadastrados\nE temos {womanunder20} mulheres com menos de 20 anos')

        break; # Parar
