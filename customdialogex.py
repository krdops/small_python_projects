import sys
from tkinter import *
makemodal = (len(sys.argv) > 1)


def dialog():

  win = Toplevel()
  Label(win, text='Hard drive reformatted!').pack()
  Button(win, text="OK", command=win.destroy).pack()
  
  if makemodal:
    win.focus_set() #take over input focus
    win.grab_set() #disable why this is open
    win.wait_window() #wait here till destroyed

  print('Dialog exit')




root = Tk()


Button(root, text='popup', command=dialog).pack()

root.mainloop()


