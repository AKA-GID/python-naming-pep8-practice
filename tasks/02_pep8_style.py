
TAX_RATE = 0.2

product_name = "Книга"
product_price = 100
products_count = 2

subtotal=product_price * products_count
tax_amount=subtotal * TAX_RATE
final_price=subtotal+tax_amount

print("Товар:",product_name)
print("Количество:",products_count)
print("Итоговая стоимость:",final_price)
