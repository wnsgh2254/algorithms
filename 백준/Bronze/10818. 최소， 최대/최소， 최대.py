import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

small = min(a)
large = max(a)

print(str(small)+" "+ str(large))