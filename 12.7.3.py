per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money=float(input("Введите сумму"))

list_of_rates=list(per_cent.values())

deposit=[i*money*0.01 for i in list_of_rates]

print(deposit)

a=max(deposit)
print("Максимальная сумма, которую вы можете заработать —", a)