from tkinter import *
from advanced import *
from simple import *
import advanced as adv 
import simple as smp

def openmain():
    
    
    class MainMenu:
        def __init__(self, mastermain):
            self.mastermain = mastermain
            mastermain.title("Main Menu")
            self.label = Label(mastermain , text="Disclaimer: leave the web browser window on FULL SCREEN for this work!")
            self.label.pack(padx=10, pady=10)
            # Create and place widgets
            self.label = Label(mastermain, text="Choose a version of the automator to run:")
            self.label.pack(padx=10, pady=10)

            self.advanced_button = Button(mastermain, text="Advanced", command=self.run_advanced)
            self.advanced_button.pack(padx=10, pady=10)

            self.simple_button = Button(mastermain, text="Simple", command=self.run_simple)
            self.simple_button.pack(padx=10, pady=10)

            self.quit_button = Button(mastermain, text="Quit", command=mastermain.quit)
            self.quit_button.pack(padx=10, pady=10)

        def run_advanced(self):
            self.mastermain.destroy()
             # Close the main menu
            adv.run_advanced() # Run the advanced program
            
            
        def run_simple(self):
            self.mastermain.destroy() # Close the main menu
            smp.run_simple() # Run the simple program


       

    if __name__ == "__main__":
        root = Tk()
        main_menu = MainMenu(root)
        root.mainloop()
openmain()