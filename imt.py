import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100

    bmi = weight / (height ** 2)

    if bmi < 16:
        interpretation = "Резко выраженнный недостаток веса"
    elif  16 <= bmi < 18.5:
        interpretation = "недостаток веса"
    elif 18.5 <= bmi < 25:
        interpretation = "Нормальный вес"
    elif 25 <= bmi < 30:
        interpretation = "Избыточный вес"
    else:
        interpretation = "Ожирение"

    bmi_result.config(text="ИМТ: " + str(round(bmi, 2)))  # Вывод ИМТ
    interpretation_result.config(text="Интерпретация: " + interpretation)  # Вывод интерпретации

root = tk.Tk()

weight_label = tk.Label(root, text="Вес (кг):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Рост (см):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Вычислить ИМТ:", command=calculate_bmi)
calculate_button.pack()

bmi_result = tk.Label(root, text="")
bmi_result.pack()

interpretation_result = tk.Label(root, text="")
interpretation_result.pack()

root.mainloop()