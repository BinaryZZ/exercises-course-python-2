number_to_convert= int(input('Digite o valor a ser convertido: ')) #valor a ser convertido
print ('Bem vindo ao TRIPLE CONVERSOR!!!\n' #Apresentação de conversões e menu
       'para converter apenas digite uma das opções\n'
       '-\033[34m1\033[m para \033[33mbinário\033[m\n'
       '-\033[34m2\033[m para \033[33moctal\033[m\n'
       '-\033[34m3\033[m para \033[33mhexadecimal\033[m')
option_menu= int(input('Selecione uma opção digitando o respectivo numero: ')) #Seleção de conversão, item menu

if option_menu ==1: #Se selecionar a opção 1
    print(bin(number_to_convert))
elif option_menu ==2: #se selecionar a opção 2
    print(oct(number_to_convert))
elif option_menu ==3: #se selecionar a opção 3
    print(hex(number_to_convert))
else: #se digitar qualquer outra coisa além dos nums 1,2,3
    print ('Apenas digite um valor de 1 a 3')