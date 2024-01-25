import sys
input = sys.stdin.readline

num = int(input())

num_beehouse = 1
count = 1

while num > num_beehouse:
    num_beehouse += 6 * count
    count += 1

print(count)