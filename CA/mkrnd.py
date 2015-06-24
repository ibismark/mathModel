import random,sys

argvs = sys.argv 
argc = len(argvs)  

SIZE = int(argvs[1])

for x in range(SIZE):
    sys.stdout.write(str(random.randint(0,1))+" ")
print("")   # print new line
