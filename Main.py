"""Project: A text based story oriented RPG Game with choices that result in
different endings. Titled: "SECRET OF THE GOLDEN EGG" """

__author__ = "Govinda Ramrattan"

import random


# Functions for the game to run

def return_to_main():
    """The function allows the player to return to the main menu after getting
to an ending."""
    print('\nType "menu" to return to the main menu')
    return_loop = True
    while return_loop:
        command = input("> ")
        if command == "menu".lower():
            return_loop = False
            main_menu()
            menu_navigation()
        else:
            continue


def dead_ending():
    """This function brings the player to the scene containing the "Dead
    Ending. They return to the main menu after this." """
    print(
        '\nYou confidently stand proud as the dragon returns to the next, '
        'as you hope your super secret"chosen one powers" awaken.\n\nThey '
        'don\'t\n\n ')
    print("The dragon eats you... You Died.")
    print("\n\nYou have achieved the \"DEAD ENDING.")
    return_to_main()


def winner_ending():
    """This function brings the player to the scene containing the "Winner
    Ending". They return to the main menu after this. """
    print(
        "\nWith quick wit, you decide to hide in the nest with the eggs. The "
        "dragon returns to the nest but doesn't notice you. After five "
        "minutes, ""the dragon")
    print(
        "leaves the nest. You take this time to retrieve the egg and return "
        "it to the village.\n\n The villagers consider you a hero, "
        "as ownership of this egg")
    print(
        "has allowed them to create medicines to heal a plethora of "
        "diseases, ushering in a new age of medicine, healing people across "
        "the globe.")
    print('\n\nYou have achieved the "HERO ENDING.')
    return_to_main()


def chosen_one():
    """Brings the player to the "Chosen One" scene. They can be directed to
    the Winner Ending or Dead Ending. """
    print(
        "\nThe scholars tell you about a golden egg that they wish to study. "
        "They say that its rare composition makes it so they can create a wide"
        " array of medicines.")
    print(
        "They lead you to the outskirts of their city where they there is a "
        "large nest. They say there is a dragon that has killed every person "
        "who has tried to obtain the egg.")
    print(
        "\nYou approach the empty nest and attempt the grab the egg when you "
        "hear the roar of the dragon. Its returning to the nest.")
    print("What will you do?\n1.Confront the Dragon. \n2. Hide in the nest.")
    chosen_loop = True
    while chosen_loop:
        command = input("> ")
        # Goes to the "Dead" ending
        if command == "1":
            chosen_loop = False
            dead_ending()
        elif command == "2":
            # Goes to the "Winner" ending
            chosen_loop = False
            winner_ending()
        else:
            print("Invalid input, try again")
            continue


def scholar_ending():
    """This function brings the player to the scene containing the "Scholar
    Ending. They return to the main menu after this."""
    print(
        "\nUnderstanding that its a title that holds a lot of responsibility, "
        "the villagers understand your decision. With your intelligence "
        "proven from solving")
    print(
        "the gatekeeper's puzzle, the scholars offer to allow you to stay in "
        "the village and live with them. They teach you everything they know "
        "and you become a genius.")
    print('\n\nYou have achieved the "SCHOLAR ENDING."')


def enter_the_city():
    """Brings the player to the "Enter the City" scene. They can be directed to
        the Scholar Ending or The Chosen one scene. """
    print(
        "\nAs you head past the gate, you are lead into a tunnel leading"
        " underground. After following the tunnel for sometime, you arrive"
        " at a big opening revealing an underground city located in a large "
        "cavern in the cave\n")
    print(
        'You see a bunch of men and women exit their stone huts and they all '
        'congregate around you. "They seem quite astonished",  you think to '
        'yourself.\n')
    print(
        "The crowd then makes room for someone who seems like an ordinary "
        "old man. He approaches you and explains that he is the village "
        "elder, and the villagers\nhave been waiting 100 years for an "
        "outsider to come the village.")
    print(
        "He tells you that the village scholars have discovered a prophecy "
        "and I seem like someone to fulfill it.")
    print(
        'Do you become the village\'s "chosen one"?\n\nChoices:\n1. You want '
        'to become the chosen one.\n2. You do NOT want to become the chosen '
        'one.')
    city_loop = True
    while city_loop:
        command = input("> ")
        # Goes to the "Chosen one" route.
        if command == "1":
            city_loop = False
            chosen_one()
        elif command == "2":
            # Goes to the "Scholar" ending
            city_loop = False
            scholar_ending()
        else:
            print("Invalid input, try again")
            continue


