# Govinda Ramrattan
# My Integration Project

# Project:
# A text based story oriented RPG Game with choices that result in different endings.

#NOTE: All story paths have been planned. Every branch is currently being worked on, but none have been coded to an ending yet. 



import random


#Functions for the game to run
    

def outside_path():
    print("\nYou leave the cave. Outside of the cave you see that you are in dark forest. You notice that there is a path from the entrance to the cave that leads further into the forest. With no other option, you decide to follow it.")
    print("\nAfter keeping to the path for what feels like an eternity, you arrive at a quiet town in the middle of the woods. At first it seems barren, but you hear noise coming from a tavern in the center of town, the town's only source of light.")
    print("\n As you approach the tavern, you hear a whistling noise. You turn around to see a drunken jester trying to get your attention.\n1.See what the jester wants. \n2.Ignore the drunken jester and enter tavern.")
    outside_loop = True
    while outside_loop:
        command = input("\n> ")

        #Goes to the "jester" route
        if command == "1":
            outside_loop = False
            print("jester")
            #jester_path()  #Not coded yet

        #Goes to the "tavern" route
        elif command == "2":
            outside_loop = False
            print("tavern")
            #tavern_path() #Not coded yet
        else:
            print('Invalid response, type "1" or "2"')
            continue

        

def optional_puzzle():
    print('The gatekeeper explains the premise of his simple game. Guess what number he is thinking of. He explains the following rules:')
    print('\n"The number will be between 1 and 20. You will have five tries to guess the number. You will be told if your guess was higher or lower than the number."')
    print("The game begins now.\nGuess:")
    
#Uses for loop with relational operators
    answer = random.randrange(1, 20)
    guess_amount = 0
    for turn in range(5):
        try:   #stops the user from entering invalid inputs
            guess = int(input("> "))
        except:
            print("Please try guessing a whole number!")
            continue
        if guess == answer:
            break
        elif int(guess) > answer:
            print("Your guess was higher than the number.")
        elif (guess) < answer:
            print("Your guess was lower than the number.")
        guess_amount += 1
    if guess_amount < 5:
        print("\nCongrats you won.\n")
    elif guess_amount:
        print("\nSorry you lost.\n")
    print("The gatekeeper thanks you for playing his game. You now head into the city.")
    #enter_the_city() # Not coded yet
    
    


def puzzle_path(amulet): #<----Function that accepts the parameter received from the cave function. 
    if amulet:
        print("As the gate keeper is about to the begin the puzzle, he notices takes great notice from the amulet on your person. ")
    else:
       print('The gatekeeper gives you the following riddle:\n\n"This has a head and tail, but no body. It is a ________?"\nNOTE: You can guess as many times as you want, if your give up, type "quit".\nGuess:')
       puzzle_loop = True
       while puzzle_loop:
           command = input("> ")
           if command == "coin".lower():
               print('CORRECT!\nThe gate keeper explains that you are now able to enter the city, however he has an optional game to play if you are up for it.')
               print("\n\nChoices\n1.Play his game.\n2.Enter the city.")
               continue

        #Goes to the outside path
           elif command == "quit".lower():
               print("You quit attempting the gatekeeper's riddle. With no other option, you decide to leave the cave.\n")
               outside_path()

        #Goes to the optional puzzle function
           elif command == "1":
               print("puzzle")
               optional_puzzle()
               
        #Goes to the "enter the city" path
           elif command == "2":
               print("enter the city")
               #enter_the_city()
           else:
               print("Wrong! Try again.")
               continue 
                               

