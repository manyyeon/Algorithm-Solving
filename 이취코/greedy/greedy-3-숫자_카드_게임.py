import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
  data.append(list(map(int, sys.stdin.readline().split())))

print(data)