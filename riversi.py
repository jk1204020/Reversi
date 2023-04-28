# Python リバーシ

import tkinter             #tkinter:GUI

#define
CELLSIZE = 48         #1ますのピクセル数
FONTSIZE = ("",24)
BOADDW = 8
OFSX = 2 * CELLSIZE
OFSY = 1 * CELLSIZE
TYPE_BLACK = 0
TYPE_WHITE = 1
TYPE_NONE = 255
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

def initboard():
        global turn, passcnt, endflag
        for y in range(BOADDW):
                for x in  range(BOADDW):
#                        setpiece((x,y), TYPE_NONE)
                        setpiece((x, y), TYPE_NONE)
        setpiece((3, 3), TYPE_BLACK)
        setpiece((4, 3), TYPE_WHITE)
        setpiece((3, 4), TYPE_WHITE)
        setpiece((4, 4), TYPE_BLACK)

        turn = TYPE_BLACK
        passcnt = 0
        endflag = False
        redraw()

#click
def canvas_click(event):
        if endflag == True:
                initboard()
                return

        if passcnt >0:
                nextturn()
                redraw()
                return

        x = int((event.x - OFSX) / CELLSIZE)
        y = int((event.y - OFSY) / CELLSIZE)
        pos = (x,y)

        if isinside(pos)==False:
                return
        if turnnablepiece(pos, turn)==0:
                return
        for vectol in range(8):
                loopcount = serch(pos,vectol,turn)
                temppos = pos
                for i in range(loopcount):
                        temppos = moveposition(temppos, vectol)
                        setpiece(temppos, turn)

        setpiece(pos,turn)
        nextturn()
        redraw()


def nextturn():
        global passcnt, endflag, turn
        turn ^= 1
        empty = 0
        for y in range(BOADDW):
                for x in range(BOADDW):
                        if getpiece((x,y)) == TYPE_NONE: empty+=1
                        if turnnablepiece((x,y),turn)>0:
                                passcnt=0
                                return

        if empty == 0:
                endflag=True
                return

        passcnt += 1
        if passcnt >=2:
                endflag = True


def moveposition(pos, vectol):
        x = pos[0] + vectable[vectol][0]
        y = pos[1] + vectable[vectol][1]
        return (x,y)

def turnnablepiece(pos,num):
        if getpiece(pos) != TYPE_NONE:
                return 0

        total = 0
        for vectol in range(8):
                total+=serch(pos,vectol,num)
        return total

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
        #盤面
        canvas.create_rectangle(xa, ya, xb, yb, fill='Green', width=2)
        if num == TYPE_NONE: return
        d = int(CELLSIZE /10)
        canvas.create_oval(xa+d, ya+d, xb-d, yb-d, fill=colortbl[num], width=2)

def redraw():
        #外枠
        canvas.create_rectangle(0,0,576,480,fill="Khaki1")
        black=0
        white=0

        for y in range(BOADDW):
                for x in range(BOADDW):
                        pos = (x,y)
                        num = getpiece(pos)
                        if num == TYPE_BLACK: black+=1
                        if num == TYPE_WHITE: white+=1
                        drawpiece(pos,num)
                        assist(pos,turn)
        msg = "黒"+str(black) + "　対　白" + str(white)
        canvas.create_text(288, 456, text=msg, font=FONTSIZE)
        msg = prayertbl[turn]+"の番です"
        if passcnt>0:
                msg += "(パス)"
        if endflag == True:
                msg = "終了です"

        canvas.create_text(288, 24, text=msg, font=FONTSIZE)

def assist(pos, num2):
        piece = turnnablepiece(pos, num2)
        if piece == 0:return
        x = pos[0] * CELLSIZE + OFSX + int(CELLSIZE / 2)
        y = pos[1] * CELLSIZE + OFSY + int(CELLSIZE / 2)
        canvas.create_text(x, y, text=str(piece), font=FONTSIZE, fill='Yellow')

#windiw
root = tkinter.Tk()        # make window
root.title("Riversi")
root.geometry("576x480")  # window Size

#canvas
canvas = tkinter.Canvas(root, width=576, height=480)
canvas.pack()
canvas.bind("<Button-1>",canvas_click)
initboard()
root.mainloop()           #show window