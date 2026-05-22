n = int(input("dimension: "))

print("first matrix:")
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

print("second matrix:")
B = []
for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for row in C:
    print(" ".join(map(str, row)))
