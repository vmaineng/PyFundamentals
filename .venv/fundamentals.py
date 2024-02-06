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











