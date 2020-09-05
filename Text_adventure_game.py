print("Welcome to my first game!") #print the welcome statement.

name = input("What is your name? ") #input of the name
age = int(input("What is your age? ")) #input of the age.

print("Hello {}, you are {} years old.".format(name, age)) #formatting the string.

health = 10 #a variable that counts the health of the player or the user

if age >= 18: #checking whether the player is more than 18
    print("You are old enough to play.".format(name)) #then they are old enough to play.
    wants_to_play = input("Do you want to play? ").lower().strip() # input for asking whethter they are ready to play
    if wants_to_play == "yes": #checking whether the answer is yes 
        print("You are starting with {} health.".format(health)) #then the health statement will be printed.
        print("Let's play") # and this statement will be printed in the following.

        first_choice = input("Do you wanna go left or right (left/right)? ").lower().strip() #asking for another choice for left or right
        if first_choice == "left": #if they want to go to the left.
            ans = input("Nice, you follow the path amd reach a lake.. Do you swim across or go around (across / around)? ").lower().strip()
            #then this input function to ask them that they got into a crossroad and which way they want to choose.
            
            if ans == "around": #if they player choose to go around
                print("You managed to get around and reached the other side of the lake.") #then print this statement.
                
                
            elif ans == "across": #if the player choose to go across
                print("You managed to get across and got beaten by a danderous crocodile and you lost 5 health.")#then print this statement
                health = health - 5 #and health reduce by 5.

            ans = input("You notice a house and a river. which do you go to (river/house)? ").lower().strip()# another chooice whether river or house.
            if ans == "house": # if the player choose to go to the house 
                print("You go to the house and are greeted by the owner... He does not like you and you loss 5 health.") #then print the statement.
                health = health - 5 #and health reduce by 5.

                if health <= 0: #if health is 0 or less than 0 
                    print("You now have 0 health and you lost the game...")#then print the statement and the player lost the game.

                else: #if health more than 0 
                    print("You have survived.. you win!")#then print the statement that you have survived the game and you win the gaem.
            else: #if you choose to go the river
                print("you fell in the rive and lost the game. ")#then print the statement that you fall in the river and you lost the game.

        else: #if you choose to go to the right
            print("You fell down and lost the game.") #then you fall down and lost the game.

    else:
        print("Cya...")

else:# your age is less than 18
    print("I am sorry {} you are not old enough to play.".format(name)) #so you are not allowed to play.
    
