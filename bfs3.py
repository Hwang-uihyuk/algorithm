n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)

for j in data:
    print(j, end =" ")