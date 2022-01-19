from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        if value == "AC":
            self.calc_value = 0.0
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.number_entry.delete(0, "end")
            entry_val = 0
            # self.number_entry.insert(0, entry_val)
        else:
            entry_val = self.number_entry.get()
            entry_val += value
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, entry_val)

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == '/':
                self.div_trigger = True
                print("/ Pressed")
            elif value == '*':
                self.mult_trigger = True
                print("* Pressed")
            elif value == '+':
                self.add_trigger = True
                print("+ Pressed")
            elif value == '-':
                self.sub_trigger = True
                print("- Pressed")
            self.number_entry.delete(0, "end")

    def equal_button_pressed(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.div_trigger:
                solution = self.calc_value / float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        # root.geometry("523x220")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", paddind=10)
        style.configure("TEntry", font="Serif 18", padding=10)
        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=80)
        self.number_entry.grid(row=0, columnspan=4, sticky=(W, E))

        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7'))
        self.button7.grid(row=1, column=0,
                          sticky=(W, E))
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8'))
        self.button8.grid(row=1, column=1, sticky=(W, E))
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9'))
        self.button9.grid(row=1, column=2, sticky=(W, E))
        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/'))
        self.button_div.grid(row=1, column=3, sticky=(W, E))
        # Row2
        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4'))
        self.button4.grid(row=2, column=0, sticky=(W, E))
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5'))
        self.button5.grid(row=2, column=1, sticky=(W, E))
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6'))
        self.button6.grid(row=2, column=2, sticky=(W, E))
        self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*'))
        self.button_mult.grid(row=2, column=3, sticky=(W, E))
        # Row3
        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1'))
        self.button1.grid(row=3, column=0, sticky=(W, E))
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2'))
        self.button2.grid(row=3, column=1, sticky=(W, E))
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3'))
        self.button3.grid(row=3, column=2, sticky=(W, E))
        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+'))
        self.button_add.grid(row=3, column=3, sticky=(W, E))
        # Row4
        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press('AC'))
        self.button_clear.grid(row=4, column=0, sticky=(W, E))
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0'))
        self.button0.grid(row=4, column=1, sticky=(W, E))
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_pressed())
        self.button_equal.grid(row=4, column=2, sticky=(W, E))
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-'))
        self.button_sub.grid(row=4, column=3, sticky=(W, E))


root = Tk()
calc = Calculator(root)
root.mainloop()