def jester_ending():
    """This function brings the player to the scene containing the "Jester
    Ending. They return to the main menu after this."""
    print(
        "\nThe jester brings you inside, and says he wants to reward you for "
        "helping him. He gives you many items to name, including gold and "
        "weird trinkets.\nYou leave the house.")
    print(
        "\nOn your way back to the tavern, you are stopped by the patrolling "
        "guards who are curious about the large sack you have that are "
        "carrying your new items.")
    print(
        "The guards decide to check your items, and accuse you of robbing "
        "the mayor's house, claiming you have some of his prized "
        "possessions and trinkets.")
    print(
        "You try to explain that you were manipulated by the jester"
        " but they don't believe you.\nYou are arrested.\n\nYou have "
        "achieved the PRISONER ENDING.")
    return_to_main()


def tavern_ending1():
    """This function brings the player to the scene containing the "Tavern
        Ending #1. They return to the main menu after this."""
    print("You decide to get involved by trying to talk one of the men out "
          "of fighting. In a drunken rage, he punches you out cold.\nYou are"
          "knocked unconscious.\n\nYou have achieved the KNOCKED OUT ENDING.")
    return_to_main()


def tavern_ending2():
    """This function brings the player to the scene containing the "Tavern
    Ending #2. They return to the main menu after this."""
    print("After about a minute of yelling, it seems the two men calm down. "
          "You get to enjoy your time at the tavern, you eat, drink and even "
          "make new friends. You learn about the town and something about a "
          "fabled \"golden egg\". You look forward to possibly trying to "
          "find it, and you settle down for the night.\n\nYou have achieved "
          "the PLEASANT ENDING.")
    return_to_main()


def tavern_path():
    """Brings the player to the "Tavern" path. They can be directed to
        Tavern Ending #1 or Tavern Ending #2. """
    print("You enter the tavern and look around. The tavern is packed with "
          "lively people. It is loud but you get the impression that "
          "everyone is enjoying themselves.\nAs you get situated, you hear "
          "some yelling across the bar, two men have started to argue and it "
          "seems like it is going to get physical. ")
    print("Do you get involved?\nChoices\n\n1.See if you can stop the "
          "fight.\n2.Stay out of the fight, none of my business.")
    tavern_loop = True
    while tavern_loop:
        command = input("> ")
        if command == 1:
            # Goes to the "Tavern" ending #1.
            tavern_ending1()
        elif command == 2:
            # Goes to the "Tavern" ending #2.
            tavern_ending2()
        else:
            print("Invalid input, please try again.")
            continue


def jester_path():
    """Brings the player to the "Jester" path. They can be directed to
        the Jester Ending or the Tavern Path. """
    print(
        "\nYou approach the jester, who tells you he has a proposition for "
        "you. He tells you that he is currently locked out of his house, "
        "and he needs help getting in.")
    print(
        "Since it seems not be be much trouble, you decide to help him. "
        "You follow him to his house, and he asks you to break a window."
        " Using a nearby rock,")
    print(
        "You break the window and he crawls through. He asks for you to "
        "come in afterward.\nDo you join him?\nChoices\n\n1.Go in the "
        "house with him.\n2.Refuse and go to the tavern.")
    jester_loop = True
    while jester_loop:
        command = input("> ")
        if command == "1":
            # Goes to the "Jester" ending
            jester_loop = False
            jester_ending()
        elif command == "2":
            # Goes to the "Tavern" route
            jester_loop = False
            tavern_path()


def outside_path():
    """Brings the player to the "Outside" path . They can be directed to
        the Jester path or Tavern path. """
    print(
        "\nYou leave the cave. Outside of the cave you see that you are in "
        "dark forest. You notice that there is a path from the entrance to the"
        " cave that leads further into the forest. With no other option, you "
        "decide to follow it.")
    print(
        "\nAfter keeping to the path for what feels like an eternity, you"
        "arrive at a quiet town in the middle of the woods. At first it "
        "seems barren, but you hear noise coming from a tavern in the "
        "center of town, the town's only source of light.")
    print(
        "\n As you approach the tavern, you hear a whistling noise. You"
        " turn around to see a drunken jester trying to get your "
        "attention.\n1.See what the jester wants. \n2.Ignore the drunken "
        "jester and enter tavern.")
    outside_loop = True
    while outside_loop:
        command = input("\n> ")

        # Goes to the "jester" route
        if command == "1":
            outside_loop = False
            print("jester")
            jester_path()

            # Goes to the "tavern" route
        elif command == "2":
            outside_loop = False
            print("tavern")
            tavern_path()
        else:
            print('Invalid response, type "1" or "2"')
            continue


