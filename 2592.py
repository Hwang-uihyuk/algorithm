data = []
for i in range(10):
    data.append(int(input()))



print(int(sum(data)/10))
print(max(data, key = data.count))
    