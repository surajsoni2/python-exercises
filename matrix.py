m = int(input())
n = int(input())

result = []

for i in range(m):
    a = []
    for j in range(n):
        a.append(i*j)
    result.append(a)

for i in range(m):
    print(result[i])