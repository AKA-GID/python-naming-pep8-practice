
TAX_RATE = 0.2

productName = "Книга"
product_price=500
countOfProducts = 2

totalPrice=product_price*countOfProducts
tax=totalPrice*TAX_RATE
finalPrice=totalPrice+tax

print("Товар:",productName)
print("Количество:",countOfProducts)
print("Итоговая стоимость:",finalPrice)
