#От вас требуется определить вес минимального остовного дерева
#для неориентированного взвешенного связного графа.

vertices_n, edges_m = map(int, input().split(' '))
edges = []
for n in range(edges_m):
  f, s, w = map(int, input().split(' '))
  edges.append([w, f -1, s -1])
edges.sort()
c = list(range(vertices_n))
s = 0
for m in range(edges_m):
  if c[edges[m][1]] != c[edges[m][2]]:
    s = edges[m][0] + s
    c1 = edges[m][1]
    c2 = edges[m][2]
    for i in range(len(c)):
      if c[i] == c1:
        c[i] = c2
print(s)