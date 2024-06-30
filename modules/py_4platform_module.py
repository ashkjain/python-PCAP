# The platform module can help you with the version of the software, Operating System, and the hardware that is being used.
# This module can help us with some basic information about the underlying layers.
import platform

from platform import platform
# The platform function return the information about the Operating System that is working on.
print(platform())
# We can provide two values for parameter either trur or false, and the first value is for the alias, and the second value is for terse. By default the values are set to false.
print(platform(aliased=True, terse=False))
# The aliased parameter will return the alias if available and the terse parameter will make the string shorter and gives the only information that is required.

from platform import machine
# This function return the name of the information about the processor architecture.
print(machine())

from platform import processor
# This function returns the name of the processor that is being used (Real Name)
print(processor())

from platform import system
# This function return the string of the Generic Operating System Name
print(system())

from platform import python_implementation
# This function returns the string of the name of the implemetation of the Python like: jython, cpython, ironpython and more
print(python_implementation())

from platform import python_version_tuple
# This function returns a tuple with the version of the python. First element return major python version, second element is minor part and the third and last returns the patch.
print(python_version_tuple())

from platform import python_version
# This function return the single string of the release version
print(python_version())

# last two functions are important because in exam these can be confusing.