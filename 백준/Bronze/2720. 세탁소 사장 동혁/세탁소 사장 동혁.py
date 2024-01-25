import sys
input = sys.stdin.readline


q = 0
d = 0
n = 0
p = 0


a = int(input())

for _ in range(a):
    money = int(input())
    q = money // 25
    money = money%25
    d = money // 10
    money = money%10
    n = money // 5
    money = money%5
    p = money // 1
    print(str(q)+" "+str(d)+" "+str(n)+" "+str(p))