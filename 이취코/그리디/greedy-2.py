import sys
N,M,K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

dap = 0
if(arr[0] == arr[1]):
  dap += arr[0] * M
else:
  dap += ((arr[0] * K) + arr[1]) * (M // (K+1))
  dap += arr[0] * (M % (K+1))

print(dap)