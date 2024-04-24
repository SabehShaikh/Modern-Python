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

transportation : list[str] = ["Honda motorcycle", "Tesla Model S", "double-decker bus", "high-speed bullet train"]

for mode in transportation:
  print(f"I would like to own a {mode}.")

# Q14: Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes
# at least three people you’d like to invite to dinner. use your list to print a message to each person, inviting them to dinner.  

guest_list : list[str] = ['Vinicius' , 'Rodrygo' , 'Jude Bellingham']
for guest in guest_list:
   print(f'{guest} I would like to invite you for dinner.')

# Q15: Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 14. Add a print statement at the end of your program stating the name of the guest who can’t make it.
unavailable_guest = 'Rodrygo'
new_guest = 'Modric'
print(f'{unavailable_guest} is unavailable.')
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guest_list[guest_list.index(unavailable_guest)] = new_guest
# • Print a second set of invitation messages, one for each person who is still in your list.
for guest in guest_list:
   print(f'Changed GuestList: {guest} I would like to invite you for dinner.')

# Q16: More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 15. Add a print statement to the end of your program informing 
# people that you found a bigger dinner table.
print("Congratulations bigger dinner table is found.")

# • Add one new guest to the beginning of your array.
guest_list.insert(0, 'Lunin' )

# • Add one new guest to the middle of your array. 
middle_index = len(guest_list) // 2 # Floor Division: 
# The // operator performs floor division. It divides the elements in len(guest_list) by 2 and discards any remainder.
# The result is always a whole number (integer).
guest_list.insert(middle_index, 'Toni Kroos')

# • Use append() to add one new guest to the end of your list.
guest_list.append('Rudiger')

#  • Print a new set of invitation messages, one for each person in your list.
for guest in guest_list:
   print(f'Big guestList: {guest} , Would you like to come for dinner tonight?')

# Q17: Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# • Start with your program from Exercise 16. Add a new line that prints a message saying that you can invite only two people for dinner.
print("Sad news, we can only invite two people for dinner.")

# • Remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
while(len(guest_list) > 2):
   removed_guest = guest_list.pop()
   print(f'{removed_guest} sorry for removing you.')

# • Print a message to each of the two people still on your list, letting them know they’re still invited.
for guest in guest_list:
   print(f'{guest} you are still invited.')

# • Remove the last two names from your list, so you have an empty list.
del guest_list[0:2]
#  Print your list to make sure you actually have an empty list at the end of your program.
print(guest_list)

# 19-Dinner Guests: Working with one of the programs from Exercises 14 through 18,
#  print a message indicating the number of people you are inviting to dinner.
print("No of people invited for dinner:" , len(guest_list))

# Q18: Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a array. Make sure the array is not in alphabetical order.

five_stadiums: list[str] = ['Emirates Stadium', 'Santiago Bernabéu', 'Allianz Arena', 'King Fahd Stadium', 'Old Trafford']

# Print your array in its original order.
# print("Original order:" , *five_stadiums)
print("Original order:" , ' , '.join(five_stadiums))


# • Print your array in alphabetical order without modifying the actual list.
sorted_stadiums = sorted(five_stadiums) # created new sorted list, leaving the original one unchanged.
print("Alphabetical order:", sorted_stadiums)

# • Show that your array is still in its original order by printing it.
print("Still In Original order:" , five_stadiums)

# • Print your array in reverse alphabetical order without changing the order of the original list.
reversed_sorted_stadiums = sorted(five_stadiums , reverse=True)
print("Reverse alphabetical order:" , reversed_sorted_stadiums)

# • Show that your array is still in its original order by printing it again.
print("Still In Original order:" , five_stadiums)

# • Reverse the order of your list. Print the array to show that its order has changed.
five_stadiums.reverse()
print("Reverse order:" , five_stadiums )

# • Reverse the order of your list again. Print the list to show it’s back to its original order.
five_stadiums.reverse()
print("Back to original order:" , five_stadiums)

# • Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.
five_stadiums.sort()
print("Alphabetical order with modifying list:" , five_stadiums)

# • Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
five_stadiums.sort(reverse=False)
print("Reverse alphabetical order again:" , five_stadiums)

# Q20: Think of something you could store in a array. For example, you could make a list of mountains, rivers, countries, cities,
#  languages, or anything else you’d like. Write a program that creates a list containing these items.

mountains: list[str] = ["Mount Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]
rivers: list[str] = ["Nile", "Amazon", "Yangtze", "Mississippi", "Danube"]
countries: list[str] = ["Japan", "Palestine", "Germany", "Australia", "Russia"]
cities: list[str] = ["Tokyo", "Jerusalem", "Berlin", "Sydney", "Moscow"]
languages: list[str] = ["English", "Mandarin Chinese", "Spanish", "Urdu", "Arabic"]

print("Mountains:", mountains)
print("Rivers:", rivers)
print("Countries:", countries)
print("Cities:", cities)
print("Languages:", languages)


# Q21: They think of something you could store in a TypeScript Object. Write a program that creates Objects containing these items.
footballer = {
    'name': 'Cristiano Ronaldo',
    'position': 'Forward',
    'nationality': 'Portuguese',
    'age': 39,
    'club': 'Al-Nassr'
}
print(footballer)

# Q22: Intentional Error: If you haven’t received an array index error in one of your programs yet, try to make one happen.
# Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

myArr: list[str] = ['One', 'Two', 'Three', 'Four']
#Accessing an index that doesn't exist, will print undefined
# print(myArr[5])
# Make sure you correct the error before closing the program.
print(myArr)

# Q23: Conditional Tests: Write a series of conditional tests. Print a statement describing each test 
# and your prediction for the results of each test. Your code should look something like this:
car = 'subaru'
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
# Test 1: Equality (==)
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # Output: True

# Test 2: Not Equal (!=)
print("Is car != 'honda'? I predict False.")
print(car != 'honda')  # Output: True

# Test 3: Regular Equality (==) - checks type and value
print("Is car == 'toyota'? I predict False.")
print(car == 'toyota')  # Output: False (regular equality is sufficient)

# Test 4: Accessing first character (charAt() equivalent)
print("Is car[0] == 's'? I predict True.")
print(car[0] == 's')  # Output: True (access first character using indexing)

# Test 5: Not Equal (!=)
print("Is car != 'subaru'? I predict False.")
print(car != 'subaru')  # Output: False

# Test 6: String length (length property)
print("Is len(car) == 6? I predict True.")
print(len(car) == 6)  # Output: True (use `len()` for string length)

# Test 7: String length comparison (alternative)
print("Is len(car) == 5? I predict False.")
print(len(car) == 5)  # Output: False (correct usage of `len()`)

# Test 8: Convert to uppercase (toUpperCase() equivalent)
print("Is car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')  # Output: True (use `upper()` for uppercase)

# Test 9: Regular equality after conversion
print("Is car == 'Tesla'? I predict False.")
print(car == 'Tesla')  # Output: False