def optional_puzzle():
    """This function contains a puzzle that the user can solve. It is
    optional and has no consequences whether the player can solve this or
    not. The player is redirected to the "Enter the City" scene."""
    print(
        'The gatekeeper explains the premise of his simple game. Guess what '
        'number he is thinking of. He explains the following rules:')
    print(
        '\n"The number will be between 1 and 20. You will have five tries to '
        'guess the number. You will be told if your guess was higher or '
        '.lower than the number."')
    print("The game begins now.\nGuess:")

    # Uses for loop with relational operators
    answer = random.randrange(1, 20)
    guess_amount = 0
    for turn in range(5):
        try:  # stops the user from entering invalid inputs
            guess = int(input("> "))
        except ValueError:
            print("Please try guessing a whole number!")
            continue
        if guess == answer:
            break
        elif int(guess) > answer:
            print("Your guess was higher than the number.")
        elif int(guess) < answer:
            print("Your guess was lower than the number.")
        guess_amount += 1
    if guess_amount < 5:
        print("\nCongrats you won.\n")
    elif guess_amount:
        print("\nSorry you lost.\n")
    print(
        "The gatekeeper thanks you for playing his game. You now head into "
        "the city.")
    enter_the_city()


def puzzle_path(amulet):
    """Brings the player to the "Puzzle" path. If the player has the amulet,
the scene plays out differently, as they do not have to complete the puzzle.
The puzzle has infinite the attempts, with a success putting the player in
the "Enter the City scene, and a failure bringing the player to the
"Outsider" path.  """
    if amulet:
        print(
            "As the gate keeper is about to the begin the puzzle, he notices "
            "takes great notice from the amulet on your person. ")
        print(
            "He explains that they have been waiting for someone to bring "
            "this amulet back to their civilization. He decides to let you"
            " into the city without solving the puzzle.")
        print("enter the city")
        enter_the_city()
    else:
        print(
            'The gatekeeper gives you the following riddle:\n\n"This has a'
            'head and tail, but no body. It is a ________?"\nNOTE: You can'
            ' guess as many times as you want, if your give up, '
            'type "quit".\nGuess:')
        puzzle_loop = True
        while puzzle_loop:
            command = input("> ")
            if command == "coin".lower():
                print(
                    'CORRECT!\nThe gate keeper explains that you are now '
                    'able to enter the city, however he has an optional '
                    'game to play if you are up for it.')
                print("\n\nChoices\n1.Play his game.\n2.Enter the city.")
                continue

            # Goes to the outside path
            elif command == "quit".lower():
                print(
                    "You quit attempting the gatekeeper's riddle. With "
                    "no other option, you decide to leave the cave.\n")
                outside_path()

            # Goes to the optional puzzle function
            elif command == "1":
                print("puzzle")
                optional_puzzle()

            # Goes to the "enter the city" path
            elif command == "2":
                enter_the_city()

            else:
                print("Wrong! Try again.")
                continue


