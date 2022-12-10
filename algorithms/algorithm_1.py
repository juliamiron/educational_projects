#Алгоритм Дейкстры
#Дан ориентированный взвешенный граф.
# Для него вам необходимо найти кратчайшее расстояние от вершины S до вершины F


vertices_number, start_vertex, final_vertex = map(int, input().split(" "))
graph_matrix = []
start_vertex = start_vertex - 1
final_vertex = final_vertex - 1
INF = float('inf')
for i in range(vertices_number):
  graph_matrix.append(list(map(int, input().split(" "))))
u = [0] * vertices_number
u[start_vertex] = 1
cost_way = [INF] * vertices_number
current = start_vertex
cost_way[start_vertex] = 0
while current != final_vertex and cost_way[current] != INF:
  for i in range(vertices_number):
    if u[i] == 0 and graph_matrix[current][i] != -1:
      cost_way[i] = min(cost_way[i], cost_way[current] + graph_matrix[current][i])
  min_cost = INF
  number = -1
  for i in range(vertices_number):
    if u[i] == 0 and cost_way[i] <= min_cost:
      number = i
      min_cost = cost_way[i]
  current = number
  u[current] = 1
print(cost_way[final_vertex])
