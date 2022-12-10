#Вводится кол-во строк, кол-во столбцов двумерного массива.
#Далее вводится двумерный массив.
#Необходимо все отрицательные элементы массива заменить на 0 и вывести новый массив.

rows, columns = map(int, input().split())
array = []
for i in range(rows):
  array.append(list(map(int, input().split())))
for i in range(rows):
  for j in range(columns):
    if array[i][j] < 0:
      array[i][j] = 0
for i in range(rows):
  print(array[i])