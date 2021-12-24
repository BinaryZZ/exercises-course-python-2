from random import randint # Importando biblioteca
attempt = 0 # tentativa
while True: # repetição
    pc = randint(0, 10) # escolha aleatória
    pl = int (input ('Tente adivinhar o número de 0 a 10: ')) # recebe numero
    attempt += 1 # adiciona +1 na tentativa
    if pl == pc and attempt >1: # se o numero recebido for igual ao do pc e maior que uma tentativa
        print ('\033[33mSua numero é {}\033[m \n\033[32mEu pensei no número {}\033[m\n\033[34mParabéns! você venceu :))\033[m\nForam necessárias {} tentativas para sua vitória! ' .format(pl, pc,attempt))
        break; # parar
    elif pl == pc and attempt == 1: # se o numero recebido for igual ao do pc e em uma tentativa
        print(
            '\033[33mSua numero é {}\033[m \n\033[32mEu também pensei no número {}\033[m\n\033[34mParabéns! você venceu :))\033[m\nFoi necessária {} tentativa para sua vitória! '.format(pl, pc, attempt))
        break;
    elif pl != pc: # se o numero recebido for diferente do numero do pc
        print ('\033[33mSua numero é {}\033[m \n\033[32mEu pensei no número {}\033[m\n\033[31mVocê perdeu! mais sorte na próxima :((\033[m' .format(pl, pc))