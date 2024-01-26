import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in str(n):
    n_list.append(int(i))
n_list.sort(reverse=True)

for i in n_list:
    print(i, end="")