import tkinter as tk

def update_display(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

display_var = tk.StringVar()
display_var.set("")

display_label = tk.Label(root, textvariable=display_var, font=("Arial", 18), anchor="e", relief="solid", width=15)
display_label.grid(row=0, column=0, columnspan=4)

button_labels = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3)
]

for (text, row, col) in button_labels:
    if text == "=":
        continue 
    button = tk.Button(root, text=text, font=("Arial", 18), width=4, height=2, command=lambda t=text: update_display(t) if t != "C" else display_var.set(""))
    button.grid(row=row, column=col, padx=5, pady=5)

equals_button = tk.Button(root, text="=", font=("Arial", 18), width=4, height=2, command=calculate)
equals_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

root.mainloop()
