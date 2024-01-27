import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    work = input().split()
    if work[0] == 'push':
        n_list.append(work[1])
    elif work[0] == 'top':
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list[-1])
    elif work[0] == 'size':
        print(len(n_list))
    elif work[0] == 'empty':
        if len(n_list) == 0:
            print(1)
        else:
            print(0)
    elif work[0] == "pop":
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list[-1])
            n_list.pop()