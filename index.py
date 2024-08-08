print("Hello Python world!")

# variables
message = "Hello Njonge"
print(message)

# STRINGS
# Changing case in a string with methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Using variables in strings
first_name = "fred"
last_name = "njonge"

full_name = f"{first_name} {last_name}"
print(full_name.title())

# Adding whitespace to strings with tabs or newlines
# \t - Add a tab to your text
print("Python")
print("\tPython")

# \n - Add a neline ina string
print("Languanges:\n\tPython\n\tRuby\n\tJavaScript")

# Stripping whitespace
favorite_language = 'python '
fav = favorite_language.rstrip() #strips space from the right side of a string

# lstrip() - strips whitespace from the left side of a string
# strip() - strips whitespace from both sides(left and right)

# Removing prefixes
# nostarch_url = 'https://nostarch.com'
# nostarch_url.remove('https://') # Leaves the original string unchanged

# simple_url = nostarch_url.removeprefix('https://')
# print(simple_url)

# removesuffix() - works exactly like the above and can be used to remove file extensions from filenames

# NUMBERS
# Division of floats and numbers
print(4/2) # always get a float

# Underscores in Numbers- when writing long numbers, you can group digits using underscores to make large numbers more readable
universe_age = 14_000_000_000
print(universe_age)

# Multiple assignment
x,y,z = 0, 2, 4
print(x)
print(y)
print(z)

# CONSTANTS- a variable whose value stays the same throughout the life of of a program
MAX_CONNECTIONS = 5000

# CHAPTER 2: INTRODUCING LISTS
# List- collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
print(bicycles[0])

# Using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# Modifying, Adding and Removing Elements
# 1. Modifying
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 2. Adding elements to a list
# Appending elements to the end of a list
motorcycles.append('honda')
print(motorcycles)

# Inserting elements into a list
# insert()- you can specify the index of the new element
motorcycles.insert(0, 'toyota')
print(motorcycles)

# Removing elements from a list
# del() - removes the element if you know the position of the item from the list
del motorcycles[0]
print(motorcycles)

# pop() - removes the last item in alist, but it lets you work with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popping items from any position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Removing an item by value
motorcycles.append('ducati')
motorcycles.insert(0, 'honda')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# you can use the value removed just like in the pop method
motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# NOTE
# The remove() method deletes only the first occurence of the value you specify.
# If there's a possibility the value appears more than once in a list, you'll need
# to use a loop to make sure all occurences of the value are removed.

# Organizing a List
# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can sort the list above in a reverse-alphabetical order by passing the argument reverse=True
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in Reverse Order
cars.reverse()
print(cars)

# Notice that reverse() doesn't sort backward alphabetically;
# it simply reverses the order of the list
# and changes the order of the list permanently, but
# you can revert to the original order by applying reverse() to the same list a second time.

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# CHAPTER 3: WORKING WITH LISTS
# Looping through a list using the for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
# Doing more work within a for loop
    # print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
# Doing something after a for loop
print("Thank you, everyone. That was a great magic show!")

# Making numerical lists
# Using the range() Function
for value in range(1, 5):
    print(value)
    
# Using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# You can use range() to skip numbers in a given range
# example: list of even numbers
# starts with 2 and the adds 2 to that value. it adds 2
# repeatedly until it reaches or passes the end value, 11,
# and produces the results below
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# square from 1 to 9
squares = []
for value in range(1, 10):
    square = value ** 2
    squares.append(square)

print(squares)

# Simple statistics with a list of numbers
# min, max and sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehesions- allows you to generate this same list in just one line of code
squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

# Working with part of a list
# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])
print(players[2:])
print(players[:-3])

# Looping through a slice
print('Here are the first three players on my team:')
for player in players[:3]:
    print("\t")
    print(f"{player.title()}")
    
# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# TUPLES
# is an immutable list(cannot be modified)
# Defining a tuple - looks like a list but you use parentheses instead of square brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250

# tuple with one element
my_t = (3,)
print(my_t)

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
    
# Writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
# CHAPTER 5
# IF STATEMENTS
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# Checking for equality
car = 'bmw'
print(car == 'bmw')

# Ignoring case when checking for equality
car = 'Audi'
print(car == 'audi')

# Why false?
# Testing for equality is case sensitive in Python.
car = 'Audi'
print(car.lower() == 'audi')

# Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies')
    
# Checking whether a value is in a list
# The keyword in tells Python to check for the existence of 'mushrooms' and 'pepperoni' in the list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Using if Statemenets with lists
# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")

# DICTIONARIES
# A simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'red'
print(f"The alien is now {alien_0['color']}")

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original postion: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using get() to acess values
# Sets a default value that will be returned if the requested key doesn't exist
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
# If you leave out the second argument in the call to get()
# and the key doesn't exist, Python will return the value None.
# The special value means "no value exists".This is not an error:
# it's a special value meant to indicate the absence of a value.

# Looping Through a Dictionary
# Looping through all key value pairs
user_0 = {
    'username': 'efermi', 
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Looping through all the keys in a dictionary
for name in favorite_languages.keys(): # This is the default behaviour
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# looping through a dictionary's keys in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
# The above returns a collection with repetitive languages
# To solve the problem we will use a set
# set - is a collection in which each item must be unique
print("Printing languages without repetition")
for language in set(favorite_languages.values()):
    print(language.title())
    
# You can build a set directly using braces and 
# separating the elements with commas:
languages = {'python', 'rust', 'c', 'python'}
print(languages)

# When you see braces but no key-value pairs, its probably a set
# Unlike lists and dictionaries, sets do not retain items in any specific order

# NESTING
# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# A more realistic example
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] =10
        # elif alien['color'] == 'yellow':
        #     alien['color'] = 'red'
        #     alien['speed'] = 'fast'
        #     alien['points'] = 15
    
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# A list in a dictionary
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['topping']:
    print(f"\t{topping}")

# More example
favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'], 
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell', 'ruby'],
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favourite language is:")
    for language in languages:
         print(f"\t{language.title()}")


# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein', 
        'location': 'princeton'
    }, 
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# CHAPTER 7: USER INPUT AND WHILE LOOPS
# How the input() function works
# input() - this pauses your program and waits for the user to enter some text
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# # Writing clear prompts
# name = input("Please enter your name: ")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")

# # Using int() to Accept numerical input
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older")
    
# # The modulo operator
# # % - divides one number by another and returns the remainder
# number = input("Enter a number, and I'll tell you if it's even or odd:")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
    
# # Introducing while loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
    
# # Letting the user choose when to quit
# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# # Using a flag
# active = True

# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
        
# # Using break to exit a loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)
    
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")
        
# # Using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
    
# # Avoiding infinite loops
# x = 1
# print('\n')
# while x <= 5:
#     print(x)
#     x += 1
    
# Using a while loop with lists and dictionaries
# you shouldn't  modify a list inside a for loop because Python
# will have trouble keeping track of the items in the list
# To modify a list as you work through it, use a while loop

# Moving items from one list to another
# start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# The modified array of confirmed users
print(confirmed_users)

# Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# Filling a dictionary with user input
# responses = {}
# # Set a flag to indicate that polling is active
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
    
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
    
#     # Store the response in the dictionary.
#     responses[name] = response
    
#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond?(yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
#     elif repeat == 'yes':
#         polling_active = True
#     else:
#         print("Please say yes or no!")
#         polling_active = False
    
# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")

# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")
    
    
# CHAPTER 8: FUNCTION
# Defining a function
def greet_user():
    # This is a comment called docstring, which describes what the function does.
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()

# Passing information to a function
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('fred')

# Passing arguments
# 1. Positional Arguments- need the arguments to be in the  same order the parameters were written
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
# Multiple function calls
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# order matters in positional arguments

# 2.Keyword Arguments-is a name-value pair that you pass to a function
# keyword arguments free you from having to worry about correctly ordering your arguments in athe function call
# And clarify the role of each value in the function call.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pet(pet_name='Njonge', animal_type="Bull")

# Default values
# the default value should be the last parameter in a function definition
def describe_pet( pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pet('banda')

# Return values
# Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('fred', 'muturi')
musician2 = get_formatted_name('fred', 'muturi', 'njonge')

print(musician)
print(musician2)

# Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician = build_person('jimi', 'hendrix')
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    break

# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in a list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Arbitrary Arguments, *args
# If you do not know how many argument sthat will be passed into your function,
# add a * before the parameter name in the function
def my_function(*kids):
    print(f"The youngest child is {kids[2]}")

my_function('Emil', 'Tobias', 'linus')

# Keyword Arguments
def my_function(child3, child2, child1):
    print(f"The youngest child is {child3}")

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add twoo asterisk: ** before the parameter name in the function defination.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kid):
    print(f"His last name is {kid['lname']}")

