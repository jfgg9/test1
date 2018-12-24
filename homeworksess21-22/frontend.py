from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window
        bgcolor = "#20207f"
        title = "Hangman Game"
        window.title("Hangman")
        window.geometry("1400x700")
        window.resizable(0, 0)
        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=1)
        self.image_frame = Frame(master=self.frame)
        self.canvas = []

        for i in range(5):
            self.canvas.append(Canvas(master=self.image_frame, width=250, height=500, bg="green", highlightthickness=0))
            self.canvas[i].grid(row=0, column=i)

        self.image_frame.grid(row=1, padx=20)
        self.label = Label(self.frame, text="", bg=bgcolor, fg="white")
        self.label.grid(row=5)
        self.label.config(font=("Courier", 44))
        self.label2 = Label(self.frame, text=title, bg=bgcolor, fg="White")
        self.label2.grid(row=0, columnspan=2)
        self.label2.config(font=("Courier", 20))
        self.bt1 = Button(self.frame, text="Hit me!")
        self.bt1.config(font=("Courier", 15))
        self.bt1.grid(row=1, column=1, columnspan=2)
        self.bt2 = Button(self.frame, text="Exit Game", bg="black", fg="yellow")
        self.bt2.grid(row=2, column=2)


window = Tk(screenName="Hangman Game")
hangman_game = GUI(window)
window.mainloop()
