from tkinter import *




def showPosEvent(event):


  print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))



def showAllEvent(event):

    print(event)
    for attr in dir(event):
      if not attr.startswith('__'):
        print(attr, '=>', getattr(event, attr))


def onKeyPress(event):

    print('Got key press: ', event.char)


def onArrowKey(event):

    print('Got return key press')


def onLeftClick(event):

    print('Got left mouse button click:', end=' ')


    showPosEvent(event)

def onRightClick(event):

    print('Got right mouse button click:', end=' ')

    showPosEvent(event)



def onMiddleClick(event):

    print('Got middle button click: ', end=' ')
    showPosEvent(event)
    showAllEvent(event)




def onLeftDrag(event):

    print('Got left mouse button drag: ', end=' ')
    showPosEvent(event)


def onDoubleLeftClick(event):

    print('Got double left mouse click: ', end=' ')
    showPosEvent(event)

    tkroot.quit()



