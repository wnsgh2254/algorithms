import sys
input = sys.stdin.readline

N = int(input())
cnt = N

for i in range(N):
    word = input()
    # if len(word) <= 2:
    #     continue
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)