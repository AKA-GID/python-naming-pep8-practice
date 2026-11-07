# Задание 5
# Приведите код в порядок. Не меняйте порядок вычислений и условия.

city_from = "Майкоп"
city_to = "Краснодар"
distance = 120
fuel_per_100 = 8.5
fuel_price = 62
people = 3
fuel_needed = distance * (fuel_per_100 / 100)
trip_cost = fuel_needed * fuel_price
cost_per_person = trip_cost / people
is_long_trip = distance > 100

print("Маршрут:",city_from,"—",city_to)
print("Расстояние:",distance)
print("Расход топлива:",fuel_needed)
print("Стоимость поездки:",trip_cost)
print("Стоимость на одного человека:",cost_per_person)
print("Дальняя поездка:",is_long_trip)
