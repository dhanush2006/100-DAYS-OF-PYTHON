# #LESSON - 1 
# #MERSENNE TWISTER
# import random
# random_int = random.randint(1,10)
# print(random_int)
# random_float = random.random()
# print(random_float)
# a = random_float * 5
# print(a)

# love_calculator = random.randint(1,100)
# print(f"Your love score is {love_calculator}")

# Exercise - 1 
# import random

# coin = random.randint(0,1)
# if coin == 0:
#     print("Tails")
# elif coin == 1:
#     print("Heads")

# Lesson - 2
# List = datastructure
# fruits = ["apple", "cherry", "mango"]
# India = ["Delhi", "Tamilnadu", "Kerala","Karnataka", "Hydrabad", "Mumbai", "Kolkata"]
# India.append("Dhanush")
# India.extend(["prakash","DP"])
# print(India[1])
# ind = India[1] = "Tamil"
# print(ind) # save it for future
# print(India[-1])
# print(India)

# Exercise - 2
# import random

# names_string = input("Give me everybody's names seperated by ',' ")
# names = names_string.split(",")
#random.choice(names)
# random_choice = random.randint(0, len(names)-1)
# person = names[random_choice]
# print(person)
# random = ["apple","ap","are","fef"][1]
# print(random)

#Lesson - 3 
# list inside list

# Fruits = ["Apple","Mango","Starberry","Pineapple","Grapes"]
# Vegitables = ["cucumber","onion","carrot","beans","tomato"]
# Fruits_Vegitables = [Fruits,Vegitables]

# print(Fruits_Vegitables)

# Exercise - 3 
# row1 = ["🥺","🥺","🥺"]
# row2 = ["🥺","🥺","🥺"]
# row3 = ["🥺","🥺","🥺"]

# map = [row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the tressure?")

# horizontal = int(position[0])
# vertical = int(position[1])

# Selected_row = map[vertical - 1]
# Selected_row [horizontal - 1] = "x"

# print(f"{row1}\n{row2}\n{row3}")

#Final Exercise 
# import random

# Rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# Paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# Scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """


# user_Choose = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Sissors\n"))
# if user_Choose >= 3 or user_Choose < 0:
#     print("You typed an invalid number")
# if user_Choose == 0:
#     print(Rock)
# elif user_Choose == 1:
#     print(Paper)
# elif user_Choose == 2:
#     print(Scissors)


# computer_choose = random.randint(0,2)
# if user_Choose >= 0 or user_Choose <= 2:    
#     if computer_choose == 0:
#         print(Rock)
#     elif computer_choose == 1:
#         print(Paper)
#     elif computer_choose == 2:
#         print(Scissors)

# if user_Choose == computer_choose:
#     print("The Match is Draw")
# elif user_Choose != computer_choose:
#     if user_Choose == 0 and computer_choose == 2:
#         print("You Win")
#     elif user_Choose == 0 and computer_choose == 1:
#         print("You lose")
#     elif user_Choose == 1 and computer_choose == 0:
#         print("You Win")
#     elif user_Choose == 1 and computer_choose == 2:
#         print("You Lose")
#     elif user_Choose == 2 and computer_choose == 1:
#         print("You Win")
#     elif user_Choose == 2 and computer_choose == 0:
#         print("You lose")
# elif user_Choose >= 3 or user_Choose < 0:
#     print("You typed an invalid number")