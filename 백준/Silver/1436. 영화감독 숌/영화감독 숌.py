import sys
input = sys.stdin.readline

n = int(input())

num = 666
count = 0
while True:
    if '666' in str(num):
        count += 1
        if count == n:
            break
    num += 1

print(num) 