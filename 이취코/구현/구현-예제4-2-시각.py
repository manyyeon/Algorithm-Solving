N = int(input())

result = 0
for i in range(N+1):
  if('3' in str(i)):
    result += 3600
  else:
    result += 1575