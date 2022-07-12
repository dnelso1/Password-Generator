import random
import pyperclip
import tkinter as tk
import tkinter.ttk

def generatePwd():
    entry.delete(0, tk.END)

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specials = "!@#$%^&*()?"
    length = pwd_length.get()
    pwd = ""

    for _ in range(length):
        pwd = pwd + random.choice(lower)
    
    return pwd


def displayPwd():
    pwd = generatePwd()
    entry.insert(10, pwd)

def copyPwd():
    pwd = entry.get()
    pyperclip.copy(pwd)

def slide(var):
    slide_label = tk.Label(root, text=slider.get())
    slide_label.grid(column=1, row=20, sticky="W", ipadx=52)

def spinbox(var):
    # spin box for minimum numbers
    nums_spinbox = tk.Spinbox(root, from_=2, to=slider.get(), width=2)
    nums_spinbox.grid(column=1, row=50, sticky="E")

    # spin box for minimum special characters
    symbols_spinbox = tk.Spinbox(root, from_=2, to=slider.get(), width=2)
    symbols_spinbox.grid(column=1, row=55, sticky="E")

def includeLows():
    pass

def includeCaps():
    pass

def includeNums():
    pass

def includeSymbols():
    pass

# create GUI
root = tk.Tk()
root.geometry("428x500")
pwd_length = tk.IntVar()
low_letters = tk.IntVar()
cap_letters = tk.IntVar()
nums = tk.IntVar()
symbols = tk.IntVar()
spinbox_max = tk.StringVar()

# GUI title
root.title("Password Generator")

# label for password
#pwd_label = tk.Label(root, text="Password")
#pwd_label.grid(column=0, row=5)
entry = tk.Entry(root, width=25)
entry.grid(column=1, row=5, sticky="W")

# generate button
gen_button = tk.Button(root, text="Generate", command=displayPwd)
gen_button.grid(column=2, row=5)

# label for pwd length
length_label = tk.Label(root, text="Length")
length_label.grid(column=0, row=20, sticky="SW")

# label for lowercase letters
lows_label = tk.Label(root, text="Lowercase")
lows_label.grid(column=0, row=25, sticky="W")
lows_hover = tk.Label(root, text="ex: password", font=('*Font', '8'), fg="gray")
lows_hover.grid(column=1, row=25, sticky="W")

# label for capital letters
caps_label = tk.Label(root, text="Capitals")
caps_label.grid(column=0, row=30, sticky="W")
caps_hover = tk.Label(root, text="ex: pAsswOrD", font=('*Font', '8'), fg="gray")
caps_hover.grid(column=1, row=30, sticky="W")
#caps_hover = tk.Label(root, text="", width=40)
#caps_enter = caps_hover.configure(text="Include capital letters in your password.")
#caps_leave = caps_hover.configure(text="")
#caps_label.bind("<Enter>", caps_enter)
#caps_label.bind("<Leave>", caps_leave)

# label for numbers
nums_label = tk.Label(root, text="Numbers")
nums_label.grid(column=0, row=35, sticky="W")
nums_hover = tk.Label(root, text="ex: p4ssw9r2", font=('*Font', '8'), fg="gray")
nums_hover.grid(column=1, row=35, sticky="W")

# label for special characters (symbols)
symbols_label = tk.Label(root, text="Symbols")
symbols_label.grid(column=0, row=40, sticky="W")
symbols_hover = tk.Label(root, text="ex: p&ssw!r#", font=('*Font', '8'), fg="gray")
symbols_hover.grid(column=1, row=40, sticky="W")

# label for L33T replacement

# label for requirements
reqs_label = tk.Label(root, text="Requirements:")
reqs_label.grid(column=0, row=45, sticky="W")

# label for minimum numbers
min_nums_label = tk.Label(root, text="Min Numbers")
min_nums_label.grid(column=0, row=50, sticky="W")

# label for minimum special characters (symbols)
min_symbols_label = tk.Label(root, text="Min Special")
min_symbols_label.grid(column=0, row=55, sticky="W")

# combo box for length values
"""combo = tk.ttk.Combobox(root, textvariable=pwd_length)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(8)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)"""

# slider for length values
slider = tk.Scale(root, variable=pwd_length, from_=8, to=32, orient="horizontal", showvalue=0, command=slide)
slider.set(16)
slider.grid(column=1, row=20, sticky="E")

# label for slider
#slide_label = tk.Label(root, text=slider.get())
#slide_label.grid(column=1, row=1, sticky=tk.W)

# check box for lowercase letters
low_box = tk.Checkbutton(root, variable=low_letters, onvalue=1, offvalue=0, command=includeLows)
low_box.grid(column=1, row=25, sticky="E")
low_box.select()

# check box for capital letters
caps_box = tk.Checkbutton(root, variable=cap_letters, onvalue=1, offvalue=0, command=includeCaps)
caps_box.grid(column=1, row=30, sticky="E")

# check box for numbers
nums_box = tk.Checkbutton(root, variable=nums, onvalue=1, offvalue=0, command=includeNums)
nums_box.grid(column=1, row=35, sticky="E")

# check box for special characters (symbols)
symbols_box = tk.Checkbutton(root, variable=symbols, onvalue=1, offvalue=0, command=includeSymbols)
symbols_box.grid(column=1, row=40, sticky="E")

# spin box for minimum numbers
nums_spinbox = tk.Spinbox(root, from_=2, to=pwd_length.get(), command=spinbox, width=2)
nums_spinbox.grid(column=1, row=50, sticky="E")

# spin box for minimum special characters
symbols_spinbox = tk.Spinbox(root, from_=2, to=pwd_length.get(), command=spinbox, width=2)
symbols_spinbox.grid(column=1, row=55, sticky="E")

root.mainloop()