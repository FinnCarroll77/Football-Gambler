balance = 100

import random
print ("Welcome to Football Gambler")
while True:
    yes = input ("if you would like to play type play if you would like to quit press Q ")
    
    if yes == "play":
        break
    
    elif yes == "Q":
        print ("The game will now quit. ")
        
    else:
        print ("Please retry")
while True:
    while True:
        # Team 1 random variable       
        team1 = random.choice (["Manchester Utd", "Newcastle Utd", "Luton Town","Aston Villa", "Liverpool", "Manchester City ", "Arsenal", "Tottenham Hotspur", "West Ham United","Chelsea FC","Brentford","Dorking Wanderers"])

        # Team 2 random variable
        team2 = random.choice (["Manchester Utd", "Newcastle Utd", "Luton Town","Aston Villa", "Liverpool", "Manchester City ", "Arsenal", "Tottenham Hotspur", "West Ham United","Chelsea FC","Brentford","Dorking Wanderers"])
    
        if team1 != team2:
            break
    
    while True:
        bet = int(input("How much would you like to bet? "))
    
        if bet > 100:
            print ("Please try again your max bet is £100")
        
        if bet <= 100:
            break
    


    team1score = random.randint (1, 10)
    team2score = random.randint (1, 10)


    guess = int(input("The two teams are, " + team1 + " and " + team2 + ". Who do you think will win. (1, 2) "))
    
    if guess == 1:
        
        if team1score > team2score:
            print ("You won! the score was, " + team1 + " " + str(team1score) + " and " + team2 + " " + str(team2score) + "!  ")
            balance = balance + bet
            print (balance)
        elif team2score > team1score:
            print ("You lost! the score was, " + team1 + " " + str(team1score) + " and " + team2 + " " + str(team2score) + "!  ")
            balance = balance -bet 
            print (balance)
    elif  guess == 2:
        
        if team1score > team2score:
            print ("You lost! the score was, " + team1 + " " + str(team1score) + " and " + team2 + " " + str(team2score) + "!  ")
            balance = balance -bet 
            print (balance)
            
        elif team2score > team1score:
            print ("You won! the score was, " + team1 +  " " + str(team1score) + " and " + team2 + " " + str(team2score) + "!  ")
            balance = balance + bet
            print (balance)

