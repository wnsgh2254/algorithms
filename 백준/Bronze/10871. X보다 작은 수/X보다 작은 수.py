import sys
input = sys.stdin.readline

n,x = map(int, input().split())
a = list(map(int,input().split()))

result = ""

for i in a:
    if x > i:
        result += str(i)+" "

print(result)