#___________LIBRARY____________#

import datetime #Importando biblioteca

#_____________VARIABLES_____________#

year_birthday = int(input('Digite o seu ano de nascimento: ')) #ano de nascimento
year = datetime.date.today().year # ano atual
age = year-year_birthday # idade

#____________CONDITIONS________##
print ('O atleta tem {} anos.' .format(age)) #Idade
if age <= 9: #se for igual a 9 ou menor
    print('Sua categoria é \033[34mMirim\033[m')
elif age >= 10 and age <= 14: # se for entre 10 e 14
    print('Sua categoria é \033[34mInfantil\033[m')
elif age >= 15 and age <= 19: # se for entre 15 e 19
    print ('Sua categoria é \033[34mJúnior\033[m')
elif age == 20: # se for igual a 20
    print('Sua categoria é \033[34mSenior\033[m')
elif age >= 21: # se for maior que 21
    print ('Sua categoria é \033[34mMaster\033[m')