import Tkinter,sys

PIXEL = 5         # pixel size

argvs = sys.argv   
argc = len(argvs)  

#  read file into array[][]
fd = open(argvs[1],"r")    # input configuration
array = []
for line in fd:
     conf = line.split()
     array.append(conf)
fd.close()
HEIGHT = len(array)
WIDTH = len(conf)

#  display array
root = Tkinter.Tk()
frm = Tkinter.Frame(root)
cnv = Tkinter.Canvas(frm, width = WIDTH * PIXEL + 3, height = HEIGHT * PIXEL + 3)

for y in range(HEIGHT):
    for x in range(WIDTH):
        if array[y][x] == "0":
            color = "white"
        else:
            color = "black"
        cnv.create_rectangle(x * PIXEL+3, y * PIXEL+3, (x+1)*PIXEL+3, (y+1)*PIXEL+3, fill = color)

cnv.pack()
frm.pack()
root.mainloop()
