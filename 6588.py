import dataclasses
import sys

num = 10
data = [True for _ in range(num)]

for i in range(2, int((num-1)**0.5) + 1) :
  if data[i] :
    for j in range(i + i, num, i) : #data[4]부터 false로 바귄다. data[짝수]
      data[j] = False
 
while True :
  n = int(sys.stdin.readline())
  
  if n == 0 :
    
    break
  
  count = 0
  for i in range(3, len(data)) :
    if data[i] and data[n-i] :

      print(str(n) + " = " + str(i) + " + " + str(n-i))
      count = 1
      break

  if count == 0 :
    print("Goldbach's conjecture is wrong.")