# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:00:35 2024

@author: mando
"""


# %% First Codes:
print("Hello, World!")
print("I like 6.00.1x!")


x = int(input("Enter an integer: "))
if x % 2 == 0:
    print("")
    print("Even")
else:
    print("")
    print("Odd")
print(
    "Done with conditional"
)  # The indentation is important here. It would be part of the block otherwise.


"eric"[1:4]


# %% Exercício com o comando input() -----
text = input("Digite alguma coisa...")
print(5 * text)


# Funcionamento de Loops -----
n = input("You are lost in the Lost Forest. Go Left or Right? ")
while n == "Right":
    n = input("You are lost in the Lost Forest. Go Left or Right? ")
print("You got out of the Lost Forest!")


# More complex using only the WHILE:
n = 0
while n <= 5:
    print(n)
    n = n + 1

# Using the FOR Loop is easier to understand and make:
for n in range(5):
    print(n)

# FOR Loop com valores fora do padrão:
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)


# %% THE BREAK STATEMENT ON LOOPS:

num = 10
while True:
    if num < 7:
        print("Breaking out of loop")
        break
    print(num)
    num -= 1
print("Outside of loop")
# Notice the function of the break statement
# It will stop the code there and then it will immediately go to the line outside of the loop.


# %% Exercises WHILE
# Exercise 01: WHILE Loop
# Convert the following into code that uses a while loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

num = 2
while num <= 10:
    print(num)
    num += 2
print("Goodbye!")

# Exercise 02: WHILE Loop
# Convert the following into code that uses a while loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
num = 10
while num >= 2:
    print(num)
    num -= 2

# Here is another way:
num = 11
print("Hello!")
while num > 1:
    num -= 1
    if num % 2 == 0:
        print(num)


# Write a WHILE loop that sums the values 1 through 'end', where 'end' is a variable of any value:
# This is my answer and it works... Even though the course evaluates it as being wrong.
end = 6
n = 1
TotalSum = 0
while n in range(1, end + 1):
    TotalSum = TotalSum + n
    n = n + 1
print(TotalSum)

# Here is one of a few ways to solve this problem:
end = 6
current = 1
total = 0
while current <= end:
    total += current
    current += 1

print(total)


# %% Exercises FOR
# Exercise 01: In this problem you'll be given a chance to practice writing some for loops.
# Convert the following into code that uses a for loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

i = 2
for i in range(2, 12, 2):
    print(i)
    i += 2
print("Goodbye!")

# Exercise 02: FOR Loop
# Convert the following into code that uses a while loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
i = 10
for i in range(10, 0, -2):
    print(i)
    i += i

# Write a FOR loop that sums the values 1 through 'end', where 'end' is a variable of any value:
# This is my answer and it works... Even though the course evaluates it as being wrong.
end = 6
n = 1
TotalSum = 0
for n in range(1, end + 1):
    TotalSum = TotalSum + n
    n = n + 1
print(TotalSum)

# %% ITERATION

num = 100
for num in range(5):
    print(num)
print(num)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")


for letter in "hola":
    print(letter)


divisor = 2
for num in range(0, 10, 2):
    print(num / divisor)


# EXERCISE
greeting = "Hello!"
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print("done")


# EXERCISE
school = "Massachusetts Institute of Technology"
numVowels = 0
numCons = 0

for char in school:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        numVowels += 1
    elif char == "o" or char == "M":
        print(char)
    else:
        numCons -= 1

print("numVowels is: " + str(numVowels))
print("numCons is: " + str(numCons))


# UNIT 01: Final Problem 1
# Assume 's' is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

school = "Massachusetts Institute of Technology"
numVowels = 0
numCons = 0

for char in school:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        numVowels += 1
    elif char == "o" or char == "M":
        print(char)
    else:
        numCons -= 1

print("numVowels is: " + str(numVowels))
print("numCons is: " + str(numCons))

test = ""
