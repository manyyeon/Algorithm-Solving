text = input()

stack = []
arr = []

numLen = 0
for i in range(len(text)):
  if(text[i] >= '0' and text[i] <= '9'):
    numLen += 1
    if(i == (len(text)-1)):
      j = i - numLen + 1
      numLen = 0
      num =""
      while(j <= i):
        num += text[j]
        j += 1
      stack.append(int(num))
      arr.append(sum(stack))
      stack = []
      if(len(arr) == 1):
        result = arr[0]
      else:
        result = 2*arr[0] - sum(arr)
  elif(text[i] == '+' or text[i] == '-'):
    j = i - numLen
    numLen = 0
    num =""
    while(j < i):
      num += text[j]
      j += 1
    stack.append(int(num))
    if(text[i] == '-'):
      arr.append(sum(stack))
      stack = []

print(result)