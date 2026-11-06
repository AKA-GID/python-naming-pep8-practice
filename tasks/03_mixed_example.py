# Задание 3. Переименуйте переменные по смыслу и правилам PEP 8.
# Не меняйте условия, формулы и порядок вычислений.

MIN_AGE = 14
MAX_AGE=18

u = "Misha"
ageNow = 16
score1 = 87
score2=92

averageScore=(score1+score2)/2
canJoin = ageNow >= MIN_AGE and ageNow <= MAX_AGE
passed = averageScore >= 80

print("Участник:",u)
print("Средний балл:",averageScore)
print("Подходит по возрасту:",canJoin)
print("Прошёл отбор:",passed)
