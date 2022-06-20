import tkinter as tk
from tkinter import filedialog as fd
from random import choice

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

file_path = fd.askopenfilename(parent=root)
with open(file_path, 'r', encoding='utf-8') as file:
    pool1 = [line.split()[0] for line in file.readlines()]

file_path = fd.askopenfilename(parent=root)
with open(file_path, 'r', encoding='utf-8') as file:
    pool2 = [line.split()[0] for line in file.readlines()]

file_path = fd.askopenfilename(parent=root)
with open(file_path, 'r', encoding='utf-8') as file:
    pool3 = [line.split()[0] for line in file.readlines()]

s = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ss = "f,dult`;pbqrkvyjghcnea[wxio]sm'.z"

orig = s + s.upper()
repl = ss + ss.upper()

# выбор слов
w1 = pool1[choice(range(len(pool1)))]
w2 = pool2[choice(range(len(pool2)))]
w3 = pool3[choice(range(len(pool3)))]

prepass = w1[:3].capitalize() + w2[:3].capitalize()  + w3[:3].capitalize() 

finalpool = []
for sym in prepass:
    pos = orig.index(sym)
    finalpool.append(repl[pos])

finalpass = ''.join(finalpool)

print("Фраза для запоминания: " + w1.capitalize() + " " + w2.capitalize() + " " + w3.capitalize()) 
print("Пароль: " + finalpass)