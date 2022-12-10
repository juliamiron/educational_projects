#Проверить прямые пересикаются или нет, найти точку пересечения

k1 = int(input())
b1 = int(input())
k2 = int(input())
b2 = int(input())
if k1==k2 and b1==b2:
  print('Совпадают')
elif k1==k2:
  print('Параллельны')
else:
  print('Пересекаются')
  X=(b2-b1)/(k1-k2)
  y=k1*X + b1
  print(X, y)