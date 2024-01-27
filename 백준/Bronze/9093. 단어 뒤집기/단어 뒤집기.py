import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n_list = input().split()
    for i in range(len(n_list)):
        n_list[i] = n_list[i][::-1]

    for i in n_list:
        print(i, end=" ")
