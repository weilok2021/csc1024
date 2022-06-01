# ques 1

##import random
##
##while True:
##    count = 1
##    secret_num = random.randint(1, 100)
##    guessed_num = int(input("Guessed a number within 1 through 100: "))
##    while guessed_num != secret_num:
##        if guessed_num < secret_num:
##            print("too low")
##        else:
##            print("too high")
##        count += 1
##        guessed_num = int(input("Have another guess:"))
##    print("Well done, you took " + str(count) + " attempts")
##    user_will = input("do u want to play again? Type (yes/no) or (y/n)")
##    if str.lower(user_will) in ['no', 'n']:
##        break
##

## ques 2
##number = int(input("Which multiplication table would you like to print? "))
##times = int(input("How high would you like to go? "))
##
##count = 1
##while count <= times:
##    multiple = number * count
##    print(str(number) + " times " + str(count) + " = " + str(multiple))
##    count += 1
    
#ques 3
##Write a Python program using the while loop
##to print the follow patter
##n.
##10101010101
##10101010101
##10101010101
##10101010101
##10101010101

##i = 0
##while i < 5: # rows
##    j = 0
##    while j < 11: # columns
##        if j % 2 == 0:
##            print(1, end="")
##        else:
##            print(0, end="")
##        j += 1
##    print("")
##    i += 1


##4.
##Write a temperature conversion program between degree Celsius and degree Fahrenheit

while True:
    print("Temperature Conversion Programme.")
    print("1] Convert Celsius to Fahrenheit.")
    print("[2] Convert Fahrenheit to Celsius.")
    selection = int(input("Enter your selection, 1 or 2: "))
    user_will = ""
    if selection != 1 and selection != 2:
        print("ERROR: Invalid Selection!")
        user_will = input("Do you want to run the program again? [Y/N]: ")
    if str.upper(user_will) != 'Y':
        break
    else:
        continue
    print("Enter temperature in integer values only.")
    min_temp = int(input("Enter minimum temperature: "))
    max_temp = int(input("Enter maximum temperature: "))
    temp = min_temp
    #converted_temp = 0
    if selection == 1:
        print("Celsius (C) to Fahrenheit (F) Conversion")
        while temp <= max_temp:
            converted_temp = (temp *  9/5) + 32
            print(str(temp) + 'C' + ' = ' + str(converted_temp) + 'F')
            temp += 1
        print("Conversion done")
    elif selection == 2:
        print("Fahrenheit (F) to Celsius (C) Conversion")
        while temp <= max_temp:
            converted_temp = (temp - 32) * 5/9
            print(str(temp) + 'F' + ' = '+ str(converted_temp) + 'C')
            temp += 1
        print("Conversion done")
    else:
        print("ERROR: Invalid Selection!")
    user_will = input("Do you want to run the program again? [Y/N]: ")
    if str.upper(user_will) != 'Y':
        break


##if selection != 1 and selection != 2:
##    user_will = input("Do you want to run the program again? [Y/N]: ")
##    if str.upper(user_will) == != 'Y':
##        continue





































