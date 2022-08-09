import random, pyperclip, pika
import tkinter as tk
from PIL import Image, ImageTk

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "01234567890123456789"
SPECIALS = "!@#$%^&*()}{?!@#$%^&*()}{?"

# create GUI
root = tk.Tk()
root.geometry("427x500")
root.title("Password Generator")


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
    # displays the length slider value as it changes
    slide_label = tk.Label(pwd_frame, text=len_slider.get())
    slide_label.grid(column=1, row=2, sticky="W", ipadx=52)

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


# * * * * * * * * * * * * * * * *
#  Password Frame Labels
# * * * * * * * * * * * * * * * *

pwd_frame = tk.Frame(root)
pwd_frame.grid(column=0, row=0)

# label for pwd length
length_label = tk.Label(pwd_frame, text="Length")
length_label.grid(column=0, row=2, sticky="SW")

# label for options
options_label = tk.Label(pwd_frame, text="Choose options for a secure password:")
options_label.grid(column=0, row=1, columnspan=2, pady=10, sticky="SW")

# label for lowercase letters
lows_label = tk.Label(pwd_frame, text="Lowercase")
lows_label.grid(column=0, row=3, sticky="W")
lows_hover = tk.Label(pwd_frame, text="ex: password", font=('*Font', '8'), fg="gray")
lows_hover.grid(column=1, row=3, sticky="W")

# label for capital letters
caps_label = tk.Label(pwd_frame, text="Capitals")
caps_label.grid(column=0, row=4, sticky="W")
caps_hover = tk.Label(pwd_frame, text="ex: pAsswOrD", font=('*Font', '8'), fg="gray")
caps_hover.grid(column=1, row=4, sticky="W")

# label for numbers
nums_label = tk.Label(pwd_frame, text="Numbers")
nums_label.grid(column=0, row=5, sticky="W")
nums_hover = tk.Label(pwd_frame, text="ex: p4ssw9r2", font=('*Font', '8'), fg="gray")
nums_hover.grid(column=1, row=5, sticky="W")

# label for special characters (symbols)
symbols_label = tk.Label(pwd_frame, text="Symbols")
symbols_label.grid(column=0, row=6, sticky="W")
symbols_hover = tk.Label(pwd_frame, text="ex: p&ssw!r#", font=('*Font', '8'), fg="gray")
symbols_hover.grid(column=1, row=6, sticky="W")


# * * * * * * * * * * * * * * * * * * *
#  Password Frame Interactive Elements
# * * * * * * * * * * * * * * * * * * *

# entry box for password
pwd_entry = tk.Entry(pwd_frame, width=32)
pwd_entry.grid(column=1, row=0, sticky="W")

# password regenerate and copy buttons
original_regen_img = Image.open("Images/regenerate.jpeg")
resized_regen_img = original_regen_img.resize((20, 20), Image.Resampling.LANCZOS)
regen_img = ImageTk.PhotoImage(resized_regen_img)
regen_button = tk.Button(pwd_frame, image=regen_img, command=generatePwd)
regen_button.grid(column=2, row=0)

original_copy_img = Image.open("Images/copy.jpeg")
resized_copy_img = original_copy_img.resize((20, 20), Image.Resampling.LANCZOS)
copy_img = ImageTk.PhotoImage(resized_copy_img)
copy_button = tk.Button(pwd_frame, image=copy_img, command=lambda: copyPwd(''))
copy_button.grid(column=3, row=0)

# slider for length values
pwd_length = tk.IntVar()
len_slider = tk.Scale(pwd_frame, variable=pwd_length, from_=8, to=32, orient="horizontal", showvalue=0, command=lenSlide)
len_slider.set(16)
len_slider.grid(column=1, row=2, sticky="E")

# checkboxes for lowercase/uppercase letters, numbers, and special characters
low_letters = tk.IntVar()
low_box = tk.Checkbutton(pwd_frame, variable=low_letters, onvalue=1, offvalue=0, command=generatePwd)
low_box.grid(column=1, row=3, sticky="E")
low_box.select()

cap_letters = tk.IntVar()
caps_box = tk.Checkbutton(pwd_frame, variable=cap_letters, onvalue=1, offvalue=0, command=generatePwd)
caps_box.grid(column=1, row=4, sticky="E")
caps_box.select()

nums = tk.IntVar()
nums_box = tk.Checkbutton(pwd_frame, variable=nums, onvalue=1, offvalue=0, command=generatePwd)
nums_box.grid(column=1, row=5, sticky="E")
nums_box.select()

symbols = tk.IntVar()
symbols_box = tk.Checkbutton(pwd_frame, variable=symbols, onvalue=1, offvalue=0, command=generatePwd)
symbols_box.grid(column=1, row=6, sticky="E")


# * * * * * * * * * * * * * * * *
#  L33t Frame Labels
# * * * * * * * * * * * * * * * *

l33t_frame = tk.Frame(root)
l33t_frame.grid(column=0, row=2, pady=50)

# labels for l33T conversion
l33t_label = tk.Label(l33t_frame, text="L33t Converter:")
l33t_label.grid(column=0, row=0, columnspan=2, sticky="W")
l33t_description = tk.Label(l33t_frame, text="Convert your weak passwords to strong ones", font=('*Font', '8', "italic"), fg="gray")
l33t_description.grid(column=0, row=3, columnspan=2, sticky="W")


# * * * * * * * * * * * * * * * * *
#  L33t Frame Interactive Elements
# * * * * * * * * * * * * * * * * *

# entry box for l33t conversion
l33t_entry = tk.Entry(l33t_frame, width=26)
l33t_entry.grid(column=1, row=1, sticky="W")

# l33t conversion and copy buttons
original_convert_img = Image.open("Images/convert.jpeg")
resized_convert_img = original_convert_img.resize((20, 20), Image.Resampling.LANCZOS)
convert_img = ImageTk.PhotoImage(resized_convert_img)
l33t_button = tk.Button(l33t_frame, image=convert_img, command=convertToL33t)
l33t_button.grid(column=2, row=1)

l33t_copy_button = tk.Button(l33t_frame, image=copy_img, command=lambda: copyPwd('convert'))
l33t_copy_button.grid(column=3, row=1)

# generate password upon program start
generatePwd()

root.mainloop()
