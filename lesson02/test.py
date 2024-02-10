import mymod
import mymod as mm
from mymod import var, DoThis

print(mymod.var)
mymod.DoThis()

print(mm.var)
mm.DoThis()

print(var)
DoThis()