import paho.mqtt.client as mqtt
import tkinter as tk

#       ____  ____     _        ____  ____  ___
# ____ |_   ||   _| __| | ____ | _  ||_   ||_  \
# |____| / | ||  |_ |__  ||____|| \|_| / | | _|> |
#      |/\__/|____|   |_|      \__|  |/\__/|___/
# argituri              28.8.2018


# Display a given text w/ tkinter
# "explicit is better than implicit"
root = tk.Tk()
root.attributes("-fullscreen", True)


def key(event):
    print("pressed"), repr(event.char)
    root.attributes("-fullscreen", False)


root.bind("<Key>", key)
# separator = tk.Frame()
# separator.pack(fill='both', padx=5, pady=5)
print("root width: " + str(root.winfo_width()) + ", height: " + str(root.winfo_height()))
c = tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height())
c.pack()
c.create_text(100, 200, text="hello")


# e = tk.Entry(c)
# e.pack()
# e.delete(0, 'end')
# e.insert(0, "a default value")


#    e.delete(0, 'end')
#   e.insert(0, 'pressed')

def puttext(text):
    print("hello")


tk.mainloop()
