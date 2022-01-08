from tkinter import *
from tkinter import ttk


def load_time(*arge):
    h1.set(0)
    m1.set(0)
    s1.set(0)
    h2.set(0)
    m2.set(0)
    s2.set(0)
    sd3.set(0)
    ss3.set(0)
    sm3.set(0)
    sh3.set(0)
    d1.set(0)
    d2.set(0)


def check_limit(h1, m1, s1):
    if h1 >= 24 or m1 >= 60 or s1 >= 60:
        return False
    else:
        return True


def add_time(*args):
    try:
        h1_val = int(h1.get())
        m1_val = int(m1.get())
        s1_val = int(s1.get())
        d1_val = int(d1.get())
        if not check_limit(h1_val, m1_val, s1_val):
            colon = ttk.Label(frame, width=14, text="Invalid Time 1")
            colon.grid(row=8, column=0, sticky=(W, E))
            root.mainloop()
        else:
            colon = ttk.Label(frame, width=0, text="")
            colon.grid(row=8, column=0, sticky=(W, E))
        h2_val = int(h2.get())
        m2_val = int(m2.get())
        s2_val = int(s2.get())
        d2_val = int(d2.get())
        if not check_limit(h2_val, m2_val, s2_val):
            colon = ttk.Label(frame, width=14, text="Invalid Time 2")
            colon.grid(row=8, column=0, sticky=(W, E))
            root.mainloop()
        else:
            colon = ttk.Label(frame, width=0, text="")
            colon.grid(row=8, column=0, sticky=(W, E))
    except ValueError as e:
        print("Error : ", e)
        colon = ttk.Label(frame, width=23, text="All Cell must be filled")
        colon.grid(row=8, column=0, sticky=(W, E))
        root.mainloop()
    except:
        colon = ttk.Label(frame, width=23, text="All Cell must be filled")
        colon.grid(row=8, column=0, sticky=(W, E))
        root.mainloop()
        print("Unknown Error occoured")
    colon = ttk.Label(frame, width=0, text="")
    colon.grid(row=8, column=0, sticky=(W, E))

    s3_val = s1_val + s2_val
    m3_val = m1_val + m2_val
    h3_val = h1_val + h2_val
    d3_val = d1_val + d2_val
    if s3_val >= 60:
        s3_val -= 60
        m3_val += 1
    if m3_val >= 60:
        m3_val -= 60
        h3_val += 1
    if h3_val >= 24:
        d3_val += 1
        h3_val -= 24
    with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
        my_file.write(str(h3_val)+":"+str(m3_val) +
                      ":"+str(s3_val)+":"+str(d3_val))
        my_file.close()
    ss3.set(s3_val)
    sm3.set(m3_val)
    sh3.set(h3_val)
    sd3.set(d3_val)

# Substraction


def sub_time(*args):
    try:
        h1_val = int(h1.get())
        m1_val = int(m1.get())
        s1_val = int(s1.get())
        d1_val = int(d1.get())
        if not check_limit(h1_val, m1_val, s1_val):
            colon = ttk.Label(frame, width=14, text="Invalid Time 1")
            colon.grid(row=8, column=0, sticky=(W, E))
            root.mainloop()
        else:
            colon = ttk.Label(frame, width=0, text="")
            colon.grid(row=8, column=0, sticky=(W, E))
        h2_val = int(h2.get())
        m2_val = int(m2.get())
        s2_val = int(s2.get())
        d2_val = int(d2.get())
        if not check_limit(h2_val, m2_val, s2_val):
            colon = ttk.Label(frame, width=14, text="Invalid Time 2")
            colon.grid(row=8, column=0, sticky=(W, E))
            root.mainloop()
        else:
            colon = ttk.Label(frame, width=0, text="")
            colon.grid(row=8, column=0, sticky=(W, E))
    except ValueError as e:
        colon = ttk.Label(frame, width=23, text="All Cell must be filled")
        colon.grid(row=8, column=0, sticky=(W, E))
        root.mainloop()
        print("Error : ", e)
    except:
        colon = ttk.Label(frame, width=23, text="All Cell must be filled")
        colon.grid(row=8, column=0, sticky=(W, E))
        root.mainloop()
        print("Unknown Error occoured")
    colon = ttk.Label(frame, width=0, text="")
    colon.grid(row=8, column=0, sticky=(W, E))

    s3_val = s1_val - s2_val
    m3_val = m1_val - m2_val
    h3_val = h1_val - h2_val
    d3_val = d1_val - d2_val
    if s3_val < 0:
        s3_val += 60
        m3_val -= 1
    if m3_val < 0:
        m3_val += 60
        h3_val -= 1
    if h3_val < 0:
        h3_val += 24
        d3_val -= 1
    with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
        my_file.write(str(h3_val)+":"+str(m3_val) +
                      ":"+str(s3_val)+":"+str(d3_val))
        my_file.close()
    ss3.set(s3_val)
    sm3.set(m3_val)
    sh3.set(h3_val)
    sd3.set(d3_val)


def save_result(*args):
    data = ""
    with open("mydata.txt", mode="r", encoding="utf-8") as my_file:
        data = my_file.read()
        my_file.close()
    h_2, m_2, s_2, d_2 = data.split(":")
    h_2 = int(h_2)
    m_2 = int(m_2)
    s_2 = int(s_2)
    d_2 = int(d_2)
    h1.set(h_2)
    m1.set(m_2)
    s1.set(s_2)
    d1.set(d_2)


