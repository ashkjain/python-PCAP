# String are immutable, which means that it cannot be manipulated. Which means cannot be shrinked or extended, but can be redeclared.
print(len('Hi There')) # Return the lenght including Whitespace
print(len('')) # THis will retrun nothing but '0' because there is no whitespace or characters in between the quotes.

# String can be treated as list, but things that are applicable to list, won't be applicable to string. Some functions and methods will work but strings have limited functionallity since they are immutable.

some_string = "Hi There!"
print(some_string[1]) # Will return the element at position 1
print(some_string[1:]) # Will return the element from position 1 through end
print(some_string[:5]) # Will return the elements from '0' to 4th element
print(some_string[3:6]) # Will return the elements from 3 to 5 not including 6 as same as list.
print(len('I\'m Ash')) # This will return 7 elements, because we are using escaping sequence, and only the apostrophe is being counted not the slash.

# ord function takes the characters as an input and returns the ASCII value of it. If value in not provided will return ValueError
print(ord('a')) # Will Return 97
print(ord('A')) # Will return 65
# chr function takes the number and return the character based on the ASCII table. If value is not provided or the value in negative or not a number, it will return ValueError or TypeError
print(chr(97)) # Will return lowercase 'a'

# This code will throw an error, but if multiple line string needs to be passed, we can use two ways either '''some string''' or """Some String """
""" test_string = 'Line1
Line 2' """
test_string = """This is 
the multiple string"""
# WHen you pass it in len function it will return the length but you will see an addition, because when we are moving to the next line, and what is causing is this is this \n which is counted as next line.
print(len(test_string))

# We can add strings or in another words concatenation
print('aaa'+'bbb')
# We can use the multiplication to replicate nth number of times
print('aaa'*2)

# We can also do some iteration with and on strings like this:-
for i in "This is the string":
    print(i,end="-")
print("\n")

# We cannot remove a certain part of the string use indices like this:-
temp_string = "Hello"
# del temp_string[1]
# But we can remove it as a whole 
del temp_string
# If now we try to print it or use the temp_string variable we will receive an error because it does not exist anymore.
# print(temp_string)

# min() function takes the string and return the value with the lowest ASCII value inside of it.
print(min("abfddsinodnA"))
print(min("This is space"))
# max() function takes the string and return the value with the highest ASCII value inside of it.
print(max("abfddsinodnA"))