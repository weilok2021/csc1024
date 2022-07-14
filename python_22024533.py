import random

fruits_list = ["apple", "banana", "grapes", "orange"]
random_fruits = random.choices(fruits_list, k=4)
random_fruits = ['banana', 'banana', 'apple', 'apple']


print(random_fruits)

while True:
    user_fruits = []
    for i in range(4):
        user_choice = str.lower(input(f"Enter your choices from the list of 4 fruits. choice {i+1} : "))
        while not(user_choice in fruits_list):
            user_choice = str.lower(input("Please enter the valid choice: "))
        print(user_choice)
        user_fruits.append(user_choice) 
    
    random_fruits_count = dict()
    user_fruits_count = dict()
    
       
    # Using fruit_name as key, number of each fruit as value, initailize the dict
    # one dict for random_fruits, the other one for user_fruits
    for i in range(4):
        fruit_name = fruits_list[i]
        random_fruits_count[fruit_name] = random_fruits.count(fruit_name)
        user_fruits_count[fruit_name] = user_fruits.count(fruit_name)
        
    num_correct_fruit = 0
    num_correct_place = 0
    num_wrong_place = 0
    
    for fruit_name, random_fruit_count in random_fruits_count.items():
        print(fruit_name, random_fruit_count)
        # only check for fruits that are available in random_fruits
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
    
    print("numbers of correct fruit:", num_correct_fruit)
    print("Correct fruit in the correct place:", num_correct_place)
    print("correct fruit in the wrong place:", num_wrong_place)
    
    print(random_fruits_count)
    print(user_fruits_count)
    
    if num_correct_place == 4:
        break
    
