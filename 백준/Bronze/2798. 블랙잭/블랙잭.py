import sys
input = sys.stdin.readline

n,m = map(int, input().split())

card = list(map(int, input().split()))

max_num = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            temp = card[i]+card[j]+card[k]
            if temp > m:
                continue
            else:
                max_num = max(max_num, temp)

print(max_num)