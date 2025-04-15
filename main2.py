# # what are variables?

# # there are different types of variables
# # strings are text
# name= "John" #quotation marks
# name2= "Lucy"
# # integers are whole numbers
# num1="10" # no quotation marks
# num2=20
# print(int(num1)+num2)
# # when you have a plus sign betrween two variables its called concatenatiom
# # floats are decimal numbers
# # typecasting is when you convert a variable from one type to another

# # f strings allows us to insert variables into strings
# # using f before the string
# print(f"{name}and {name2} have {num1} apples")
# # it can be positivce or negative
# dollars= 10.99
# print (f"{name} has {dollars} dollars")
# # booleans arew true or false
# is_student = True
# # It can be true or false
# print(f" {name} is a student: {is_student}")
# # lists are collections of values
# # dictionaries are collections of key-values pairs
# # problem set #1
# # 1. create 5 diff types of variables
# # 2. print them out
# # 3. use f strings to format the strings

# name= "hunty"
# name2= "boots"
# food = "strawberries"
# num1= 420
# print(f"{name} and {name2} bought {num1} strawberries to make jam")


# if conditionals
# if statements are used to check if a condition is true or false 
# of condition  is true, do something 

# if conditional statements always start with if
#  and depend on a boolean value ( true or false)
# example
classStarted = True
if classStarted:
    print("class has started")
else:
    print ("class has not started")

#  logiical and comparison operators
# == logical to
# != not equal to 
# > greater than
# < less than
#>= greater than or equal to
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
    age= 18
    if age >= 18:
        print("you are an adult")

    elif age == 17:
        print ("you are almost an adult")
    else:
        print ("you are a minor")

    
    # problem set #2
    # 1. create a program that schecks if a number is even or odd
    # 2. ask user for a number
    number = int(input("what is your number?"))
    # 3. check if number is even or odd
    if  number % 2 == 0:
        print (f"{number} is even")
    else:
        print(f"{number} is odd")
   