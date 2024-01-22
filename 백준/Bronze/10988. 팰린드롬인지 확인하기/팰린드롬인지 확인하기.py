import sys
input = sys.stdin.readline

a = input().strip()
print(1 if a==a[::-1] else 0)