# Задание 4
# Приведите код в порядок. Результат работы программы должен остаться прежним.

CLIENT = "Мария"
ITEM = "Наушники"
PRICE = 3490
QUANTITY = 2
DISCOUNT = 0.1
sum_1 = PRICE * QUANTITY
sum_2 = sum_1 * DISCOUNT
sum_3 = sum_1 - sum_2

print("Покупатель:", CLIENT)
print("Товар:", ITEM)
print("Стоимость без скидки:", sum_1)
print("Размер скидки:", sum_2)
print("К оплате:", sum_3)
