list_name,list_age,list_gender = [],[],[] # Lista
people = 0 # Recebe pessoas de repeticao
age_sum = 0 # Recebe soma idade de repeticao
young_woman = 0 # Recebe soma de quantidade de mulheres com menos de 20 anos
for c in range (0,3): # Repeticao
    name = str (input('Digite o seu nome: ')) # Recebe nome
    list_name.append(name) # Adiciona nome recebido na lista
    people += 1 # Acrescenta +1 em pessoas
    age = int (input('Digite a sua idade: ')) # Recebe idade
    list_age.append(age) # Acrescenta idade recebida na lista
    age_sum += age # Soma idade inserida na soma de idades
    gender = int(input('Informe seu gênero: \n -1 para maculino;\n -2 para feminino; \n -3 para outros;\n Digite sua escolha digitando seu respectivo número: ')) # Recebe genero
    if gender == 1: # Se genero inserido for 1
        list_gender.append('Masculino')
    elif gender ==2: # Se genero inserido for 2
        if age < 20: # Se houver menos que 20 anos
            young_woman +=1 # Somar +1 em mulheres com menos de 20 anos
        list_gender.append('Feminino')
    elif gender ==3: # Se genero inserido for 3
        list_gender.append('Outro')

max_age = max(list_age) # Acha a maior idade na lista
max_find = list_age.index(max_age) # Acha o bloco da maior idade na lista
age_average = age_sum / people # Recebe a media de idade
print ('A média de idade das {} pessoas é de: {}\nE o nome da pessoa mais velha é: {}\nDentro dessas pessoas {} mulheres tem menos de 20 anos'.format(people,int(age_average),list_name[max_find],young_woman)) # acha o nome na lista por bloco encontrado em idade