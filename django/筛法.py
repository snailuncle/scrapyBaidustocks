import math
MAX_INT = 2000
marks_bool = [True] * (MAX_INT + 1)
# print(type(marks_bool), len(marks_bool), marks_bool)
for i in range(2, int(math.sqrt(MAX_INT)) + 1):
    j = i
    k = j
    while j * k <= MAX_INT:
        marks_bool[j * k] = False
        k += 1
sum_int = 0
for i in range(2, MAX_INT + 1):
    if marks_bool[i] is True:
        sum_int += 1
print(sum_int)
