import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
  data.append(list(map(int, sys.stdin.readline().split())))

minArr = []
for i in range(N):
  minArr.append(min(data[i]))

print(max(minArr))