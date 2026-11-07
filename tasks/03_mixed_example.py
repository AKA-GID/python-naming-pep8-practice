# Задание 3. Переименуйте переменные по смыслу и правилам PEP 8.
# Не меняйте условия, формулы и порядок вычислений.

MIN_AGE = 14
MAX_AGE = 18

NAME = "Misha"
AGE_NOW = 16
SCORE_1 = 87
SCORE_2 = 92

average_score = (SCORE_1 + SCORE_2) / 2
can_join = AGE_NOW >= MIN_AGE and AGE_NOW <= MAX_AGE
passed = average_score >= 80

print("Участник:", NAME)
print("Средний балл:", average_score)
print("Подходит по возрасту:", can_join)
print("Прошёл отбор:", passed)
