import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        master = self.master

        self.calculated = False# Init calculated state

        # Configure frame
        master.geometry("300x400")
        master.title("Calculator")
        master.configure(bg="darkgray")
        master.resizable(False, False)

        # Add equation entry
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        self.entEq = tk.Entry(master, font=("Calibri 12"))
        self.entEq.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Add the clear button
        master.rowconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        tk.Button(master, text="Clear", bg="darkgray", command=self.clear).grid(row=1, column=1, sticky="nsew")

        # Add the delete button
        master.rowconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        tk.Button(master, text="Del", bg="darkgray", command=self.delete).grid(row=1, column=2, sticky="nsew")

        # Add number buttons
        for i in range(3):
            for j in range(3):
                master.columnconfigure(j, weight=1)
                master.rowconfigure(i + 2, weight=1)
                tk.Button(master, text=str(j + i * 3 + 1), bg="darkgray", command=lambda val=j + i * 3 + 1: self.onBtn(btnText=val)).grid(row=i + 2, column=j, sticky="nsew")
        master.rowconfigure(5, weight=1)
        master.columnconfigure(0, weight=1)
        tk.Button(master, text=0, bg="darkgray", command=lambda val=0: self.onBtn(btnText=val)).grid(row=5, column=0, columnspan=3, sticky="nsew")

        # Add operation buttons
        master.rowconfigure(1, weight=1)
        master.columnconfigure(3, weight=1)
        tk.Button(master, text='+', bg="darkgray", command=lambda val='+': self.onBtn(btnText=val)).grid(row=1, column=3, sticky="nsew")
        master.rowconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)
        tk.Button(master, text='-', bg="darkgray", command=lambda val='-': self.onBtn(btnText=val)).grid(row=2, column=3, sticky="nsew")
        master.rowconfigure(3, weight=1)
        master.columnconfigure(3, weight=1)
        tk.Button(master, text='*', bg="darkgray", command=lambda val='*': self.onBtn(btnText=val)).grid(row=3, column=3, sticky="nsew")
        master.rowconfigure(4, weight=1)
        master.columnconfigure(3, weight=1)
        tk.Button(master, text='/', bg="darkgray", command=lambda val='/': self.onBtn(btnText=val)).grid(row=4, column=3, sticky="nsew")

        # Add the equal button
        master.rowconfigure(5, weight=1)
        master.columnconfigure(3, weight=1)
        tk.Button(master, text='=', bg="darkgray", command=self.calculate).grid(row=5, column=3, sticky="nsew")

        master.mainloop()

    def onBtn(self, btnText):
        if self.calculated:
            self.clear()
        self.entEq.insert(tk.END, btnText)

    def clear(self):
        self.entEq.delete(0, tk.END)
        self.calculated = False

    def delete(self):
        self.entEq.delete(len(self.entEq.get()) - 1, tk.END)

    def calculate(self):
        try:
            result = eval(self.entEq.get())
        except:
            result = "error"
        self.entEq.insert(tk.END, '=')
        self.entEq.insert(tk.END, result)
        self.calculated = True
