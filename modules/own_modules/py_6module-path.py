import sys
print(sys.path)
# This standard library function return list of all locations that where it check for modules.

# We can also change the path and set it to some other location other than the standard library location.

# import secret_module
# The above import will cause an error because the path is not part of the standard location.
# We can use the append function for path since it returns list and set pass the name of the folder, in this case which is 'secret'.
sys.path.append('secret')
import secret_module
# Now everything works fine, and we cannot only set relative path as we did, we can also set absolute path which will be the full address of that location.