# indentation formulation 
# if 5 > 2:
#     print("five is greater than 2")
    
# if 15 < 30:
#     print("thirty is greater than fifteen")

# if 2>1:
#     print("2 is greater than 1")
    
# if 90<100:
#     print("100 is greater than 90")

#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# if 5 > 2:
#   print("Five is greater than two!")
#variable declaration
# x=5
# y="hello world"
# print(x)
# print(y)

#############################################################################
#This is a comment.
# print("Hello, World!")
#############################################################################
#This is a comment
#written in
#more than just one line
# print("Hello, World!")

#triple qoutes comment
# """
# This is a comment
# written in
# more than just one line
# """
# print("Hello, World!")
"""
this is a multiline comment use for

"""
######### variable declaration
# x=5
# y="John"
# print(x)
# print(y) 

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)


"""Casting variables
If you want to specify the data type of a variable, this can be done with casting."""


# x = str(3)
# y = int(3)
# z = float(3)

# print(x)
# print(y)
# print(z)
# x=str("hello-world")
# print(x)

#######################################################################
"""Get the Type
You can get the data type of a variable with the type() function."""
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

###########################################
# x = "John"
# print(x)
# #double quotes are the same as single quotes:
# x = 'John'
# print(x)
###############################################################
#A will not overwrite a
# a = 4
# A = "Sally"
# print(a)
# print(A)
# print(type(a))
# print(type(A))
#############################################################
######legal varibales declaration
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

#######Illegal variable names:###
# 2myvar = "John"
# my-var = "John"
# my var = "John"
#################################################
#Multi Words Variable Names#


# myVariableName = "John"
# MyVariableName = "John" #pascal variable
# my_variable_name = "John" # snake case


#####Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# a,b,c="apple","harry","ron"
# print(a)
# print(b)
# print(c)

########################
"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:"""
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
# a=b=c="harry potter"
# print(a)
# print(b)
# print(c)
################################
''' Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.'''

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# ron =["harry","emma","zaid"]
# a,b,c=ron
# print(a)
# print(b)
# print(c)
#####################################################
###Output VariablesThe Python print() function is often used to output variables.####

# x = "My name is harry potter and i am living in london"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# a="harry"
# b="is"
# c="love"
# print(a,b,c)

#############################################
###You can also use the + operator to output multiple variables:#
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 50
# print(x + y)

'''Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.'''

# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()

#####Create a variable inside a function, with the same name as the global variable
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

########################################
# a = 'Hello'
# b = 'World'
# print(a + " " +b)

# a = 'Hello'
# b = 'World'
# print(a+b)

#######################################################################

'''Python Data Types'''
'''In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:'''

'''Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType'''

##########################################################
# x = 5
# print(type(x))

'''Setting the Data Type
In Python, the data type is set when you assign a value to a variable:'''

# x=str('hello world')
# print(x)

'''------------------------int-value----------------------------------------'''
# x=20
# print(type(x))
# print(x)

'''------------------float-value---------------------------'''
# x=2.5
# print(type(x))
# print(x)
'''------------complex  combination of int and string just like 1j 3e etcetera______________'''
# x=1j
# print(type(x))
# print(x)

'''----------------list _______'''
# x = ["apple", "banana", "cherry"]	
# print(type(x))
# print(x)
'''-----------------tuple____________________'''
# x = ("apple", "banana", "cherry")
# print(type(x))
# print(x)

'''------------------range__________________'''
# x = range(100)
# print(type(x))
# print(x)

'''____________dict___________'''

# x = {"name" : "John", "age" : 36, "address" : "india"}
# print(type(x))
# print(x)

'''_________set___________'''

# x = {"apple", "banana", "cherry"}
# print(type(x))
# print(x)

'''_________________frozen-set'''
# x = frozenset({"apple", "banana", "cherry"})	
# print(type(x))
# print(x)
'''------bool_____'''

# x = True	
# print(type(x))
# print(x)

'''------bytearray_________ '''

# x = bytearray(5)	
# print(type(x))
# print(x)


'''Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:'''

# x = str("Hello World")
# print(x)
# x = int(20)
# print(x)
# x = float(20.5)
# print(x)
# x = complex(1j)
# print(x)
# x = list(("apple", "banana", "cherry"))
# print(x)
# x = tuple(("apple", "banana", "cherry"))
# print(x)
# x = range(6)
# print(x)
# x = dict(name="John", age=36)
# print(x)
# x = set(("apple", "banana", "cherry"))
# print(x)
# x = frozenset(("apple", "banana", "cherry"))
# print(x)
# x = bool(5)
# print(x)

# x = bytearray(5)
# print(x)

# x = memoryview(bytes(5))
# print(x)


'''_______Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:'''
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

'''-----__Import the random module, and display a random number between 1 and 100:'''

# import random

# print(random.randrange(1, 100))


# a = ("Hello how are you , you are 'awesom'")
# print(a)

# b = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(b)





























