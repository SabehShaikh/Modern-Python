# Q25: Alien Colors 1: Imagine an alien was just shot down in a game. 
# a variable called alien_color and assign it a value of  'green', 'yellow', or 'red'.
alien_color : str = 'green'
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
if alien_color == 'green':
    print(f"The player just earned 5 points for shooting the {alien_color} alien.")


# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
alien_color = 'red'
if alien_color == 'yellow':
    print('player just earned 5 points.')


# Q26: Alien Colors 2: Choose a color for an alien as you did in Exercise 25, and write an if-else chain.

# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
alien_color = 'green'
if alien_color == 'green':
    print('the player just earned 5 points for shooting the alien.')
else:   
    print("the player just earned 10 points.")

# • Write one version of this program that runs the if block and another that runs the else block.
if alien_color == 'yellow':
    print("the player just earned 5 points for shooting the alien.")
else:
    print("the player just earned 10 points.")    


# Q27: Alien Colors 3: Turn your if-else chain from Exercise 5-4 into an if-else chain.
# • If the alien is green, print a message that the player earned 5 points.
alien_color = 'green'

if alien_color == 'green':
    print(f'{alien_color} detected! Player earned 5 points.')

elif alien_color == 'yellow':
    print('Player earned 10 points.')

elif alien_color == 'red':
    print('Player earned 15 points.')

else:
    print("Wrong color selected.")

# version two: 
# • If the alien is yellow, print a message that the player earned 10 points.
alien_color = 'yellow'

if alien_color == 'green':
    print('Player earned 5 points.')

elif alien_color == 'yellow':
    print(f'{alien_color} detected! Player earned 10 points.')

elif alien_color == 'red':
    print('Player earned 15 points.')

else:
    print("Wrong color selected.")

# • If the alien is red, print a message that the player earned 15 points.
alien_color = 'red'

if alien_color == 'green':
    print('Player earned 5 points.')

elif alien_color == 'yellow':
    print('Player earned 10 points.')

elif alien_color == 'red':
    print(f'{ alien_color} detected! Player earned 15 points.')

else:
    print("Wrong color selected.")


# Q28: Stages of Life: Write an if-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
age : int = int(input('enter your age: '))
# • If the person is less than 2 years old, print a message that the person is a baby.
if age < 2:
    print('the person is a baby.')

# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
if age >= 2 and age < 4:
    print('the person is a toddler.')

# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
if age >= 4 and age < 13:
    print('the person is a kid.')

# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
if age >= 13 and age < 20:
    print('the person is a teenager.')

# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
if age >= 20 and age < 65:
    print('the person is an adult.')

# • If the person is age 65 or older, print a message that the person is an elder.
if age >= 65:
    print('the person is an elder.')


# Q29: Favorite Fruit: Make a array of your favorite fruits, and then write a series of 
# if statements that check for certain fruits in your array.
# • Make a array of your three favorite fruits and call it favorite_fruits.
favorite_fruits: list[str] = ['banana' , 'apple' , 'mango']

# • Write five if statements. Each should check whether a certain kind of fruit is in your array.
#  If the fruit is in your array, the if block should print a statement, such as You really like bananas!
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'mango' in favorite_fruits:
    print('You really like mango!')
if 'strawberry' in favorite_fruits:
    print('You really like strawberry!')
if 'pineapple' in favorite_fruits:
    print('You really like pineapple!')


# Q30: Hello Admin: Make a array of five or more usernames, including the name 'admin'. Imagine you are writing code
# that will print a greeting to each user after they log in to a website.
# Loop through the array, and print a greeting to each user:
usernames : list [str] = [ 'RonaldoFan7', 'MessiMagic10', 'admin' , 'NeymarJr11', 'MbappeSpeed', 'Beckham23']

# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
for username in usernames:
    if username == 'admin':
          print(f'Hello {username}, would you like to see the status report?')
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.    
    else:
        print(f'Hello {username}, thank you for logging in again.')


# Q31: No Users: Add an if test to Exercise 30 to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
if len(usernames) == 0:
    print('we need to find some users.')
# • Remove all of the usernames from your array, and make sure the correct message is printed.
else:
    usernames = []
    print(f'All users removed: {usernames} , {len(usernames)}')


# Q32: Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.    
# • Make a list of five or more usernames called current_users.
current_users : list[str] = ['john' , 'abbie' , 'steve' , 'luka' , 'alex']

# • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
new_users : list[str] = ['michael' , 'khan' , 'abbie' , 'alex' , 'lunin']

# • Loop through the new_users list to see if each new username has already been used. If it has, 
for newuser in new_users:
    if newuser.lower() in [user.lower() for user in current_users]:
         # print a message that the person will need to enter a new username. If a username has not been used,
         print('The username', newuser, 'is already taken. Please choose a different one.')
         
    else:
         # print a message saying that the username is available.
         print('The username', newuser, 'is available.')  


# we can also do like this: 
# current_users_lowers = [user.lower() for user in current_users]
# for new_user in new_users:

#     new_user_lower = new_user.lower()

#     if new_user_lower in current_users_lowers:
#         print("the person will need to enter a new username.")
#     else:
#         print('the username is available.')   


# Q33: Ordinal Numbers: Ordinal numbers indicate their position in a array, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a array.
# • Use an if-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
# and each result should be on a separate line.
numbers : list[int] = [1,2,3,4,5,6,7,8,9]

# • Loop through the array.
for num in numbers:
    ordinal_number : str = ''
    if num == 1:
        ordinal_number = 'st'
    elif num == 2:
        ordinal_number = 'nd'
    elif num == 3: 
        ordinal_number = 'rd'
    else:
        ordinal_number = 'th'            

    print(f'{num}{ordinal_number}')

# Q34: Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a array, 
# and then use a for loop to print the name of each pizza.
favorite_pizza : list[str] = ['Chicken Tikka', 'Afghani', 'Pepperoni', 'Fajita']
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. 
# For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in favorite_pizza:
    print(f'I like {pizza} pizza.')

# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and 
# then an additional sentence, such as I really love pizza!

pizza_str = ' , '.join(favorite_pizza) # Converts list into separate strings
print(f'I really love pizza! Whether it is {pizza_str} or any flavour, I enjoy eating it.')


# Q35: Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list,
# and then use a for loop to print out the name of each animal.

Animals : list[str] = ['Cow', 'Goat', 'Sheep']

# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
for Animal in Animals:
    print(f'A {Animal} would make a great pet.')

# • Add a line at the end of your program stating what these animals have in common.
# You could print a sentence such as Any of these animals would make a great pet!
animal_str = ' , '.join(Animals)
print(f'These animals {animal_str} are domesticated livestock, they provide us with dairy products. Any of them would make a great pet!')
