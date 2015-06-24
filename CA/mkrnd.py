#################################
#  pseudo random number generator
#  seed is system time
#  Usage : mkrnd.py size
#################################
import random,sys

argvs = sys.argv   # command line argument list
argc = len(argvs)  # the no. of arguments

SIZE = int(argvs[1])

for x in range(SIZE):
    sys.stdout.write(str(random.randint(0,1))+" ")
print("")   # print new line
