r1 = int(input('Valor da primeira reta: ')) #valor 1
r2 = int(input('Valor da segunda reta: ')) #valor 2
r3 = int(input('Valor da terceira reta: ')) #valor 3

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1 : #se nao podem formar um triângulo
    print ('Esses valores não podem formar um triângulo!')
elif r1 == r2 and r1 == r3: # se o primeiro valor for igual ao segundo valor ou  o primeiro valor for igual ao terceiro valor
    print ('Equilatero')
elif r1 == r2 or r1 == r3 or r2 == r3: #se o primeiro valor for igual ao segundo valor ou o primeiro valor for igual ao segundo valor ou o segundo valor for igual ao terceiro valor
    print ('Isósceles')
else:
    print ('Escaleno')