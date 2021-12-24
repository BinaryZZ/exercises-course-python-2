#______________Library___________#

import datetime #importando biblioteca datetime

#_____________Variables_____________#

year_birthday = int(input('Digite seu ano de nascimento: ')) #recebendo ano de nascimento
year = datetime.date.today().year # recebendo ano atual
age = year - year_birthday

#_____________Conditions__________#

if age < 18: # se for menor de 18 anos
    if age == 17:
        print ('\033[32mVocê deverá se alistar em {} ano\033[m' .format(18-(age))) #Mensagem singular
    else:
        print('\033[32mVocê deverá se alistar em {} anos que será no ano de {}\033[m' .format(18-(age),year+(18-age)))
elif age == 18: # se houver 18 anos
    print ('\033[34mEste é o ano do seu alistamento ao serviço militar!\033[m')
elif age > 18: #se for maior de 18 anos
    print ('\033[31mVocê passou do tempo de seu alistamento junto ao serviço militar que foi no ano de {}, regularize sua situação!\033[m' .format(year+(18-age)))