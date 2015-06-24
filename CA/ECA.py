import sys  # sys module 

argvs = sys.argv 
argc = len(argvs) 

RULE = int(argvs[1])   # rule no.
STEPS = int(argvs[2])  # toal no. of steps

# make rule table
rule =[0] * 8      # rule[0..7]   rule[0]<=000, rule[7]<=111
for i in range(8):   # create list [0 1 ... 7 ]
   rule[i] = RULE % 2
   RULE = RULE // 2

#print(rule)

# read initial configuration
fd = open(argvs[3],"r") 
buff = fd.readline()
fd.close()

confStr = nextConf = buff.split()  # split cnfstr into token
CELLS = len(confStr)         # the no. of cells
conf = list(map(int,confStr))  # string list -> int list
print(" ".join(map(str,conf)))

# transiton
for step in range(STEPS-1):
     for x in range(CELLS):
           nextConf[x] = rule[ conf[(x-1+CELLS) % CELLS] * 4 + conf[x] * 2 + conf[(x+1)%CELLS] ]
     conf = list(nextConf)
     print(" ".join(map(str,nextConf)))