my_function(fname = "Tobias", lname = "Marcos")

# The pass statement
# function definations cannot be empty, but if for some reasons
# You have a function defination with no content, put pass
# statement to avoid getting an error
def myfunction():
    pass

# Positional-only arguments
# You can specify that a function can have only positional arguments, or ONLY keyword arguments
# To specify that a function can have only positional arguments, add ,/ after the arguments
def my_function(x, /):
    print(x)

my_function(3)

# Keyword-only arguments
# To specify that a function have only keyword arguments, add *, before the arguments
def my_function(*, x):
    print(x)

my_function(x = 4)

# combine positional-only and keyword-only
# You can combine the two arguments types in the same function
# Any arguments before the /, are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
    print(a+b+c+d)

my_function(5, 6, c= 7, d= 8)

# Recursion - a defined function can call itself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# PYTHON LAMBDA
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but only have one expession.
x = lambda a: a + 10
print(x(3))

x = lambda a, b: a * b
print(x(2,6))

# Why use lambda functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function
# For example
def myfunction(n):
    return lambda a : a * n

mydoubler = myfunction(2)

print(mydoubler(11))

# PYTHON CLASSES AND OBJECTS
# a class with state and behaviors
class GoodDog:
    def __init__(self, name):
        # self.name is an instance variable(state)
        self.name = name
        print(f"Constructor for {self.name}")

    # speak is an instance method(behavior)
    def speak(self):
        # we're using th eself.name instance variable
        print(f"{self.name} says woof!")

    # roll_over is an instance method(behavior)
    def roll_over(self):
        # we're using the self.name instance variable
        print(f"{self.name} is rolling over.")
    
sparky = GoodDog('Sparky') # Constructoe for sparky
sparky.speak()
sparky.roll_over()

rover = GoodDog('Rover')
rover.speak()
rover.roll_over()
# Explanation
# 1.__init__ is a magic method(dunder method) in python.its called an initializer,instance constructor or constructor.
# it initializes a new instance of an object

