# Задание 3. Переименуйте переменные по смыслу и правилам PEP 8.
# Не меняйте условия, формулы и порядок вычислений.

min_age = 14
max_age=18

name = "Misha"
age = 16
first_score = 87
second_score = 92

average = (first_score+second_score)/2
can_join = age >= min_age and age <= max_age
passed = average >= 80

print("Участник:",name)
print("Средний балл:",average)
print("Подходит по возрасту:",can_join)
print("Прошёл отбор:",passed)
