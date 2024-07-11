print("ilovetravellingaroundtheworld".index('a'))
# This function returns the first occurence of the string that is being searched in the string. And if the string doesn't have the string searched it will return a valuerror: string not found
my_text = "This is my sample string"
print(my_text.index('m'))
print(my_text.find('m'))
# The difference between index and find is that find is the method which is safe to use and does not cause an error upon value not being found. Instead if the value is not found it return -1.
print(my_text.find('z'))
# We can also pass a second value for which position to start looking for it.
print(my_text.find('s',3))
# We can also pass three arguments and the third argument will determine where to stop
print(my_text.find('s',3,7))