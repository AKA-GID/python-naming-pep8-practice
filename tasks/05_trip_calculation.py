# Задание 5
# Приведите код в порядок. Не меняйте порядок вычислений и условия.

CITY_FROM = "Майкоп"
CITY_TO = "Краснодар"
DISTANCE = 120
FUEL_PER_100 = 8.5
FUEL_PRICE = 62
PEOPLE = 3
fuel_needed = DISTANCE * FUEL_PER_100 / 100
trip_cost = fuel_needed * FUEL_PRICE
cost_per_person = trip_cost / PEOPLE
is_long_trip = DISTANCE > 100

print("Маршрут:", CITY_FROM, "—", CITY_TO)
print("Расстояние:", DISTANCE)
print("Расход топлива:", fuel_needed)
print("Стоимость поездки:", trip_cost)
print("Стоимость на одного человека:", cost_per_person)
print("Дальняя поездка:", is_long_trip)
