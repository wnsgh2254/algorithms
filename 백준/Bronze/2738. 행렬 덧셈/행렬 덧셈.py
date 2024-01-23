import sys
input = sys.stdin.readline

a,b = map(int, input().split())

a_a = []
a_b = []

for i in range(a):
    arr = list(map(int, input().split()))
    a_a.append(arr)

for i in range(a):
    arr = list(map(int, input().split()))
    a_b.append(arr)

for i in range(a):
    for j in range(b):
        print(a_a[i][j] + a_b[i][j], end=" ")
    print()