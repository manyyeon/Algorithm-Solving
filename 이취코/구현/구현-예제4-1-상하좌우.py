import sys

N = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x,y= 1,1
for plan in plans:
  for i in range(len(move_types)):
    if(plan == move_types[i]):
      nextX = x + dx[i]
      nextY = y + dy[i]
  if(nextX < 1 or nextX > N or nextY < 1 or nextY > N):
    continue
  x, y = nextX, nextY

print(x,y)