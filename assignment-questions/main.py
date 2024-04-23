# Q2: Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be
#  simple, such as, “Hello Eric, would you like to learn some Python today?”

person_name : str = 'Sabeh Shaikh'
print("Hello" , person_name , "would you like to learn some Python today?")

# Q3: Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

print("lowercase:" , person_name.lower())
print("uppercase:" , person_name.upper())
print("titlecase:" , person_name.title())

# Q4: Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

quote : str = "A person who never made a mistake never tried anything new."
print(f'Albert Einstein once said, "{quote}"')

# Q5: Famous Quote 2: Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person.
# Then compose your message and store it in a new variable called message. Print your message.

famous_person : str = "Quaid e Azam"
message : str = "With faith, discipline and selfless devotion to duty, there is nothing worthwhile that you cannot achieve"
print(f'{famous_person} once said, "{message}"')

# Q6: Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once. Print the name once,
# so the whitespace around the name is displayed. Then print the name after striping the white spaces.

person = " \t  Sabeh Shaikh  \n  "
print("With Whitespaces:", person)
print("Without Whitespaces:", person.strip())

# Q7: Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8.
# Be sure to enclose your operations in print statements to see the results.

print("Addition:" , 5 + 3)
print("Subtraction:" , 10 - 2)
print("Multiplication:" , 4 * 2)
print("Division:" , 16 / 2)

# Q9 : Favorite Number: Store your favorite number in a variable. Then, using that variable, 
# create a message that reveals your favorite number. Print that message.

fave_number : int = 15
print(f"favorite number: {fave_number}")

# Q10: Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have
# anything specific to write because your programs are too simple at this point, just add your name and the current date
# at the top of each program file. Then write one sentence describing what the program does.

#  Sabeh, this program determines area of the rectangle:
length = 5  # Length of the rectangle
width = 3   # Width of the rectangle
area = length * width  # Calculate the area

print(f'The area of the rectangle is {area}.')  # Print the area

# Q11: Names: Store the names of a few of your friends in a array called names. Print each person’s name 
# accessing each element in the list, one at a time.

names : list[str] = ['Sabeh', 'Ronaldo', 'Messi', 'Mbappe']
for name in names:
    print(name)

# Q12: Greetings: Start with the array you used in Exercise 11, but instead of just printing each person’s name,
#  print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name.
for name in names:
    print(f'Hello {name}')

# Q13: Your Own Array: Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. Use your list to print a series of statements 
# about these items, such as “I would like to own a Honda motorcycle.”

transportation = ["Honda motorcycle", "Tesla Model S", "double-decker bus", "high-speed bullet train"]

for mode in transportation:
  print(f"I would like to own a {mode}.")









