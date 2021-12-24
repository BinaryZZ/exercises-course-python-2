first_term = int(input('Digite o primeiro termo: ')) # Recebe o primeiro termo
reason = int(input('Digite a razão: ')) # recebe a razão
print ('A PA partindo do termo {} e da razão {} é a seguinte:' .format(first_term,reason))
attempt = 0 # Recebe tentativas
value = 0 # recebe valor do termo + razao
attempt2 = 0 # recebe as tentativas2
while attempt != 9: # Loop en quanto tentativas for diferente de 9
    value += first_term + reason # valor recebe termo + razao
    print (value, end = ' -> ')
    attempt += 1 # tentativas recebe +1
    if attempt == 9: # Se for igual a 9
        value += first_term + reason # valor recebe termo + razao
        print (value)
        ex = str(input('Você deseja sair? digite S ou Y pra sim ou qualquer letra pra não: \n')) # Opcao de parada do programa
        if ex.lower() == ('s') or ex.lower() == ('y'): # se a resposta for s ou y
            break; # parar

attempt2 += int(input('Mais quantos termos você quer ver? Digite um número: \n')) # tentativas 2 recebe valor
while attempt2 != 0: # enquanto tentativas2 for diferente de zero
    value += first_term + reason # valor recebe termo + razao
    print(value, end=' -> ')
    attempt2 += -1 # tentativa2 recebe -1
    if attempt2 == 0: # se tentativa 2 for igual a 0
        ex = str(input('\nVocê deseja sair? digite S ou Y pra sim ou qualquer letra pra não: \n')) # opcao de parada
        if ex.lower() == ('s') or ex.lower() == ('y'): # se a resoista for s ou y
            break; # parar
        else: # se a resposta for diferente de s ou y
            attempt2 += int(input('Mais quantos termos você quer ver? Digite um número: \n')) # opcao de ver mais termos
            pass # retornar o loop