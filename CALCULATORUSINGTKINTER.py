import tkinter as tk
from tkinter import messagebox

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Main window
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20,
                       font=('Arial', 14),
                       command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew")

root.mainloop()
