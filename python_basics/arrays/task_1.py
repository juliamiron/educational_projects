#Вводится кол-во строк, кол-во столбцов двумерного массива.
#Далее вводится двумерный массив.
#Необходимо вывести сумму всех элементов этого двумерного массива.

rows, columns = map(int, input().split())
array = []
s = 0
for i in range(rows):
  array.append(list(map(int, input().split())))
for i in range(rows):
  for j in range(columns):
    s = array[i][j] + s
print(s)
