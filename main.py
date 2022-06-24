import sys
count = 0
while(True):
  count+=1
  dap = 0
  L,P,V = map(int,sys.stdin.readline().split())
  if(L == 0 and P == 0 and V == 0):
    break
  dap += (V // P) * L
  if((V % P) > L):
    dap += L
  else:
    dap += V % P
  print("Case", count, end = "")
  print(": ", end = "")
  print(dap)