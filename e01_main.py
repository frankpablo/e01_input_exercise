# ------------------------------------------------------
# INFO: this example shows different ways of using the
#   input built-in function
# ------------------------------------------------------

## NOTE: this code fails at the end ON PURPOSE
print("Hello!")
print("Below, the program will wait for you to write your name AND press 'return'")
# getting a string with no prompt
name = input("Give me your name: ")

print() # just to add a new line

total_pets = 0

# getting a string with a prompt
num_dogs = input("How many dogs do you have? ")
# using the numeric string to print
print (name,"has",num_dogs,"dogs")

# getting another string with a prompt
num_cats = input("How many cats do you have? ")

#if you try to use these variables in an expression
# you'll run into trouble
# total_pets = total_pets + num_dogs + num_cats

print("total_pets:", total_pets)

# Tasks and Questions:
#  0. Uncomment line 26
#  1. What is wrong with line 26?
#  2. How do we fix the issue that appears in line 26?
#  3. Change line 26 to use an update operator

# The Update operators
# The following are shorthand operators for updating a variable:
# x = x + 3 is the same as x += 3
# x = x - 3 is the same as x -= 3
# x = x * 3 is the same as x *= 3
# x = x / 3 is the same as x /= 3

#  3. Rewrite the corrected expression of line 26 using: +=