def cave_path():
    """Brings the player to the "Cave" path. They can be directed to
        the Puzzle Path or the Outside Path. """
    has_amulet = ""
    print(
        "\nYou explore further into the cave filled with pillars and "
        "stalagmites. The amount of torches placed becomes more prevalent. "
        "As you walk through the cave you see a")
    print(
        "mysterious glint of light from some rocks for a split second. "
        "Curious, you approach the rocks and notice there is an opening "
        "between the rocks.")
    print(
        "You reach your hand in and find an amulet with a strange symbol"
        " on it.")
    print(
        "Do you take it?\n\nChoices:\n1.Take it. I bet no one's coming "
        "back for it.\n2.Leave it. Someone probably stashed it here and will "
        "probably come back for it.")
    cave_loop = True
    while cave_loop:
        command = input("\n> ")

        # Player takes amulet
        if command == "1":
            cave_loop = False
            has_amulet = True
            print("\nYou took the amulet.\n")

        # Player leaves amulet
        elif command == "2":
            cave_loop = False
            has_amulet = False
            print("\nYou decide not to take the amulet.\n")
        else:
            print('Invalid response, type "1" or "2"')
            continue

    print(
        "As you continue to walk, you soon arrive at a large wooden gate "
        "built in the cave. An old man ")
    print(
        "in rags, comes out from an opening in the gate. He explains that "
        "there is a society full of the brightest scholars and philosophers "
        "that live beyond the gate. But")
    print(
        "to pass, you must answer his riddle, or leave.\n\nChoices:\n1.See if "
        "you can solve the riddle.\n2.I'm not smart enough for this, "
        "I'm leaving.")
    gate_loop = True
    while gate_loop:
        command = input("\n> ")

        # Goes to the "puzzle" route
        if command == "1":
            gate_loop = False
            puzzle_path(has_amulet)  # Passes argument

        # Goes to the "outside" route
        elif command == "2":
            gate_loop = False
            outside_path()
        else:
            print('Invalid response, type "1" or "2"')
            continue


def game_has_started():
    """Brings the player to the first scene. They can be directed to
        the Cave path or Outside Path. """
    print(
        "\nYou awaken in the entrance of a dark cave, your memory hazy "
        "to the events that led up to your arrival here.\nLooking in the "
        "cave, you faintly see torches placed on the walls deep in the cave, "
        "indicating that someone has been there.")
    print(
        "\nChoices:\n1.Your curiosity gets the best of you, you must "
        "investigate this mysterious cave.\n2.What a boring cave. I'm "
        "getting out of here.")
    game_loop = True
    while game_loop:
        command = input('Enter choice ("1" or "2") \n>')

        # Goes to the "cave" story route
        if command == "1":
            game_loop = False
            cave_path()
        # Goes to the "outside" story route
        if command == "2":
            game_loop = False
            outside_path()
        else:
            print("Invalid input, try again")
            continue


# Questions prompted to the player when they choose PLAY GAME
def ready_to_play():
    """This function asks the player whether they are ready to start the
    game. This can lead to the game beginning, or the player returning to
    the main menu."""
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
                ready_to_play_loop = False
                main_menu()
                menu_navigation()
            elif command == "no".lower():
                print("Are you ready to start your adventure?\nYes or No")
                continue
        else:
            print(
                'Invalid command, try again')
            continue


# Function that calls the Main Menu Screen

def main_menu():
    """This function prints the main menu to the player when the program
    starts."""
    print("""
            WELCOME TO "SECRET OF THE GOLDEN EGG"    
                    PLAY GAME
                    GAME INFO
                     CREDITS
                    QUIT GAME
                     """)


def menu_navigation():
    """This functions allows the main menu commands to run."""
    main_menu_loop = True
    while main_menu_loop:
        command = input("> ")
        # Code for quitting the game.
        if command == "quit game".lower() or command == "quit".lower():
            print("You have exited the game.\nTHANKS FOR PLAYING")
            break
            # Stops the code

        # Code for the "CREDITS" section.
        elif command == "credits".lower():
            print("This game was created by Govinda Ramrattan.\nBACK")
            command = input("> ")
            if command == "back".lower():
                main_menu()
            else:
                print(
                    'Invalid command, enter "back" to return to the main '
                    'menu')  # if any undefined commands are typed

        # Code for "GAME INFO" section.
        elif command == "game info".lower():
            print(
                '"SECRET OF THE GOLDEN EGG" is a text-based RPG Game. Follow '
                'your character in an \ninteractive journey where '
                'your choices affect the outcomes.\nTry and see if you '
                'can get all the endings!(Although only one ending '
                'makes the title make sense) Good Luck!\nBACK')
            command = input("> ")
            if command == "back".lower():
                main_menu()
            else:
                print(
                    'Invalid command, enter "back" to return to the main menu')

        # Code for "PLAY GAME" section.
        elif command == "play".lower() or command == "play game".lower():
            main_menu_loop = False
            print("\n")
            ready_to_play()
        elif command == "back".lower():
            main_menu()


# Main functions are called:

main_menu()
print("NOTE: input your commands and choices next to the > symbol.")
menu_navigation()



