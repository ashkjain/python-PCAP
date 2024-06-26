# Libraries can be imported like these two examples.
import sys
import math
# or
import sys, math

# If you want to know about the methods or function that are available in the module pack, you can use the dir function and pass the library as a parameter and it will return all the functions that are availabel to use in the library.
""" for name in dir(sys):
    print(name, end="\t") """

# If you try to use an entity from the library that does not exist, it will return an Attribute Error.
# sys.exit3()

# This function from the system library exit the program.
# sys.exit()

# If we are using the module very frequently in our code, what we can do is we can call that entity as whole and use it without using dot notation and referring the name of the library before.
from sys import exit

# But if we are calling the function like that and if we are creating our own function with the same name, during invocation Python will refer to the latest created function which is going to be recently created one. Look at the example below:-
from sys import exit
def exit():
    print("I Wanna Exit")

exit()

# There are two other ways to import everything from the library. 
from sys import *
import sys
# In the first case you can use all the functions inside the sys directly like you call your own defined function. But in the second case you need to use the 'sys.' prefix before calling the function.

# We can also give aliases to our functions and library to use in the program:-
import sys as s
from sys import exit as bye
# For the first case we can use the functions in the sys library by using the prefix 's.' instead of typing whole library name. In the second case we imported specific function and gave it an alias, so we can use the function called exit now as bye.
bye()