import random

def draw_card():
    return random.randint(1, 13)


# hand = [1, 5, 11]
def list_sum(hand):
    sum = 0
    
    for i in range(len(hand)):
        sum = sum + hand[i]

    return sum






if __name__ == '__main__':
    dealers_hand = []
    dealer_bust = False
    dealers_sum = 0
    
    players_hand = []
    player_bust = False
    players_sum = 0
    
    while(not dealer_bust and not player_bust):
    
        user_input = int(input("Do you want to hit(1), or stick(0)"))
        
        if user_input == 1:
            print("You selected hit!")
            players_hand.append(draw_card())
            players_sum = list_sum(players_hand)
            print(players_hand, "\tTotal:", players_sum)
        else:
            break
         
        
        
        
        if player_bust:
            print("Player busted! House wins!")
        elif dealer_bust:
            print("House busts! Player wins!")
            
    
        
        