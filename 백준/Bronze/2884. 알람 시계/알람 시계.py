import sys
input = sys.stdin.readline

a ,b = map(int, input().split())

if b >= 45:
    print(a, b-45)
elif a > 0 and b < 45:
    print(a - 1, b + 15)
else:
    print(23, b+15)



