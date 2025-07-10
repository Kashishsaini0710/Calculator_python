from tkinter import Tk, Entry, Button, StringVar, Label

class Calculator:
    def __init__(self, master):
        master.title("Advanced Calculator")
        master.geometry('357x480+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        self.history = StringVar()

        # Display field
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # History label
        Label(master, textvariable=self.history, bg='black', fg='white', anchor='w', font=('Arial', 14)).place(x=0, y=45)

        # Buttons layout
        Button(width=11, height=4, text='(', bg='white', relief='flat', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', bg='white', relief='flat', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', bg='white', relief='flat', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='/', bg='white', relief='flat', command=lambda: self.show('/')).place(x=270, y=50)

        Button(width=11, height=4, text='1', bg='white', relief='flat', command=lambda: self.show('1')).place(x=0, y=125)
        Button(width=11, height=4, text='2', bg='white', relief='flat', command=lambda: self.show('2')).place(x=90, y=125)
        Button(width=11, height=4, text='3', bg='white', relief='flat', command=lambda: self.show('3')).place(x=180, y=125)
        Button(width=11, height=4, text='*', bg='white', relief='flat', command=lambda: self.show('*')).place(x=270, y=125)

        Button(width=11, height=4, text='4', bg='white', relief='flat', command=lambda: self.show('4')).place(x=0, y=200)
        Button(width=11, height=4, text='5', bg='white', relief='flat', command=lambda: self.show('5')).place(x=90, y=200)
        Button(width=11, height=4, text='6', bg='white', relief='flat', command=lambda: self.show('6')).place(x=180, y=200)
        Button(width=11, height=4, text='-', bg='white', relief='flat', command=lambda: self.show('-')).place(x=270, y=200)

        Button(width=11, height=4, text='7', bg='white', relief='flat', command=lambda: self.show('7')).place(x=0, y=275)
        Button(width=11, height=4, text='8', bg='white', relief='flat', command=lambda: self.show('8')).place(x=90, y=275)
        Button(width=11, height=4, text='9', bg='white', relief='flat', command=lambda: self.show('9')).place(x=180, y=275)
        Button(width=11, height=4, text='+', bg='white', relief='flat', command=lambda: self.show('+')).place(x=270, y=275)

        Button(width=11, height=4, text='C', bg='white', relief='flat', command=self.clear).place(x=0, y=350)
        Button(width=11, height=4, text='0', bg='white', relief='flat', command=lambda: self.show('0')).place(x=90, y=350)
        Button(width=11, height=4, text='.', bg='white', relief='flat', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='=', bg='white', relief='flat', command=self.solve).place(x=270, y=350)

        # Enable keyboard input
        master.bind('<Key>', self.key_input)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')
        self.history.set('')

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.history.set(f"{self.entry_value} = {result}")
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def key_input(self, event):
        char = event.char
        if char in '0123456789+-*/().%':
            self.show(char)
        elif event.keysym == 'Return':
            self.solve()
        elif event.keysym == 'BackSpace':
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)

# Run the app
root = Tk()
calculator = Calculator(root)
root.mainloop()
