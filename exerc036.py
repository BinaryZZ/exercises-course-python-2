#________________DATAS_TO_COLLECT___________________#
house_value= int(input('Enter the house value: ')) #Valor do imóvel
salary = int(input('Enter the salary value: ')) #Salário
years_of_payment= int(input('Enter in how many years you intend to repay the loan: ')) #Anos de pagamento

#____________________ALGORITHM______________________#

house_payments= house_value/(years_of_payment*12) #Valor mensal do empréstimo
approve = salary*0.30 #Cálculo para pegar 30% do valor do salário

#____________________CONDITIONS_____________________#
if house_payments <= approve: #Se o valor da mensalidade for igual ou menor a 30% do salário
    print ('Seu empréstimo foi aprovado!')

elif house_payments > approve:
    print ('Seu empréstimo foi negado, infelizmente você não pode financiar esta casa!') #se o valor da mensalidade for maior que 30% do salario
