# Variables
# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.


# Eg:
x = 5
y = "John"
print(x)
print(y)


# Eg:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))


# Variable Names
# Variable names in Python must begin with a letter or an underscore (_).
# They cannot start with a number.
# Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
# Python variable names are case-sensitive, meaning age, Age, and AGE would be treated as distinct variables.
# Variable names cannot be Python keywords.

# Global Variables

# Variables created outside of any function, as shown in previous examples, are referred to as global variables.
# Global variables are accessible to all parts of a program, including inside functions as well as outside them.

x = "epic"

def myfunc():
  print("Python is " + x)

myfunc()