root = Tk()
root.title("Time Calc")
root.geometry("550x300")
root.resizable(width=False, height=False)
style = ttk.Style()
style.configure("TButton", font="Serif 15")
style.configure("TEntry", font="Serif 18", padding=10)

frame = ttk.Frame(root, padding="20 20 20 20")

frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

h1 = StringVar()
m1 = StringVar()
s1 = StringVar()
h2 = StringVar()
m2 = StringVar()
s2 = StringVar()
sh3 = StringVar()
sm3 = StringVar()
ss3 = StringVar()
sd3 = StringVar()
d2 = StringVar()
d1 = StringVar()

Label_1 = ttk.Label(frame, width=10, text="HH (0-23)")
Label_1.grid(row=0, column=1, sticky=(W, E), padx=5, pady=5)
Label_1 = ttk.Label(frame, width=10, text=" MM (0-59)")
Label_1.grid(row=0, column=3, sticky=(W, E), padx=5, pady=5)
Label_1 = ttk.Label(frame, width=10, text=" SS (0-59)")
Label_1.grid(row=0, column=5, sticky=(W, E), padx=5, pady=5)
Label_1 = ttk.Label(frame, width=10, text=" Day ")
Label_1.grid(row=0, column=7, sticky=(W, E), padx=5, pady=5)


# time 1
Label_1 = ttk.Label(frame, width=28, text="Time 1 : ")
Label_1.grid(row=1, column=0, sticky=(W, E))
h1_entry = ttk.Entry(frame, width=2, textvariable=h1)
h1_entry.grid(row=1, column=1, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=1, column=2, sticky=(W, E))
m1_entry = ttk.Entry(frame, width=2, textvariable=m1)
m1_entry.grid(row=1, column=3, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=1, column=4, sticky=(W, E))
s1_entry = ttk.Entry(frame, width=2, textvariable=s1)
s1_entry.grid(row=1, column=5, sticky=(W, E))
colon = ttk.Label(frame, width=1, text="-")
colon.grid(row=1, column=6, sticky=(W, E))
d1_entry = ttk.Entry(frame, width=2, textvariable=d1)
d1_entry.grid(row=1, column=7, sticky=(W, E))

# Space
add_symbol = ttk.Label(frame,  text="")
add_symbol.grid(column=2, row=2, sticky=(W, E))

# time2
Label_1 = ttk.Label(frame, width=10, text="Time 2 : ")
Label_1.grid(row=3, column=0, sticky=(W, E))
h2_entry = ttk.Entry(frame, width=2, textvariable=h2)
h2_entry.grid(row=3, column=1, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=3, column=2, sticky=(W, E))
m2_entry = ttk.Entry(frame, width=2, textvariable=m2)
m2_entry.grid(row=3, column=3, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=3, column=4, sticky=(W, E))
s2_entry = ttk.Entry(frame, width=2, textvariable=s2)
s2_entry.grid(row=3, column=5, sticky=(W, E))
colon = ttk.Label(frame, width=1, text="-")
colon.grid(row=3, column=6, sticky=(W, E))
d1_entry = ttk.Entry(frame, width=2, textvariable=d2)
d1_entry.grid(row=3, column=7, sticky=(W, E))

# Space
add_symbol = ttk.Label(frame,  text="")
add_symbol.grid(column=2, row=4, sticky=(W, E))
# Button
add_button = ttk.Button(frame, text="+", width=2, command=add_time)
add_button.grid(column=5, row=5, sticky=(W, E), columnspan=3)
add_button.columnconfigure

sub_button = ttk.Button(frame, text="-", width=2, command=sub_time)
sub_button.grid(column=1, row=5, sticky=(W, E), columnspan=3)
sub_button.columnconfigure


sub_button = ttk.Button(frame, text="Load Result", width=5, command=save_result)
sub_button.grid(column=0, row=5, sticky=(W, E))
sub_button.columnconfigure

# Space
add_symbol = ttk.Label(frame,  text="")
add_symbol.grid(column=2, row=6, sticky=(W, E))
load_time()

# solution
Label_1 = ttk.Label(frame, width=10, text="Result : ")
Label_1.grid(row=7, column=0, sticky=(W, E))
h3_entry = ttk.Entry(frame, width=2, textvariable=sh3)
h3_entry.grid(row=7, column=1, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=7, column=2, sticky=(W, E))
m3_entry = ttk.Entry(frame, width=2, textvariable=sm3)
m3_entry.grid(row=7, column=3, sticky=(W, E))
colon = ttk.Label(frame, width=1, text=":")
colon.grid(row=7, column=4, sticky=(W, E))
s3_entry = ttk.Entry(frame, width=2, textvariable=ss3)
s3_entry.grid(row=7, column=5, sticky=(W, E))
colon = ttk.Label(frame, width=1, text="-")
colon.grid(row=7, column=6, sticky=(W, E))
d_entry = ttk.Entry(frame, width=5, textvariable=sd3)
d_entry.grid(row=7, column=7, sticky=(W, E))
root.bind("<Return>", add_time)


root.mainloop()
