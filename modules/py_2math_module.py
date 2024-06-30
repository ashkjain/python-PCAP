import math

for name in dir(math):
    print(name,end="\t")
print("\n")

# There are various functions that we can use from math module but for PCAP we need to focus on at least these three: ceil, floor, trunc
from math import ceil, floor, trunc

x:float = 3.6
print(ceil(x)) # Always round the number to the closest upper nearest integer
print(floor(x)) # Always round the number to the closest lower nearest integer
print(trunc(x)) # It truncates the floating point number and leaves it to an integer
y:float = -3.6
print(ceil(y)) # When the number is negative it still goes for the uppter but in this case it will be opposite than poisitve
print(floor(y)) # It will go the other way since the numbers are negative
print(trunc(y)) # It still remains the same

from math import factorial

print(factorial(10)) # 1*2*3*4*5*6*7*8*9*10
print(factorial(5)) #1*2*3*4*5
# Only thing that is not acceptable with this function is negative numbers

from math import sqrt
print(sqrt(9)) # This returns the square root of the given number (But not negative numbers)

from math import hypot
print(hypot(9,3)) # This function takes two argument as a parameter and returns the hypotenuse of the given numbers