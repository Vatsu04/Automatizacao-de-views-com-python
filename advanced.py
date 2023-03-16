from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pyautogui as auto
import pyperclip as pyper
import time
import webbrowser
import os
import simple as smp
def run_advanced():
    def confirmation():
        res = messagebox.askyesno(title="Confirmation", message="Are you sure you want to shut down your PC after the process?")
        if res:
            shutdown = True
        else:
            shutdown = False
            view_bot.shutdown_var.set(0)
        return shutdown

    class ViewBot:
        def __init__(self, masteradvanced):
            self.masteradvanced = masteradvanced
            masteradvanced.title("YouTube View Automator")
            #root.iconbitmap("favicon.ico")

            # Create and place widgets
            self.video_label = Label(masteradvanced, text="Video Link:")
            self.video_label.grid(row=0, column=0, padx=10, pady=10)

            self.video_entry = Entry(masteradvanced)
            self.video_entry.grid(row=0, column=1, padx=10, pady=10)


            self.horas_vagas_label = Label(masteradvanced, text="For how many minutes will you stay out of your PC?")
            self.horas_vagas_label.grid(row=1, column=0, padx=10, pady=10)

            self.horas_vagas_entry = Entry(masteradvanced)
            self.horas_vagas_entry.grid(row=1, column=1, padx=10, pady=10)

            self.duracao_label = Label(masteradvanced, text="Video length: \n (In seconds, if it's longer than 30 seconds, \n it doesn't have to be exact)")
            self.duracao_label.grid(row=2, column=0, padx=10, pady=10)

            self.duracao_entry = Entry(masteradvanced)
            self.duracao_entry.grid(row=2, column=1, padx=10, pady=10)

            self.calculate = Button(masteradvanced, text="Calculate Recommended Views", command=self.calculate_rec_views)
            self.calculate.grid(row=3, column=0, padx=10, pady=10)

            self.views_rec_label = Label(masteradvanced, text="")
            self.views_rec_label.grid(row=3, column=1, padx=10, pady=10)


            self.views_label = Label(masteradvanced, text="Number of Views:")
            self.views_label.grid(row=4, column=0, padx=10, pady=10)

            self.views_entry = Entry(masteradvanced)
            self.views_entry.grid(row=4, column=1, padx=10, pady=10)

            self.premium_label = Label(masteradvanced, text="Do you have YouTube Premium?")
            self.premium_label.grid(row=5, column=0, padx=10, pady=10)

            self.premium_var = IntVar()
            self.premium_yes = Radiobutton(masteradvanced, text="Yes", variable=self.premium_var, value=1)
            self.premium_yes.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            self.premium_no = Radiobutton(masteradvanced, text="No", variable=self.premium_var, value=0)
            self.premium_no.grid(row=5, column=1, padx=10, pady=10, sticky="e")
            
            self.shutdown_label = Label(masteradvanced, text="Do you wish to shut down your computer after the automation?")
            self.shutdown_label.grid(row=6, column=0, padx=10, pady=10  )
            
            self.shutdown_var = IntVar()
            self.shutdown_yes =Radiobutton(masteradvanced, text="Yes", variable=self.shutdown_var, value=1, command=confirmation)
            self.shutdown_yes.grid(row=6, column = 1, padx=10, pady=10, sticky="w")
            
            self.shutdown_no =Radiobutton(masteradvanced, text="No", variable=self.shutdown_var, value=0)
            self.shutdown_no.grid(row=6, column = 1, padx=10, pady=10, sticky="e")
            
            self.start_button = Button(masteradvanced, text="Start", command=self.start_bot)
            self.start_button.grid(row=7, column=0, padx=10, pady=10)

            self.quit_button = Button(masteradvanced, text="Quit", command=masteradvanced.quit)
            self.quit_button.grid(row=7, column=1, padx=10, pady=10)
            
            self.simple_run = Button(masteradvanced, text="Simple", command=self.run_simple)
            self.simple_run.grid(row=7, column=3, padx=10, pady=10  )
            
        #os.system('shutdown /p /f')
        
        def run_simple(self):
            
            smp.run_simple() # Run the simple program
            
        
        def calculate_rec_views(self):
            duracao = int(self.duracao_entry.get())
            if duracao > 30:
                duracao = 40
            horas_vagas = int(self.horas_vagas_entry.get())
            views_rec = int(horas_vagas*60 / duracao)
            self.views_rec_label.config(text=str(views_rec))

        
        def start_bot(self):
            video = self.video_entry.get()
            views = int(self.views_entry.get())
            premium = self.premium_var.get()
            duracao = int(self.duracao_entry.get())
            shutdown = self.shutdown_var.get()
        
        
            
                
            webbrowser.open("https://youtube.com")

            time.sleep(5)

            pyper.copy("{}".format(video))

            if premium:
                if shutdown: 
                    if duracao > 30:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(40)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                        os.system('shutdown /p /f')
                    else:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(duracao+2)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                        os.system('shutdown /p /f')
                else:
                    if duracao > 30:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(40)
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
                if shutdown: 
                    if duracao > 30:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(35)
                            auto.click(x=1599, y=740)
                            time.sleep(40)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                        os.system('shutdown /p /f')
                    else:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(duracao+2)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                        os.system('shutdown /p /f')
                else: 
                    if duracao > 30:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(35)
                            auto.click(x=1599, y=740)
                            time.sleep(40)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                    else:
                        for i in range(views):
                            auto.click(x=1296, y=55)
                            auto.hotkey("ctrl", "v")
                            auto.press("enter")
                            time.sleep(35)
                            auto.click(x=1599, y=740)
                            time.sleep(duracao+2)
                            auto.hotkey("ctrl", "w")
                            auto.hotkey("ctrl", "t")
                
                    


    root = Tk()
    view_bot = ViewBot(root)
    root.mainloop()


    #https://www.youtube.com/watch?v=w4cTYnOPdNk

    #skip ad: (x=1599, y=729)https://www.youtube.com/watch?v=w4cTYnOPdNk