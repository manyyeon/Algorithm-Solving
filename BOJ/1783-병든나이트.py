import sys
import math
N,M = map(int, sys.stdin.readline().split())

if(M == 1 or N == 1):
  print(1)
elif(N == 2):
  print(min(4, int(math.ceil(float(M)/2.0))))
else:
  if(M >= 7):
    print(1 + 2 + (M-5))
  else:
    print(min(4,M))