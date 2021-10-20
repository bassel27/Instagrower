from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 
import glob
from instabot import Bot
from checklistcombobox import *
from instadm import InstaDM

bot = Bot()

class Tkinter:
    def __init__(self, root):
        self.root = root
    
    def deleteConfig(self):
        try:
            cookie_del = glob.glob("config/*cookie.json")   #Return a list of path names that match pathname
            os.remove(cookie_del[0])
        except:
            pass
        
    def displayFrameChoose(self):
        self.frameChoose = LabelFrame(self.root)
        self.frameChoose.grid(row = 0, column = 0)
        Label(self.frameChoose, text = "Main Menu").grid(row = 0, column = 1)
        Label(self.frameChoose, text = " ").grid(row = 0, column = 1)
        buttonSendMsg = ttk.Button(self.frameChoose, text = 'Send a message', command = self.frameSendMsg).grid(row = 1, column = 0)
        
    
    def frameSendMsg(self):
        def textMsgStuff(frameSendMsg):
            global textMsg
            textMsg = Text(frameSendMsg, borderwidth = 3, height = 10, width = 35)
            textMsg.pack()
            textMsg.insert(1.0, 'Enter your message...')
            textMsg.config(fg = 'grey')

            def Focusin(event):  
                if textMsg.get("1.0",'end-1c') == 'Enter your message...':
                    textMsg.delete(1.0, "end") # delete all the text in the entry
                    textMsg.insert(1.0, '') #Insert blank for user input
                    textMsg.config(fg = 'black')
            def Focusout(event):
                if textMsg.get("1.0",'end-1c') == '':
                    textMsg.insert(1.0, 'Enter your message...')
                    textMsg.config(fg = 'grey')
                    
            textMsg.bind('<FocusIn>', Focusin)
            textMsg.bind('<FocusOut>', Focusout)

        self.frameChoose.destroy()
        frameSendMsg = Frame(self.root)
        frameSendMsg.grid(row = 0, column =0)
        textMsgStuff(frameSendMsg)
        
        cbValues = ('Alexandria','Sea','Flower', "Nature", "Egypt")      
        cb = ChecklistCombobox(frameSendMsg, values = cbValues, state='readonly', checkbutton_height=1, width=45, height=6)
        cb.pack()
        

        def sendMsg():
            recipients =[]
            chosen = cb.get()
            for choice in chosen:
                if choice == "Alexandria":
                    alexandria = ["alexandrinagram", "alessandria_egitto_", 'alexgram.eg', "alexandriatoday", "eskandrany18", "map_of_alexandria", "alexandriahabebti", "wualexandrian", "alexandriainmagazine"] #alexgram.eg, alexandrinagram
                    recipients.extend(alexandria)

                elif choice == "Sea":
                    sea = ['retro_codger']
                    recipients.extend(sea)

                elif choice == "Flower":
                    pass
                
                elif choice == "Nature":
                    nature = ["ourplanetdaily"]
                    recipients.extend(nature) # worldplaces, theglobewanderer, discoverearth, passionpassport, awesome_earthpix

                elif choice == "Egypt":
                    pass
                    egypt = ["mobile_photographers_egypt", "mobilephotographyeg", "egypt__pic", "thepicsecho", "unlimitedegypt", "egypt.discovery", "yalla.egypt", "yalla.egypt", "egypt.discovery"] #egypt.discovery, yalla.egypt
                    recipients.extend(egypt)

            insta = InstaDM(username='asser_seif_1999', password='3nd13$$10v3', headless=False)
            
            global textMsg    
            for recipient in recipients:
                insta.sendMessage(user=recipient, message=textMsg.get("1.0",'end-1c'))
        ttk.Button(frameSendMsg, text = 'Send', command = sendMsg).pack()
            
    def ifExit(self):
        def doSomethingOnExit():
            response = messagebox.askyesno("Exit program", "Are you sure you want to exit?")
            if response == 1:
                self.root.destroy()
            else:
                pass
        self.root.protocol('WM_DELETE_WINDOW',doSomethingOnExit)