
import tkinter as tk

def plus():
    global big
    big += 1
    button["text"] = f"Clicks {big}"
big = 0

root = tk.Tk()
root.geometry("2340x1224")


button = tk.Button(root, text=big, font=("Arial", 80), command=plus)
button.pack()


label = tk.Label(text=big, font=("Arial", 80))
label.pack()
root.mainloop()