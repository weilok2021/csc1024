import random

def main():
    fruits_list = ["apple", "banana", "grapes", "orange"]

    # Ask users do they need a tutorial
    print("Do you need some tutorials before starting the game?") 
    
    tutor_need = input("Type 'yes' or 'y' if you need, type 'no' or 'n' if you don't need: ").strip().lower()
    # when user enters invalid input, reprompt
    while not_valid_instruction(tutor_need): 
    #not(tutor_need in ['y', 'yes']) and not(tutor_need in ['n', 'no']):
        tutor_need = reprompt()
    if tutor_need in ['y', 'yes']:
        tutorial()
    
    # starts the game
    play(fruits_list)
    # After playing a game.
    while True:
        print("\nDo you want to start a new game?")
        start_or_exit = input("Type 'yes' or 'y' if you want a new game, type 'no' or 'n' to exit: ").strip().lower()
        while not_valid_instruction(start_or_exit):
            start_or_exit = reprompt()
        # if user enters yes or y, play the game else exit the game.
        if start_or_exit in ['y', "yes"]:
            play(fruits_list)
        elif start_or_exit in ['n', 'no']:
            print("You leaved the game. See you next time!")
            break
            

def play(fruits_list):
    print("-----------------------------------------")
    print("\t\tWELCOME TO THE WORLD OF \n\t\t\t MASTERMIND!!")
    print("-----------------------------------------")
    
    random_fruits = random.choices(fruits_list, k=4)
    #print(random_fruits)
    num_attempt = 0
    while True:
        print("random_fruits are:", random_fruits)
        user_fruits = []
        
        for i in range(4):
            user_choice = input(f"Enter your choices from the list of 4 random fruits. choice {i+1} : ").strip().lower()
            while not(user_choice in fruits_list):
                user_choice = reprompt()
            user_fruits.append(user_choice) 
        
        random_fruits_count = dict()
        user_fruits_count = dict()
        
        # Using fruit_name as key, number of each fruit as value, initailize key, value pair for both dict
        # one dict for random_fruits_count, the other one for user_fruits_count
        for i in range(4):
            fruit_name = fruits_list[i]
            random_fruits_count[fruit_name] = random_fruits.count(fruit_name)
            user_fruits_count[fruit_name] = user_fruits.count(fruit_name)
            
        num_correct_fruit = 0
        # correct fruit in correct place
        num_correct_place = 0
        # correct fruit in wrong place
        num_wrong_place = 0
        
        for fruit_name, random_fruit_count in random_fruits_count.items():
            # only find the numbers of correct fruit
            if random_fruit_count > 0:
                if user_fruits_count[fruit_name] == random_fruits_count[fruit_name]:
                    num_correct_fruit += user_fruits_count[fruit_name]
                elif user_fruits_count[fruit_name] > random_fruits_count[fruit_name]:
                    num_correct_fruit += random_fruits_count[fruit_name]
                elif user_fruits_count[fruit_name] < random_fruits_count[fruit_name]:
                    num_correct_fruit += user_fruits_count[fruit_name]
        
        for i in range(4):
            if user_fruits[i] == random_fruits[i]:
                num_correct_place += 1
        num_wrong_place = num_correct_fruit - num_correct_place
        
        print("\nCorrect fruit in the correct place:", num_correct_place)
        print("Correct fruit in the wrong place:", num_wrong_place)
        
        num_attempt += 1
        
        # if user guessed every fruit correctly in correct place, end this game.
        if num_correct_place == 4:
            print("Congratulations! You won the game!")
            print(f"you took [{num_attempt}] attempt to win the game!")
            break
        
        print(f"\nThis is your [{num_attempt}] attempt for mastermind.")
        
        # Enter yes or y if you want to Continue this game, else enter no or n 
        continue_or_stop = input("Enter 'y' or yes' if you wish to continue this game. Enter 'n' or 'no' if you wish to stop this game: ").strip().lower()
        while not_valid_instruction(continue_or_stop):
            continue_or_stop = reprompt()
        
        
        if continue_or_stop in ['y','yes']:
            continue
        elif continue_or_stop in ['n', 'no']:
            print("\nUnfortunately, you lost the game...Good try anyways")
            break
            

def reprompt():
    new_input = input("That is not a valid input, please enter again: ").strip().lower()  
    return new_input


def tutorial():
    print("-----------------------------------------")
    print("\t\tWELCOME TO MASTERMIND\n\t\t\t TUTORIAL")
    print("-----------------------------------------")
    
    print("\nYou are required to guess 4 fruits from a list of possible fruits")
    print("\nThere are only 4 possible fruits in this mastermind world because I want you to play this effortlessly and I want you to be happy ^-^")
    print("\nThe four fruits are apple, banana, grapes, orange")
    print("\nAlthough the same fruit might be repeated in the sequence, but there's not a problem for someone clever as you")
    print("\nGood news is there are some clues at the middle of the game bring you towards the victory")
    print("\nWhen four fruits are guessed correctly including its order, you win!")
    print("\nAlso, you can choose to exit or stop the game at the end of every game")
    print("\nEverytime when a new game started, new fruits list generated randomly\n")
    
    
def not_valid_instruction(user_input):
    # return true if user_input is invalid else, return false.
    return True if not(user_input in ['y', 'yes']) and not(user_input in ['n', 'no']) else False


main()
    
