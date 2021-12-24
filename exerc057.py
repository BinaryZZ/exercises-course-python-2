name = str(input('Digite seu nome: ')) # Recebe o nome
age = int(input('Digite sua idade: ')) # Recebe a idade
gender = 'a' # Recebe da repetição
while True: # Repetição
    gender = str(input('Digite seu gênero M para masculino ou F para Feminino: \n').lower()) # Recebe o Gênero
    if gender == 'f' or gender == 'm': # Se o gênero inserido for igual a 'f' ou 'm'
        break; # parar