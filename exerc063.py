n1 = 0 # Receber sequencia
prev_result = 0 # Receber valor anterior
attempt = 1 # Recebe tentativas
ivalue = 1 # Recebe novo valor
quitprogram = 0 # Opcao de saida do programa
while True:
    if attempt == 1: # Se tentativas for igual a 1
        if attempt == 1 and quitprogram == 1: # Se tentativas for igual a 1 e a opcao de saida do programa for igual a 1
            keep = str(input('\nVocê quer continuar? pra sim digite qualquer letra, e para nao digite N:\n')) # Recebe resposta se quer continuar
            if keep.lower() == 'n': # se a resposta for nao
                break; # parar
        n1 = int(input('\nDigite a quantidade da sequência desejada em número:\n')) #recebe a sequencia
        attempt = n1+1 # adiciona sequencia recebida +1 para tentativa

    elif attempt >= 0 != n1: # Se tentativa for maior ou igual a zero e diferente de sequencia
        result = ivalue + prev_result # Resultado recebe a soma de novo valor + valor anterior
        prev_result = ivalue # Recebe valor 'anterior'
        ivalue = result # Recebe resultado da soma
        print (result, end = ' => ')
        attempt += -1 # diminui uma tentativa
        quitprogram = 1 # aumenta 1 na opcao de saida do programa

    elif attempt == 0: # se tentativa for igual a zero
        break;