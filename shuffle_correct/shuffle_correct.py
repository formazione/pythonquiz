
from tkinter import filedialog
import os
from random import shuffle
 
'''
put the question and answers into a txt file in this way

What is the capital of Italy?
Rome
Florence
Venice
Tourin
 
'''
 
 
a = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text","*.txt"),("all files","*.*")))
print(a)
with open(a, "r", encoding="utf-8") as file:
    file = file.readlines()
 
html = ""
newdom = 1
risposte = []
letters = "abcd"
countdom = 1
corrette = []
for line in file:
    if line == "\n":
        newdom = 1
        continue
    if newdom == 1:
        html += f"<b>{countdom}. {line}</b><br>"
        newdom = 0
        countdom += 1
    else:
        risposte.append(line)
    if len(risposte) == 4:
        corrette.append(f"{countdom - 1}: {risposte[0]}")
        shuffle(risposte)
        for n, risposta in enumerate(risposte):
            html += f"{letters[n]}. {risposta}<br>"
        risposte = []
        newdom = 1
        html += "<br>"
 
 
with open("output.html", "w", encoding="utf-8") as file:
    file.write(html)
filename = a.split("/")[-1]
with open(f"correttore_{filename}", "w") as file:
    file.write("".join(corrette))
os.startfile("output.html")