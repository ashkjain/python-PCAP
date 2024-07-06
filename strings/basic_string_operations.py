# String are immutable, which means that it cannot be manipulated. Which means cannot be shrinked or extended, but can be redeclared.
print(len('Hi There')) # Return the lenght including Whitespace
print(len('')) # THis will retrun nothing but '0' because there is no whitespace or characters in between the quotes.

# String can be treated as list, but things that are applicable to list, won't be applicable to string. Some functions and methods will work but strings have limited functionallity since they are immutable.

some_string = "Hi There!"
print(some_string[1])
print(some_string[1:])