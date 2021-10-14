from tkinter import *
from Tkinter import *

root = Tk()
root.title('Instagrower')
root.iconbitmap('igIcon.ico')
tkinter = Tkinter(root)

tkinter.deleteConfig()
tkinter.frameWelcome()
tkinter.whichAccount()
tkinter.nextButton()
tkinter.ifExit()

root.mainloop()