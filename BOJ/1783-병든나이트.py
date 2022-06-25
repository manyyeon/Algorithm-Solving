import sys
import math
N,M = map(int, sys.stdin.readline().split())
result = 1 # 출발점은 기본적으로 지나므로 최소 1

if(M == 1 or N == 1):
  print(result)
else:
  if(M >= 7):
    if(N >= 3):
      result += 2 + (M-5)
    else:
      result = 4
  else:
    if(N >= 3):
      if(M >= 4):
        result = 4
      else:
        result = M
    else:
      result = int(math.ceil(float(M)/2.0))
  print(result)