# INHERITANCE
class Dog:
    def __init__(self,name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat:
    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot:
    def __init__(self, name):
        self.name = name
        type_name = type(self).__init__
        print(f'I am {name}, a {type_name}.')

    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
fluffy = Cat('Fluffy')
polly = Parrot('Polly')

sparky.roll_over()

for pet in [sparky, fluffy, polly]:
    pet.speak()

        
# type(self).__name__ programmatically dertermine the name of the class to which an object belongs.
# lets clean the above code
class Pet:
    def __init__(self,name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

    def eat(self):
        print(f"{self.name}: Yum-yum-yum!")
        

class Dog(Pet):
    # __init__ method removed
    def speak(self):
        print(f'{self.name} says woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat(Pet):
    # __init__ removed
    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):
    # __init__ method removed
    def speak(self):
        print(f'{self.name} wants a cracker!')
    
    def eat(self):
        print(f'{self.name}: delicious')


sparky = Parrot('Saprky')
sparky.eat()

# we can rewrite type(self).__name__ as self.__class__.name__.type(self)

# STATES AND BEHAVIOURS
# state refers to data associated with an individual class inheritance
# behaviour is what class instance objects can do

# OJECT SCOPE
# refers to methods and instance variable an object can access.

# Object Instantiation
class GoodDog:
    def __init__(self):
        print('This object was initialized!')

sparky = GoodDog()

# Instance Variables
class GoodDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

sparky = GoodDog('Sparky', 5)

# self.name and self.age are instance variables.

# Insatce Methods
class GoodDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return 'Arf!'
    
sparky = GoodDog('sparky', 5)
print(sparky.speak())

"""
    All instance methods must have a self parameter.
"""

# Privacy
# Suppose we want to print sparky's name
print(sparky.name)

# you can reassign th einstance variable:
sparky.name = 'Fido'
print(sparky.name)

# We can use a getter and a setter
class GoodDog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'
    
    def name(self):
        return self._name
    
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name
    
    def age(self):
        return self._age
    
    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age

sparky = GoodDog('Sparky', 5)
print(sparky.name())
print(sparky.age())
sparky.set_name('Fireplug')
print(sparky.name())
sparky.set_age(6)
print(sparky.age())
# sparky.set_name(45)
# sparky.set_age(-4)

# Properties
# A more Pythonic way to create getters and setters is to use the @property decorator
# Decorators are a fairly advanced concept in python
class GoodDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f'{self.name} says arf!'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be a number')
        if age > 0:
            raise ValueError('Age should be positive')
        self._age = age

"""
    Using these decorators means we no longer need () when accessing the getter and setter
    When to use properties:
        1. You want to strongly discourage misuse of instance variables.
        2. You want to validate data when your instance variable receive new values.
        3. You have dynamically computed attributes
        4. You need to refactor your code in a manner incompatible with te existing interface
        5. You want to improve your code readability and properties can help.
    #If you don't need properties to satisfy a specific problem, you shouldn;t use them
 """

# CLASS METHODS
# Python lets you invoke class mwthods with class and also instance objects
# class method requires atleast one parameter: the class itself.
# By convection, the first parameter is named cls:
class GoodCat:
    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")

# Calling the class method
GoodCat.what_am_i()

# Ways of calling a class method
# 1. If you need to call class method from within another class of 
# the same class, you can use the cls argument as the caller 
# for second method:
class Foo:
    @classmethod
    def bar(cls):
        print('this is bar')

    @classmethod
    def qux(cls):
        print('this is qux')
        cls.bar()

Foo.qux()

# 2. When you wnt to call a specific class method from outside the class
# that contains the class method, use the class's name to call it, as we did above

# 3. If you have an instance object, obj, of a class that has a class method, you invoke
# that method by using type(obj), obj.__class__, or even obj as the caller. You can also
# use self inside a method as shown below:
class Foo1:
    @classmethod
    def bar(cls):
        print('this is bar in Foo1')

    def qux(self):
        type(self).bar()
        self.__class__.bar
        self.bar()
        Foo1.bar()

class Foo2(Foo1):
    @classmethod
    def bar(cls):
        print('this is bar in Foo2')

foo1 = Foo1()
foo1.qux()


# CLASS VARIABLES
class GoodCat:
    # class variable
    counter = 0

    def __init__(self):
        GoodCat.counter += 1

    @classmethod
    def number_of_cats(cls):
        return GoodCat.counter
    
class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()

print(GoodCat.number_of_cats())
print(GoodCat.counter)
print(ReallyGoodCat.number_of_cats())

cat3 = ReallyGoodCat()
print(ReallyGoodCat.counter)

# CLASS CONSTATNTS
class GoodCat:
    CAT_YEARS = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        return self.age * GoodCat.CAT_YEARS

# More about self
# self always represent an object.ie the calling object

# STATIC METHODS
# provide utility services to the instance or class methods or to the users of the class
# To define a static method, you use the @staticmethod decorator followed by afunction defination that doesn't use a self or cls parameter.
class TheGame:
    def play(self):
        pass

    @staticmethod
    def show_rules():
        print('These are the rules of the game')

TheGame.show_rules()
game = TheGame()
game.play()

# MAGIC METHODS
# ALSO CALLED DUNDER METHODS(dunder stands for double underscore)
# These are special method in python that let developers customize the behavior of their objects
# There are surrounded by double underscores(__init__, __new__)
# common are:
# the __str__ and __repr__ method - return string representations of an object.
# In most cases, str and repr return the same value. but not all the time
from datetime import datetime

dt = datetime.now()
print(str(dt))
print(repr(dt))

# CHAPTER 9: CLASSES
# Creating and using a class
class Dog:
    # a simple attempt to model a dog.
    def __init__(self, name, age):
        # initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

# Making an instance from a class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accesing Attributes
print(my_dog.name)

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Inheritance
class Car:
    # A simple attempt to represent a car.
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        # Print a statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # Set the odometer reading to the given value.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        # Add the given amount to the odometer reading.
        self.odometer_reading += miles

class ElectricCar(Car):
    # Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        # Initialize attributes of the parent class.
        super().__init__(make, model, year)
        # defining attributes for child method
        self.battery_size = 40

    def describe_battery(self):
        # Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}--kWh battery.")

my_leaf = ElectricCar('Tesla', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()