# Задание 4
# Приведите код в порядок. Результат работы программы должен остаться прежним.

client = "Мария"
item = "Наушники"
price = 3490
quantity = 2
discount = 0.1
sum1 = price * quantity
sum2 = sum1 * discount
sum3 = sum1 - sum2

print("Покупатель:",client)
print("Товар:",item)
print("Стоимость без скидки:",sum1)
print("Размер скидки:",sum2)
print("К оплате:",sum3)
