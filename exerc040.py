#_____________VARIABLES_____________#

grade_equal1 = float(input('Digite a primeira nota: ')) #Receber nota 1
grade_equal2 = float(input('Digite a segunda nota: ')) #Receber nota 2
average_grade = float(grade_equal1 + grade_equal2) / 2 #Calcular a media

#____________CONDITIONS_________#
print ('Suas notas foram {:.1f} e {:.1f} portanto sua média e de {:.1f}' .format(grade_equal1,grade_equal2,average_grade))
if average_grade < 5.0: # se a nota for menor qu e5
    print ('\033[31mInfelizmente você foi reprovado ;(\033[m')
elif average_grade >= 5.0 and average_grade <= 6.9: # se a nota for entre 5 e 6.9
    print ('\033[33mVocê ficou de recuperação ;( faltou um pouquinho de atenção a mais nas aulas!\033[m')
elif average_grade >= 7.0: # se a nota for igual ou maior a 7
    print ('\033[32mParabéns! você foi aprovado!\033[m')

