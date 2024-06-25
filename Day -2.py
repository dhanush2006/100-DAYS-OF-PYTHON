#Day - 2
#Lesson - 1
#print (len(input("What is your name")))
#Data Types : String, Integer, Float, Boolean
#print("Hello"[4])
#String
#print("123"+"456")
#Integer, Large Integer = 234_344_434 instead of "," use "_"
#print(123+456)
#Float
#3.14159
#Boolean
#True, False

#Lesson - 2
#i)
#number_of_characters = len(input("What is yaur name? "))
#type check
#print(type(number_of_characters))
#one type to another data type
#new_num_char = str(number_of_characters)
#print("Your name has "+ new_num_char +" Characters")

#ii)
#a = float(123)
#print(type(a))
#print(70 + float("100.5"))
#print(str(100)+str(100))

#Exercise - 1
#two_digit_number = input("Type a two digit number: ")
#firstdigitnumber = two_digit_number[0]
#seconddigitnumber = two_digit_number[1]
#Final_answer = int(firstdigitnumber) + int(seconddigitnumber)
#print(Final_answer)

#Lesson - 3
#1+1
#2-2
#2*5
#3/4 = result in float
#2**2
#PEMDASLR
#()>**>*/>+-

#Exercise - 2
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
#new_height = float(height) * float(height)
#new_weight = int(weight)
#BMI = new_weight / new_height
#new_BMI = int(BMI)
#print(new_BMI)

#Lesson -4
#print(round(8/3,2)) #round off and also specify the digit to 0
#print(round(8//3)) #clean integer 2 only if "/" then integer

#result = 4/2
#result /=2
#score = 0
#score /= 4
#print(score)

#score = 0
#print("Your score is " + str(score))

#score = 0
#height = 1.8
#iswinning = True
#print(f"your score is {score}, your height is {height}, your are {iswinning}")
#f"all the data type are combined into string"

#Exercise - 3
#age = input("What is your current age?")
#Age = 90 - int(age)
#D1_year = 365*Age
#W1_year = 52*Age
#M1_year = 12*Age
#div_days =  D1_year
#div_weeks = W1_year 
#div_months = M1_year 
#print(f"you have {div_days} days, {div_weeks} weeks, {div_months} months")

#Final_Exercise - 4
#print("Welcome to the tip calculator.\n")
#Total_Bill = input("What was the total bill? $\n")
#Percentage = input("What percentage tip would you like to give? (10, 12, or 15)\n")
#Percent = int (Percentage) / 100
#Percent_in_bill = float(Total_Bill) * Percent
#Add_all_bill = float(Total_Bill) + Percent_in_bill
#Split = input("How many people to split the bill?\n")
#Split = Add_all_bill / int(Split)
#split = "{:.2f}".format(Split)
#print(f"Each person should pay: ${split}")
