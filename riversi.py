# Python リバーシ

import tkinter             #tkinter:GUI

#windiw
root = tkinter.Tk()        # make window
root.geometry("680x480")  # window Size

#canvas
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.pack()

#define
FONTSIZE = ("",24)
CELLSIZE = 48

#drow
#canvas.create_rectangle(50,150,150,250,fill='Red')

#drow
#canvas.create_oval(250,150,350,250,fill='Blue')

#drow msg
#msg="ABCDEFG"
#canvas.create_text(500,200,text=msg,font=FONTSIZE)


#click
def canvas_click(event):
        xa = event.x
        ya = event.y
        xb = xa + CELLSIZE
        yb = ya + CELLSIZE

        canvas.create_rectangle(xa,ya,xb,yb,fill='Green',width=2)
        d = int(CELLSIZE / 10)
        canvas.create_oval(xa+d, ya+d, xb-d, yb-d, fill='White', width=2)


canvas.bind("<Button-1>", canvas_click)

root.mainloop()           #show window