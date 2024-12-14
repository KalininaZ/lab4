import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())  # Получаем длину пароля из поля ввода
    if length <= 0:
        result_label.config(text="Password length must be greater than 0.")
        return

    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += "!@#$%"

    if not characters:
        result_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    result_label.config(text=password)


#Создаем графический интерфейс
root = tk.Tk()
root.title("Password Generator")

#Длина
length_label = tk.Label(root, text="Длина пароля:")
length_label.grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

#Буквы нижнего регистра
lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Буквы [a-z]", variable=lowercase_var)
lowercase_check.grid(row=1, column=0, sticky="w")

#Цифры
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Цифры [0-9]", variable=numbers_var)
numbers_check.grid(row=2, column=0, sticky="w")

#Символы
symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Символы [!@#$%]", variable=symbols_var)
symbols_check.grid(row=3, column=0, sticky="w")


#Кнопка генерации
generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2)

#Результат
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()


