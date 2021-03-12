# player_score = [1, 6, 2, 5]

# def lvp(score):
#     min = score[0]
#     for i in range(len(score)):
#         if score[i] < min:
#             min = score[i]
#     print(min)

# lvp(player_score)

# check if the input of a user matches the admin database

from modules.auth import security

admin = ["akash", "shay", "adio", "caz"]

    
security(admin)