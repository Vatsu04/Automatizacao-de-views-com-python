from tkinter import *
import pyautogui as auto
import pyperclip as pyper
import time
import webbrowser
import main 
import advanced as adv


def run_simple():

    class ViewBot:
        
        def __init__(self, mastersimple):
            self.mastersimple = mastersimple
                
            mastersimple.title("YouTube View Automator")
            root.iconbitmap("favicon.ico")
                
            # Create and place widgets
            self.video_label = Label(mastersimple, text="Video Link:")
            self.video_label.grid(row=0, column=0, padx=10, pady=10)

            self.video_entry = Entry(mastersimple)
            self.video_entry.grid(row=0, column=1, padx=10, pady=10)

            self.views_label = Label(mastersimple, text="Number of Views:")
            self.views_label.grid(row=1, column=0, padx=10, pady=10)

            self.views_entry = Entry(mastersimple)
            self.views_entry.grid(row=1, column=1, padx=10, pady=10)
                
            self.duracao_label = Label(mastersimple, text="Video length: \n (In seconds, if its longer than 30 seconds, \n it doesn't have to be exact)")
            self.duracao_label.grid(row=2, column=0, padx=10, pady=10)
                
            self.duracao_entry = Entry(mastersimple)
            self.duracao_entry.grid(row=2, column=1, padx=10, pady=10)
            
            
                
            self.premium_label = Label(mastersimple, text="Do you have YouTube Premium?")
            self.premium_label.grid(row=4, column=0, padx=10, pady=10)
                
            self.premium_var = IntVar()
            self.premium_yes = Radiobutton(mastersimple, text="Yes", variable=self.premium_var, value=1)
            self.premium_yes.grid(row=4, column=1, padx=10, pady=10, sticky="w")

            self.premium_no = Radiobutton(mastersimple, text="No", variable=self.premium_var, value=0)
            self.premium_no.grid(row=4, column=1, padx=10, pady=10, sticky="e")
                
            self.start_button = Button(mastersimple, text="Start", command=self.start_bot)
            self.start_button.grid(row=6, column=0, padx=10, pady=10)

            self.clear_button = Button(mastersimple, text="Clear Form", command=self.clear_form)
            self.clear_button.grid(row=6, column=1, padx=10, pady=10)

            self.advanced_run = Button(mastersimple , text="Advanced", command=self.run_advanced)
            self.advanced_run.grid(row=6, column=2, padx=10, pady=10  )
                
        def clear_form(self):
            self.video_entry.delete(0, END)
            self.views_entry.delete(0, END)
            self.duracao_entry.delete(0, END)
            self.premium_var.set(0)
            
        def run_advanced(self):
            adv.run_advanced() # Run the simple program
            self.mastersimple.destroy()
            # Show the main menu win

        def start_bot(self):
            video = self.video_entry.get()
            views = int(self.views_entry.get())
            premium = self.premium_var.get()
            duracao = int(self.duracao_entry.get())
            horas_vagas = int(self.duracao_entry.get())
            views_rec = horas_vagas % duracao
                
            webbrowser.open("https://youtube.com")

            time.sleep(5)

            pyper.copy("{}".format(video))

            if premium:
                if duracao>30:
                    for i in range(views):
                        auto.click(x=1296, y=55)
                        auto.hotkey("ctrl", "v")
                        auto.press("enter")
                        time.sleep(47)
                        auto.hotkey("ctrl", "w")
                        auto.hotkey("ctrl", "t")
                        
                else:
                    for i in range(views):
                        auto.click(x=1296, y=55)
                        auto.hotkey("ctrl", "v")
                        auto.press("enter")
                        time.sleep(duracao+2)
                        auto.hotkey("ctrl", "w")
                        auto.hotkey("ctrl", "t")
                        
            else:
                if duracao>30:
                    for i in range(views):
                        auto.click(x=1296, y=55)
                        auto.hotkey("ctrl", "v")
                        auto.press("enter")
                        time.sleep(35)
                        auto.click(x=1599, y=740)
                        time.sleep(47)
                        auto.hotkey("ctrl", "w")
                        auto.hotkey("ctrl", "t")
                        
                else:
                    for i in range(views):
                        auto.click(x=1296, y=55)
                        auto.hotkey("ctrl", "v")
                        auto.press("enter")
                        time.sleep(35)
                        auto.click(x=1599, y=740)
                        time.sleep(47)
                        auto.hotkey("ctrl", "w")
                        auto.hotkey("ctrl", "t")
                        


    root = Tk()
    view_bot = ViewBot(root)
    root.mainloop()


    #https://www.youtube.com/watch?v=w4cTYnOPdNk

    #skip ad: (x=1599, y=729)https://www.youtube.com/watch?v=w4cTYnOPdNk
           