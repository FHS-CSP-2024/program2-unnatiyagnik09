# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input ("Please tell me your name!\n\t ")
print("Hi "+ name)
print("How's your day "+ name)


## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input ("What's your name?\n\t ")
print("Hi " + name + " ! How's your day " + name + " ? I hope you have a good day " + name + " !")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

f_name = input("What is your first name: ")
l_name = input("What is your last name: ")
s_address = input("What is your street adress: ")
c_adress = input("What is your city and postal code: ")

print("First Name: " + f_name + "\n" + "Last Name: " + l_name + "\n"+"Street Adress: " + s_address + "\n"+"City and postal code: " + c_adress + "\n" )

## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out

w1 = input("Word 1: " )
w2 = input("Word 2: ")
w3 = input("Word 3: ")
print(w1+"-"+w2+"-"+w3)


## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

name = input("Please type in a name: ")
year = input("Please type in year: ")

print(name+ "is a really short girl who was born in the year " + year + ".\n" + "One morning " + name + " woke up to find out that she had run out of Twix." + "\n" + "So she went out to her garden and just sat in her daisy garden :)" )
