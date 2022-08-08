import random, pyperclip, pika
import tkinter as tk
import tkinter.ttk
from PIL import Image, ImageTk

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIALS = "!@#$%^&*()}{?"

# create GUI and variables
root = tk.Tk()
root.geometry("428x500")
root.title("Password Generator")
pwd_length = tk.IntVar()
low_letters = tk.IntVar()
cap_letters = tk.IntVar()
nums = tk.IntVar()
symbols = tk.IntVar()
nums_min = tk.IntVar()
symbols_min = tk.IntVar()
spinbox_max = tk.StringVar()



# * * * * * * * * * * * * * * * *
#  Functions
# * * * * * * * * * * * * * * * *

def generatePwd():
    pwd_entry.delete(0, tk.END)

    length = pwd_length.get()
    chars = ""
    pwd = ""

    if low_letters.get():
        chars += LOWER
    if cap_letters.get():
        chars += UPPER
    if nums.get():
        chars += NUMBERS
    if symbols.get():
        chars += SPECIALS

    for _ in range(length):
        pwd += random.choice(chars)
    
    displayPwd(pwd, '')

def displayPwd(pwd, src):
    if src == "convert":
        l33t_entry.delete(0, tk.END)
        l33t_entry.insert(10, pwd)
    else:
        pwd_entry.insert(10, pwd)

def copyPwd(src):
    if src == "convert":
        pwd = l33t_entry.get()
        pyperclip.copy(pwd)
    else:
        pwd = pwd_entry.get()
        pyperclip.copy(pwd)

def lenSlide(var):
    slide_label = tk.Label(root, text=len_slider.get())
    slide_label.grid(column=1, row=20, sticky="W", ipadx=52)

def convertToL33t():
    # create the RabbitMQ connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # declare the queue for receiving the converted password
    channel.queue_declare(queue='converted')

    # send/publish the current password to the receiver. routing key = receiver's consumer queue. reply_to = sender's consumer queue
    channel.basic_publish(exchange='', routing_key='password', properties=pika.BasicProperties(reply_to='converted'), body=l33t_entry.get())
    print(" [x] Sending password...")
    print(" [x] Waiting for the converted password...")

    # function that runs when a graph is received/consumed
    converted_pwd = ''
    def on_response(ch, method, properties, body):
        print(" [x] Received converted password")
        converted_pwd = body.decode()
        displayPwd(converted_pwd, "convert")
        channel.stop_consuming()

    # start consuming messages
    channel.basic_consume(queue='converted', on_message_callback=on_response, auto_ack=True)
    channel.start_consuming()

"""def displayConvertedPwd(pwd):
    l33t_entry.delete(0, tk.END)
    l33t_entry.insert(10, pwd)"""

"""def numSlide(var):
    slide_label = tk.Label(root, text=nums_slider.get())
    slide_label.grid(column=1, row=50, sticky="W", ipadx=52)
    slider = tk.Scale(root, variable=nums_min, from_=2, to=pwd_length.get(), orient="horizontal", showvalue=0, command=numSlide)
    slider.grid(column=1, row=50, sticky="E")

def symbolSlide(var):
    slide_label = tk.Label(root, text=symbols_slider.get())
    slide_label.grid(column=1, row=55, sticky="W", ipadx=52)"""

"""def spinbox(var):
    # spin box for minimum numbers
    nums_spinbox = tk.Spinbox(root, from_=2, to=len_slider.get(), width=2)
    nums_spinbox.grid(column=1, row=50, sticky="E")

    # spin box for minimum special characters
    symbols_spinbox = tk.Spinbox(root, from_=2, to=len_slider.get(), width=2)
    symbols_spinbox.grid(column=1, row=55, sticky="E")"""



# * * * * * * * * * * * * * * * *
#  Labels
# * * * * * * * * * * * * * * * *

# label for password
pwd_entry = tk.Entry(root, width=26)
pwd_entry.grid(column=1, row=5, sticky="W")

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

# label for L33T conversion
l33t_label = tk.Label(root, text="L33T Converter:")
l33t_label.grid(column=0, row=45, columnspan=2, sticky="W")
l33t_entry = tk.Entry(root, width=26)
l33t_entry.grid(column=1, row=50, sticky="W")



# * * * * * * * * * * * * * * * *
#  Interactive Elements
# * * * * * * * * * * * * * * * *

# combo box for length values
"""combo = tk.ttk.Combobox(root, textvariable=pwd_length)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(8)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)"""

# regenerate button
original_regen_img = Image.open("Images/regenerate.jpeg")
resized_regen_img = original_regen_img.resize((20, 20), Image.Resampling.LANCZOS)
regen_img = ImageTk.PhotoImage(resized_regen_img)
gen_button = tk.Button(root, image=regen_img, command=generatePwd)
gen_button.grid(column=2, row=5)

# password copy button
original_copy_img = Image.open("Images/copy.jpeg")
resized_copy_img = original_copy_img.resize((20, 20), Image.Resampling.LANCZOS)
copy_img = ImageTk.PhotoImage(resized_copy_img)
copy_button = tk.Button(root, image=copy_img, command=lambda: copyPwd(''))
copy_button.grid(column=3, row=5)

# slider for length values
len_slider = tk.Scale(root, variable=pwd_length, from_=8, to=32, orient="horizontal", showvalue=0, command=lenSlide)
len_slider.set(16)
len_slider.grid(column=1, row=20, sticky="E")

# check box for lowercase letters
low_box = tk.Checkbutton(root, variable=low_letters, onvalue=1, offvalue=0, command=generatePwd)
low_box.grid(column=1, row=25, sticky="E")
low_box.select()

generatePwd()

# check box for capital letters
caps_box = tk.Checkbutton(root, variable=cap_letters, onvalue=1, offvalue=0, command=generatePwd)
caps_box.grid(column=1, row=30, sticky="E")

# check box for numbers
nums_box = tk.Checkbutton(root, variable=nums, onvalue=1, offvalue=0, command=generatePwd)
nums_box.grid(column=1, row=35, sticky="E")

# check box for special characters (symbols)
symbols_box = tk.Checkbutton(root, variable=symbols, onvalue=1, offvalue=0, command=generatePwd)
symbols_box.grid(column=1, row=40, sticky="E")

# l33t conversion button
l33t_button = tk.Button(root, text="Convert", command=convertToL33t)
l33t_button.grid(column=2, row=50)

# l33t copy button
l33t_copy_button = tk.Button(root, image=copy_img, command=lambda: copyPwd('convert'))
l33t_copy_button.grid(column=3, row=50)

root.mainloop()