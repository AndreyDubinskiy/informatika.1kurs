import tkinter as tk

def calculate():
    expression = entry.get()
    result = eval(expression)
    output.config(text="Результат вычисления: " + str(result))

root = tk.Tk()

label = tk.Label(root, text="A в столбик посчитать слабо?:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Слабо:", command=calculate)
button.pack()

output = tk.Label(root, text="")
output.pack()

root.mainloop()
