#_______________LIBRARIES_____________#

from random import choice

#_______________VARIABLES____________#

stone = str('Pedra') #Pedra
paper = str('Papel') #Papel
scissors = str('Tesoura') #Tesoura
jokenpo = (stone,paper,scissors) #Junção de papel,pedra e tesoura
pc = choice(jokenpo) #escolha aleatória do PC
print ('\033[36mBem vindo ao JOKENPO!!!\n'
       'Selecione um item do menu digitando seu respectivo número:\033[m\n'
       '\033[36m1\033[m- \033[35mPedra\033[m\n'
       '\033[36m2\033[m- \033[35mPapel\033[m\n'
       '\033[36m3\033[m- \033[35mTesoura\033[m')
you = int(input('\033[34mDigite a sua escolha de acordo com os números do menu:\033[m '))
print ('\033[36mA máquina escolheu:\033[m',pc)
#________________CONDICTIONS_____________#
if you == 1 and pc == ('Pedra') or you == 2 and pc == ('Papel') or you == 3 and pc == ('Tesoura'): #Condição de empate
    print ('\033[32mHouve um empate!\033[m')
elif you == 1 and pc == ('Papel') or you == 2 and pc == ('Tesoura') or you == 3 and pc == ('Pedra'): #Condição de derrota
    print ('\033[31mVocê perdeu!\033[m')
elif you == 1 and pc == ('Tesoura') or you == 2 and pc == ('Pedra') or you == 3 and pc == ('Papel'): #Condição de vitória
    print ('\033[34mVocê ganhou!\033[m')
