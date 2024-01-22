import sys
input = sys.stdin.readline

s = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(x), end = ' ')