# player_score = [1, 6, 2, 5]

# def total(scores):
#     sum = 0
#     for i in range(len(scores)):
        
#         sum = sum + scores[i]
        
#     print(sum)
    
    
# total(player_score)

# aList = [4, 6, 8]

# getmax = sum(aList)

# print(getmax)

player_score = [1, 6, 2, 5]

def mvp(score):
    max = 0
    for i in range(len(score)):
        if score[i] > max:
            max = score[i]
    print(max)

mvp(player_score)