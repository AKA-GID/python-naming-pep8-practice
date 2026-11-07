# Задание 4
# Приведите код в порядок. Результат работы программы должен остаться прежним.

client_name = "Мария"
item_name= "Наушники"
price = 3490
quantity = 2
discount = 0.1
subtotal = price*quantity
discount = subtotal*discount
total_to_pay = subtotal-discount

print("Покупатель:",client_name)
print("Товар:",item_name)
print("Стоимость без скидки:",subtotal)
print("Размер скидки:",discount)
print("К оплате:",total_to_pay)
