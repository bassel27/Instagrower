from tkinter import *
from tkinter import ttk
from Igbot import *
from tkinter import messagebox
import os 
import glob
from tkinter import filedialog  #allows you to open and save files or folders


igbot = Igbot()

class Tkinter:
    def __init__(self, root):
        self.root = root
    
    def deleteConfig(self):
        try:
            cookie_del = glob.glob("config/*cookie.json")   #Return a list of path names that match pathname
            os.remove(cookie_del[0])
        except:
            pass

    def frameWelcome(self):
        self.frameWelcome = LabelFrame(self.root)
        self.frameWelcome.grid(row = 1, column = 0)
        Label(self.root, text = "Instagrower").grid(row = 0, column = 0)
    
    def whichAccount(self):        
        self.valueInside = StringVar(self.frameWelcome)  #Variable to keep track of the option selected in OptionMenu
        self.valueInside.set("fake_account")     # default value
        Label(self.frameWelcome, text = "Which account?").grid(row = 0, column =0)
        accDropDown = ttk.OptionMenu(self.frameWelcome, self.valueInside, "longlivebassel")
        accDropDown.grid(row = 0, column = 1)
    
    def nextButton(self):
        def clickNext():
            igbot.login(self.valueInside.get())
            del self.valueInside
            self.frameWelcome.destroy()
            del self.frameWelcome
            self.displayFrameChoose()
        nextButton = ttk.Button(self.frameWelcome, text = "Next", command = clickNext)
        nextButton.grid(row = 1, column = 1)

    def browseImg (self):
        self.fileAddress = filedialog.askopenfilename(initialdir = 'Downloads', title = "Select a photo", filetypes = (("image", ".jpeg"), ("image", ".jpg")))       # to open a file explorer, use the method askopenfilename()

    def afterUpload(self):
        os.rename(self.fileAddress, self.fileAddress[:-10])
        del self.fileAddress
    
    

    def displayFrameUploadPhoto(self):
        self.frameChoose.destroy()
        frameUploadPhoto = LabelFrame(self.root)
        frameUploadPhoto.grid(row = 1, column =0)
        textCaption = Text(frameUploadPhoto, borderwidth = 3, height = 13, width = 35)
        textCaption.grid(row =0, column = 0)
        buttonBrowse = ttk.Button(frameUploadPhoto, text = "Browse", command = self.browseImg).grid(row = 1, column = 0)
        buttonUpload= ttk.Button(frameUploadPhoto, text = 'Upload', command = lambda : [igbot.uploadPhoto(self.fileAddress, textCaption.get("1.0",'end-1c')), self.afterUpload()]).grid(row = 2, column = 0)
        buttonRetrun = ttk.Button(frameUploadPhoto, text = "Return to main menu", command = [frameUploadPhoto.destroy(), self.displayFrameChoose()])
        def Focusin(event):  
            if textCaption.get("1.0",'end-1c') == 'Enter your caption...':
                textCaption.delete(0, "end") # delete all the text in the entry
                textCaption.insert(0, '') #Insert blank for user input
                textCaption.config(fg = 'black')
        def Focusout(event):
            if textCaption.get("1.0",'end-1c') == '':
                textCaption.insert(0, 'Enter your caption...')
                textCaption.config(fg = 'grey')
                
        textCaption.bind('<FocusIn>', Focusin)
        textCaption.bind('<FocusOut>', Focusout)
        
        
    
    def frameSendMsg(self):
        self.frameChoose.destroy()
        frameSendMsg = LabelFrame(self.root).grid(row = 0, column =0)


    def displayFrameChoose(self):
        self.frameChoose = LabelFrame(self.root)
        self.frameChoose.grid(row = 0, column = 0)
        Label(self.frameChoose, text = "Main Menu").grid(row = 0, column = 1)
        buttonUploadPhoto = ttk.Button(self.frameChoose, text= 'Upload a photo', command = self.displayFrameUploadPhoto).grid(row = 1, column =0)
        Label(self.frameChoose, text = " ").grid(row = 0, column = 1)
        buttonSendMsg = ttk.Button(self.frameChoose, text = 'Send a message', command = self.frameSendMsg).grid(row = 1, column = 2)
        
    def ifExit(self):
        def doSomethingOnExit():
            response = messagebox.askyesno("Exit program", "Are you sure you want to exit?")
            if response == 1:
                self.root.destroy()
            else:
                pass
        self.root.protocol('WM_DELETE_WINDOW',doSomethingOnExit)