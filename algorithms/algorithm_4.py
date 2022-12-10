#Имеется N камней с разными весами P. Необходимо найти набор камней с максимальным суммарным весом,
#не превосходящим W.
#Необходимо решить задачу используя динамическое программирование.

N = int(input())
W = int(input())

weight = list(map(int, input().split()))

D = [[0] * (W+1) for i in range(N+1)]
for i in range(1, N+1):
  for j in range(1, W+1):
    if j - weight[i-1] < 0:
      D[i][j] = D[i-1][j]
    else:
      D[i][j] = max(D[i-1][j], weight[i-1] + D[i-1][j-weight[i-1]])
ans = []

i = int(N)
j = int(W)

while(D[i][j] != 0):
  if D[i-1][j] == D[i][j]:
    i = i - 1
  else:
    ans.append(weight[i-1])
    j = max(0, j - weight[i - 1])
    i = i - 1

print(D[N][W])
print(len(ans))
for i in range(len(ans) - 1, -1, -1 ):
  print(ans[i], end=' ')