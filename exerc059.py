while True:
    print ('\033[32mInsira dois números para usurfruir do programa\033[m')
    n1 = int (input('Digite o primeiro número: '))
    n2 = int (input('Digite o segundo número: '))
    sum = n1 + n2
    mult = n1 * n2
    both = n1, n2
    print ('Escolha uma das opções do menu digitando seu respectivo número:'
           '\n\033[33m[1]\033[m \033[34mSomar\033[m \n\033[33m[2]\033[m \033[34mMultiplicar\033[m \n\033[33m[3]\033[m \033[34mMaior\033[m \n\033[33m[4]\033[m \033[34mNovos números\033[m \n\033[33m[5]\033[m \033[34mSair do programa\033[m')
    choice = int(input('\033[36mDigite sua escolha de acordo com o menu:\033[m\n'))
    if choice == 5:
        break;
    elif choice == 1:
        print('Resultado da soma: {} + {} = {}'.format(n1, n2, sum))
        break;
    elif choice == 2:
        print('Resultado da multiplicação: {} x {} = {}'.format(n1, n2, mult))
        break;
    elif choice == 3:
        print('O maior número é {}\nE o menor número é {}'.format(max(both), min(both)))
        break;
    elif choice == 4:
        pass