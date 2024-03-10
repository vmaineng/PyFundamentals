print("Hello world!") #string = sequence of characters

#print = function built into python and print a message onto the application window

age = 20
print(age)

#instead of camelCase use first_name

#False = boolean false value

#input = built in function read values from the window
name = input("What is your name? ")
print("Hello " + name) #concentation

#string, number, and boolean = data type

#typeError: int vs str

birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year) #have to wrap int around birth_year b/c it's a string
print(age)

#built in function:
#float() = convert value to a floating point number
#bool() = convert value to boolean
#str()
#int()

#calculator:
first = input("type in first number ")
second = input("type in second number ")
sum = int(first) + int(second)
print (sum)

#methods = functions tied to the object
course = 'PYthon for Beginners' #strings are 0 index
print(course.find('y'))
#strings are immutable

#print( python in course) => true

#// gives you a whole number
print (10 // 3)

#/ gives you a floating number
print (10/ 3)

#moduolo operator
print (10 % 3)

#exponent operator
print (10**3)

#augmented operator
x = 10
x = x + 3
x += 3 #this is the augumented operator

#operator precedence (tells you which operator goes first - 'my dear aunt sally')
x = 10 + 3 * 2
#x = 16

#comparison operator = >, <, >=, <=, == (equality operator), != (not equality operator)

#logical operator (and (both expressions return true), or(at least one of the expression is true), not(inverts the value))
price = 25
print (price > 10 or price < 30)

print (not price >10)

#if stmts
temp = 35
if temp > 30:
    print("it's a hot day") #have to use double quotes to tell Python there's an apostrophe in the string
elif temp > 50:
    print("it's a nice day")
else:
    print("it's cold")
print("Done")
#use indentaion to represent a block of cold - if stmts
#no brackets needed


weight = int(input("weight:" )) #turn the string into a number
unit = input("(K)g or (L)bs: ")
if (unit.upper()) == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs " + str(converted)) #use 'str' function to turn the float into a string

#to enter a new line, press shift + tab ; i.e.: the else stmt

# can't do '+' with string and floats
# can do i * '*"

i = 1
while i <= 5: #will keep running til it's no longer true
    print(i)
    i = i + 1

i = 1
while i <= 1_000: #makes code more readable, it's 1000
    print(i)
    i = i + 1

i = 1
while i <= 5: #will keep running til it's no longer true
    print(i * '*')
    i = i + 1

#data types - primitive types
1 #number
1.1 #float
True #boolean
'a' #string

#lists
names = ["John", "bob", "Mary" ]
print(names) #["John", "bob", "Mary"]
print(names[0:2]) #["John", "bob"]


#add value
numbers.insert(6, 4) #at the 6th index, add in 4

#delete value
numbers.remove(4) #removes the integer

#remove all items
numbers.clear() #makes list empty

#check if the numbers exist
print(10 in numbers) #check if 10 exists in number's array

#check length
print(len(numbers)) #len is a print in function; returns length

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

i = 0;
while i < len(numbers): #have to grab each value from the while loop
    print(numbers[i])

#range function - generate a sequence of numbers
numbers = range(5) #range(0, 5)
for number in numbers:
    print(number) #0, 1,2,3,4,5

numbers = range(5, 10)
for number in numbers:
    print(number) #5, 6, 7, 8 , 9, 10

numbers = range(5, 10, 2)
for number in numbers:
    print(number) #5, 7, 9

# so can write range in the for loop
for number in range(5, 10):
    print(number)

#tuples - can't be immutable; can't add, remove
#has count and index
#has magic methods















