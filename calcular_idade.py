from datetime import date

current_date = date.today()
data_nascimento = int(input("Ano de nascimento: "))
data_actual = current_date.year
idade = data_actual - data_nascimento

print('A sua idade atual é de ' + str(idade) + ' anos.')