import tkinter as tk

# main window
root = tk.Tk()
root.title("Counter App")
root.geometry("300x250")

count = 0

# function to increase counter
def increase():
    global count
    count += 1
    label.config(text=str(count))

# function to decrease counter
def decrease():
    global count
    count -= 1
    label.config(text=str(count))

# function to reset counter
def reset():
    global count
    count = 0
    label.config(text=str(count))


# counter display
label = tk.Label(root, text="0", font=("Arial", 40))
label.pack(pady=20)

# buttons
increase_btn = tk.Button(root, text="Increase", command=increase)
increase_btn.pack(pady=5)

decrease_btn = tk.Button(root, text="Decrease", command=decrease)
decrease_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.pack(pady=5)

root.mainloop()
