import tkinter as tk
from tkinter import ttk
import random

choices = []
for i in range(1,5):
    choices.append(random.randint(1,48))


root = tk.Tk()
root.title("Dive generator")
root.geometry("630x280")

questionmark_placeholder = tk.PhotoImage(file='./randomdive/question.gif')
banner = questionmark_placeholder #tk.PhotoImage(file=u"C:/Users/User/Desktop/myprojects/randomdive/strat_icons/(40).png")



strat_1_image = questionmark_placeholder
strat_1_changed_image = tk.PhotoImage(file=f'./randomdive/strat_icons/({choices[0]}).png')
strat_2_changed_image = tk.PhotoImage(file=f'./randomdive/strat_icons/({choices[1]}).png')
strat_3_changed_image = tk.PhotoImage(file=f'./randomdive/strat_icons/({choices[2]}).png')
strat_4_changed_image = tk.PhotoImage(file=f'./randomdive/strat_icons/({choices[3]}).png')
armor_pass_changed_image = tk.PhotoImage(file=f'./randomdive/strat_icons/({choices[0]}).png')

def roll_for_stratagem():

    strat_1 = tk.Label(root, width= 120, image= strat_1_changed_image).grid(row=3, column=1)
    strat_2 = tk.Label(root, width= 120, image= strat_2_changed_image).grid(row=3, column=2)
    strat_3 = tk.Label(root, width= 120, image= strat_3_changed_image).grid(row=3, column=3)
    strat_4 = tk.Label(root, width= 120, image= strat_4_changed_image).grid(row=3, column=4)
    armor_passive = tk.Label(root, width= 150, image= armor_pass_changed_image).grid(row=3, column=5)


strat_1 = tk.Label(root, width= 120, image= questionmark_placeholder).grid(row=3, column=1)
strat_2 = tk.Label(root, width= 120, image= questionmark_placeholder).grid(row=3, column=2)
strat_3 = tk.Label(root, width= 120, image= questionmark_placeholder).grid(row=3, column=3)
strat_4 = tk.Label(root, width= 120, image= questionmark_placeholder).grid(row=3, column=4)
armor_passive = tk.Label(root, width= 150, image = questionmark_placeholder).grid(row=3, column= 5)

seaf_logo = tk.Label(root, width= 150, image = banner).grid(row=4, column=1, columnspan=5)

roll_bttn = tk.Button(root, width= 50, text = "Roll your loadout", command = roll_for_stratagem).grid(row=1, column=1, columnspan=5, rowspan= 2)

root.mainloop()
