from tkinter import *
from math import sqrt as sqr


class Application(Frame):
    """
    An example of a calculator app developed using the 
    Tkinter GUI.
    """

    def __init__(self, master):
        """
        Initializes the frame.
        :param master: root.Tk()
        """
        Frame.__init__(self, master)
        self.entry = Entry(master, width=24, font=("Arial",25))
        self.entry.grid(row=0, column=0, columnspan=6, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()
        
    def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type) 
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
        """
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
        """
        Allows user to backspace their entry.
        :return: None
        """
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):
        """
        Allows user to clear the full entry.
        :return: None
        """
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        """
        Changes the operation symbols to their mathematical representation used in 
        the eval() method.
        :return: None
        """
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("√","sqr")
        e = e.replace("×", "*")
        e = e.replace("²", "**2")
        e = e.replace("^", "**")
        e = e.replace("÷", "/")

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20: # Alleviates problem of large numbers
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state="disabled")

    def flash(self,btn):
        """
        Flashes a corresponding button when key is pressed.
        :param btn: button
        :return: None
        """
        if btn != None:
            btn.config(bg="yellow")
            if btn == self.c_bttn:
                self.clear()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="lightgrey"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            else:
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
        else:
            pass

    def bind_buttons(self, master):
        """
        Binds keys to their appropriate input
        :param master: root.Tk()
        :return: None
        """
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("c", lambda event, btn=self.ac_bttn: self.flash(btn), self.clear_all)
    
    def create_widgets(self):
        """
        Creates the widgets to be used in the grid.
        :return: None
        """
        self.eq_bttn = Button(self, text="=", width=20, height=3, bg="lightgrey", command=lambda: self.calculate())
        self.eq_bttn.grid(row=4, column=4, columnspan=2)

        self.ac_bttn = Button(self, text='CE', width=9, height=3, command=lambda: self.clear_all())
        self.ac_bttn.grid(row=1, column=4)

        self.c_bttn = Button(self, text='←', width=9, height=3, command=lambda: self.clear())
        self.c_bttn.grid(row=1, column=5 )

        self.seven_bttn = Button(self, text="Hyper", width=9, height=3, command=lambda: self.add_chr(7))
        self.seven_bttn.grid(row=1, column=0)

        self.eight_bttn = Button(self, text="Confused", width=9, height=3, command=lambda: self.add_chr(8))
        self.eight_bttn.grid(row=1, column=1)

        self.nine_bttn = Button(self, text="Meh", width=9, height=3, command=lambda: self.add_chr(9))
        self.nine_bttn.grid(row=1, column=2)

        self.four_bttn = Button(self, text="Sad", width=9, height=3, command=lambda: self.add_chr(4))
        self.four_bttn.grid(row=2, column=0)

        self.five_bttn = Button(self, text="Moody", width=9, height=3, command=lambda: self.add_chr(5))
        self.five_bttn.grid(row=2, column=1)

        self.six_bttn = Button(self, text="Angry", width=9, height=3, command=lambda: self.add_chr(6))
        self.six_bttn.grid(row=2, column=2)

        self.one_bttn = Button(self, text="Good", width=9, height=3, command=lambda: self.add_chr(1))
        self.one_bttn.grid(row=3, column=0)

        self.two_bttn = Button(self, text="Bad", width=9, height=3, command=lambda: self.add_chr(2))
        self.two_bttn.grid(row=3, column=1)

        self.three_bttn = Button(self, text="Happy", width=9, height=3, command=lambda: self.add_chr(3))
        self.three_bttn.grid(row=3, column=2)

        self.zero_bttn = Button(self, text="Wanting", width=9, height=3, command=lambda: self.add_chr(0))
        self.zero_bttn.grid(row=4, column=0)

root = Tk()
root.geometry()
root.title("Type URL into browser and enjoy")
app = Application(root)
root.mainloop()