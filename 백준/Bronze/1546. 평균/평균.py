import sys
input = sys.stdin.readline

num = int(input())
total_score = 0
score_list = list(map(int, input().split()))

for i in range(len(score_list)):
    total_score += score_list[i]/max(score_list)*100

print(total_score/num)

