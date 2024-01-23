import sys
input = sys.stdin.readline

words = []
for i in range(5):
    word = input().strip()  
    words.append(word)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')



