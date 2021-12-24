phrase = str(input('Digite uma frase: ')) # Recebe a frase
phrase_preparate = phrase.lower().replace(' ','') # Tira espaços e deixa em minúsculo\ trata a frase
phrase_inverse = phrase_preparate[::-1] # Deixa a palavra invertida
print (phrase_preparate,phrase_inverse) # Mostrar as frases
if phrase_preparate == phrase_inverse: # Se a frase tratada for igual a frase inversa
    print ('A frase {} é um palíndromo!' .format(phrase))
elif phrase_preparate != phrase_inverse: # se a frase tratada for diferente da inversa
    print ('A frase {} não é um palíndromo!' .format(phrase))
