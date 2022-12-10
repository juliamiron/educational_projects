# Алгоритм Флойда
#Полный ориентированный взвешенный граф задан матрицей смежности.
# Постройте матрицу кратчайших путей между его вершинами.
# Гарантируется, что в графе нет циклов отрицательного веса.

vertices_number = int(input())
graph_matrix =  []
INF = float('inf')
for i in range(vertices_number):
  s = input().split(' ')
  if s[-1] == '':
    s = s[:-1]
  graph_matrix.append(list(map(int, s)))

for current in range(vertices_number):
  for i in range(vertices_number):
    for j in range(vertices_number):
      graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[i][current] + graph_matrix[current][j])

for i in range(vertices_number):
  for j in range(vertices_number):
    print(graph_matrix[i][j], end = ' ')
  print()