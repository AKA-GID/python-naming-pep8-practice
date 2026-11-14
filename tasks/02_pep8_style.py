
TAX_RATE = 0.2

PRODUCT_NAME = "Книга"
PRODUCT_PRICE = 500
COUNT_OF_PRODUCTS = 2

total_price = PRODUCT_PRICE * COUNT_OF_PRODUCTS
tax = total_price * TAX_RATE
final_price = total_price + tax

print("Товар:", PRODUCT_NAME)
print("Количество:", COUNT_OF_PRODUCTS)
print("Итоговая стоимость:", final_price)