def cave_path():
    print("\nYou explore further into the cave filled with pillars and stalagmites. The amount of torches placed becomes more prevalent. As you walk through the cave you see a")      
    print("myterious glint of light from some rocks for a split second. Curious, you approach the rocks and notice there is an opening between the rocks.")
    print("You reach your hand in and find an amulet with a strange symbol on it.")
    print("Do you take it?\n\nChoices:\n1.Take it. I bet no one's coming back for it.\n2.Leave it. Someone probably stashed it here and will probably come back for it.")
    cave_loop = True
    while cave_loop:
        command = input("\n> ")
        
        #Player takes amulet
        if command == "1":
            cave_loop = False
            has_amulet = True
            print("\nYou took the amulet.\n.")
            
        #Player leaves amulet
        elif command == "2":
            cave_loop = False
            has_amulet = False
            print("\nYou decide not to take the amulet.\n")
        else:
            print('Invalid response, type "1" or "2"')
            continue
        
    print("As you continue to walk, you soon arrive at a large wooden gate built in the cave. An old man ")
    print("in rags, comes out from an opening in the gate. He explains that there is a society full of the brightest scholars and philosophers that live beyond the gate. But")
    print("to pass, you must answer his riddle, or leave.\n\nChoices:\n1.See if you can solve the riddle.\n2.I'm not smart enough for this, I'm leaving.")
    gate_loop = True
    while gate_loop:
        command = input("\n> ")

        #Goes to the "puzzle" route        
        if command == "1":
            gate_loop = False
            puzzle_path(has_amulet)  #Passes argument
            
            
        # Goes to the "outside" route
        elif command == "2":
            gate_loop = False
            outside_path()
        else:
            print('Invalid response, type "1" or "2"')
            continue
    

            
    
#Displays when game first begins
def game_has_started(): 
    print("\nYou awaken in the entrance of a dark cave, your memory hazy to the events that led up to your arrival here.\nLooking in the cave, you faintly see torches placed on the walls deep in the cave, indicating that someone has been there.")
    print("\nChoices:\n1.Your curiosity gets the best of you, you must investigate this mysterious cave.\n2.What a boring cave. I'm getting out of here.")
    game_loop = True
    while game_loop:
        command = input('Enter choice ("1" or "2") \n>')
          
        #Goes to the "cave" story route
        if command == "1":            
            game_loop = False
            cave_path()
        #Goes to the "outside" story route  
        if command == "2":
            game_loop = False
            outside_path()
        else:
            print("Invalid input, try again")
            continue
    
        
    

#Questions prompted to the player when they choose PLAY GAME
def ready_to_play():
    print("Are you ready to start your adventure?\nYes or No")
    ready_to_play_loop = True
    while ready_to_play_loop:
        command = input("> ")
        if command == "yes".lower():
            ready_to_play_loop = False
            game_has_started()
        elif command == "no".lower():
            print("Would you like to return to the main menu?\nYes or No")
            command = input("> ")
            if command == "yes".lower():
                return_menu_loop = False
                main_menu()
                menu_navigation()
            elif command == "no".lower():
                print("Are you ready to start your adventure?\nYes or No")
                continue
        else:
            print('Invalid command, try again') #if any undefined commands are inputed
            continue
                   

 

#Function that calls the Main Menu Screen
        
def main_menu():
    print("""
            WELCOME TO "SECRET OF THE GOLDEN EGG"    
                    PLAY GAME
                    GAME INFO
                     CREDITS
                    QUIT GAME
                     """)
    

def menu_navigation():
    main_menu_loop = True
    while main_menu_loop:
        command = input("> ") 
    # Code for quitting the game.
        if command == "quit game".lower() or command == "quit".lower():
            main_menu_loop = False
            print("You have exited the game.\nTHANKS FOR PLAYING")
            break
            #Stops the code
        

    # Code for the "CREDITS" section.
        elif command == "credits".lower():
            print("This game was created by Govinda Ramrattan.\nBACK")
            command = input("> ")
            if command == "back".lower():
                main_menu()
            else:
                print('Invalid command, enter "back" to return to the main menu') #if any undefined commands are inputed
                

    # Code for "GAME INFO" section.
        elif command == "game info".lower():
            #Game has no title
            print(
                '"SECRET OF THE GOLDEN EGG" is a text-based RPG Game. Follow your character in an \ninteractive journey where your choices affect the outcomes.\nTry and see if you can get all the endings!(Although only one ending makes the title make sense) Good Luck!\nBACK')
            command = input("> ")
            if command == "back".lower():
                main_menu()
            else:
                print('Invalid command, enter "back" to return to the main menu') #if any undefined commands are inputed
                

    # Code for "PLAY GAME" section.
        elif command == "play".lower() or command == "play game".lower():
            main_menu_loop = False
            print("\n")
            ready_to_play()
        elif command == "back".lower():
            main_menu()

            

#Main functions are called:

main_menu()
print("NOTE: input your commands and choices next to the > symbol.")
menu_navigation()




 
