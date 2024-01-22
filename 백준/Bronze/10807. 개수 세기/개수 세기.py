import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
v = int(input())
result = 0

for i in nums:
    if i == v:
        result+=1
print(result)

