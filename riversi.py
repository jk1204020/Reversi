# Python リバーシ

import tkinter             #tkinter:GUI

#windiw
root = tkinter.Tk()        # make window
root.geometry("576x480")  # window Size

#canvas
canvas = tkinter.Canvas(root, width=576, height=480)
canvas.pack()

#define
FONTSIZE = ("",24)
CELLSIZE = 48         #1ますのピクセル数
BOADDW = 8
OFSX = 2 * CELLSIZE
OFSY = 1 * CELLSIZE
TYPE_NONE = 255
TYPE_BLACK = 0
TYPE_WHITE = 1
turn = TYPE_BLACK
passcnt = 0
endflag = False

board = bytearray(BOADDW * BOADDW)

prayertbl = ["黒","白"]
colortbl = ["Black","White"]

#vectol
vectable = [
        ( 0,-1),
        ( 1,-1),
        ( 1, 0),
        ( 1, 1),
        ( 0, 1),
        (-1, 1),
        (-1, 0),
        (-1,-1)
]

def setpiece(pos, num):
        index = (pos[1]*BOADDW)+pos[0]
        board[index] = num

def getpiece(pos):
        index = (pos[1]*BOADDW)+pos[0]
        return board[index]

def moveposition(pos, vectol):
        x = pos[0] + vectable[vectol][0]
        y = pos[1] + vectable[vectol][1]
        return (x,y)

def initboard():
        global turn, passcnt, endflag
        for y in range(BOADDW):
                for x in  range(BOADDW):
                        setpiece((x,y), TYPE_NONE)
        setpiece((3, 3), TYPE_BLACK)
        setpiece((4, 3), TYPE_WHITE)
        setpiece((3, 4), TYPE_WHITE)
        setpiece((3, 4), TYPE_BLACK)
        passcnt = 0
        endflag = False
        redraw()


def serch(pos, vectol, num):
        piece=0
        while True:
                pos = moveposition(pos, vectol)
                if isinside(pos) == False:
                        return 0
                if getpiece(pos) == TYPE_NONE:
                        return 0
                if getpiece(pos) == num:
                        break
                piece += 1
        return piece

def isinside(pos):
        if pos[0]<0 or pos[0]>=8: return False
        if pos[1]<0 or pos[1]>=8: return False
        return True


def drawpiece(pos, num):
        xa = pos[0] * CELLSIZE + OFSX
        ya = pos[1] * CELLSIZE + OFSY
        xb = xa + CELLSIZE
        yb = ya + CELLSIZE
        canvas.create_rectangle(xa, ya, xb, yb, fill='Green', width=2)
        if num == TYPE_NONE: return
        d = int(CELLSIZE /10)
        canvas.create_oval(xa + d, ya + d, xb - d, yb - d, fill=colortbl[num], width=2)


for y in range(BOADDW):
        for x in range(BOADDW):
                drawpiece((x,y),getpiece((x,y)))

piece = serch((3,3),2,TYPE_BLACK)
msg = "Result:" + str(piece)
canvas.create_text(288,456,text=msg,font=FONTSIZE)


'''
def drawrect(pos,color):
        xa = pos[0] * CELLSIZE
        ya = pos[1] * CELLSIZE
        xb = xa + CELLSIZE
        yb = ya + CELLSIZE
        canvas.create_rectangle(xa,ya,xb,yb,fill=color,width=2)
'''

#click
def canvas_click(event):
        xa = event.x - OFSX
        ya = event.y - OFSY
        pos = (x,y)

        if endflag == True:
                initboard()
                return

        if passcnt >0:
                nextturn()
                redoraw()
                return

        if isinside(pos)



        canvas.create_rectangle(xa,ya,xb,yb,fill='Green',width=2)
        d = int(CELLSIZE / 10)
        canvas.create_oval(xa+d, ya+d, xb-d, yb-d, fill='White', width=2)


#canvas.bind("<Button-1>", canvas_click)
'''
startpos = (5,5)
drawrect(startpos, 'Red')
for vec in range(8):
        temppos = startpos
        for i in range(4):
                temppos = moveposition(temppos,vec)
                drawrect(temppos, 'Cyan')

'''

root.mainloop()           #show window