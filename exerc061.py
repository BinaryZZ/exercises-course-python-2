first_term = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))
print ('A PA partindo do termo {} e da razão {} é a seguinte:' .format(first_term,reason))
print (first_term, end = ' -> ')
attempt = 0
value = 0
value = first_term
while attempt != 9:
    value += reason
    attempt += 1
    print (value, end = ' -> ')
    if attempt == 9:
        value += reason
        print (value)