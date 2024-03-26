*Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

**Get the Type
You can get the data type of a variable with the type() function.

Example
x = 5
y = "John"
print(type(x))
print(type(y))

** Single or Double Quotes?
String variables can be declared either by using single or double quotes:
variables names must be case sensitive
Example
x = "John"
# is the same as
x = 'John'

**Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

**Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
example2:
x = y = z = "Orange"
print(x)
print(y)
print(z)
