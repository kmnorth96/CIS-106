import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        quantity = float(entry_quantity.get())

        if quantity > 10000:
            price = 10
        elif quantity > 5000:
            price = 20
        else:
            price = 30

        extended_price = quantity * price
        tax = extended_price * 0.07
        total = extended_price + tax

        result_text.set(
            f"Extended Price: ${extended_price:,.2f}\n"
            f"Tax Amount: ${tax:,.2f}\n"
            f"Total: ${total:,.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Widget Price Calculator")
root.geometry("400x250")

# Input Label and Entry
tk.Label(root, text="Enter quantity of widgets:").pack(pady=10)
entry_quantity = tk.Entry(root)
entry_quantity.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result Display
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Courier", 12), justify="left").pack(pady=10)

# Run the GUI loop
root.mainloop()