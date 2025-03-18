import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyglet
import func

# import os
# import sys

# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS2
#     except Exception:
#         base_path = os.path.abspath(".")
#     print(os.path.join(base_path, relative_path))
#     return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Random loadout generator   *** Spread democracy randomly ***                                                                              by bezrezen")

#for local test purpose. Comment b4 building
icon = PhotoImage(file = '.\\randomdive\\favicon.png')

#for executable purpose only. Uncomment b4 building
#icon = PhotoImage(file = 'favicon.png')

root.iconphoto(False, icon)
root.geometry()
root.resizable(False, False)

#for executable purpose. Uncomment b4 building
#pyglet.font.add_file('fonts/FS Sinclair Medium.otf')

#for local test purpose. Comment b4 building
pyglet.font.add_file('.\\randomdive\\fonts\\FS Sinclair Medium.otf')

questionmark_placeholder = tk.PhotoImage(file=f'{func.home_dir}question.png')
questionmark_placeholder_wide = tk.PhotoImage(file=f'{func.home_dir}question_wide.png')

strat_1_pic = None
strat_2_pic = None
strat_3_pic = None
strat_4_pic = None
armor_pic = None
passive_pic = None
primary_pic = None
secondary_pic = None
grenade_pic = None


#warbonds checked or not. Checked by default
ca = IntVar(value=1)
ce = IntVar(value=1)
dd = IntVar(value=1)
ff = IntVar(value=1)
pp = IntVar(value=1)
sof = IntVar(value=1)
sv = IntVar(value=1)
te = IntVar(value=1)
ul = IntVar(value=1)
vc = IntVar(value=1)

#roll modes checked or not
balanced_toggled = IntVar(value=0) #checked by default TODO
weapons_toggled = IntVar(value=0) #UNchecked by default


def roll_loadout():
    global strat_1_pic, strat_2_pic, strat_3_pic, strat_4_pic, armor_pic, passive_pic, primary_pic, secondary_pic, grenade_pic

    warbonds = ['default_pack','ca','ce','dd','ff','pp','sof','sv','te','ul','vc']

    if ca.get() == 0: warbonds.remove('ca')
    if ce.get() == 0: warbonds.remove('ce')
    if dd.get() == 0: warbonds.remove('dd')
    if ff.get() == 0: warbonds.remove('ff')
    if pp.get() == 0: warbonds.remove('pp')
    if sof.get() == 0: warbonds.remove('sof')
    if sv.get() == 0: warbonds.remove('sv')
    if te.get() == 0: warbonds.remove('te')
    if ul.get() == 0: warbonds.remove('ul')
    if vc.get() == 0: warbonds.remove('vc')


    
    #strats = func.roll_stratagems(warbonds)
    strats = func.roll_item('','stratagems',4,warbonds)
    armor = func.roll_item('','armor',1,warbonds)
    passive = func.roll_item('','passives',1,warbonds)
    strat_1_changed_image = tk.PhotoImage(file=f'{strats[0]}')
    strat_2_changed_image = tk.PhotoImage(file=f'{strats[1]}')
    strat_3_changed_image = tk.PhotoImage(file=f'{strats[2]}')
    strat_4_changed_image = tk.PhotoImage(file=f'{strats[3]}')
    armor_changed_image = tk.PhotoImage(file=f'{armor[0]}')
    passive_changed_image = tk.PhotoImage(file=f'{passive[0]}')

    if weapons_toggled.get() == 1:
        primary = func.roll_item('weapons','primary',1,warbonds)
        secondary = func.roll_item('weapons','secondary',1,warbonds)
        grenade = func.roll_item('weapons','grenade',1,warbonds)
        primary_changed_image = tk.PhotoImage(file=f'{primary[0]}')
        secondary_changed_image = tk.PhotoImage(file=f'{secondary[0]}')
        grenade_changed_image = tk.PhotoImage(file=f'{grenade[0]}')
        primary_pic.config(image=primary_changed_image)
        primary_pic.image = primary_changed_image
        secondary_pic.config(image=secondary_changed_image)
        secondary_pic.image = secondary_changed_image
        grenade_pic.config(image=grenade_changed_image)
        grenade_pic.image = grenade_changed_image

    strat_1_pic.config(image=strat_1_changed_image)
    strat_1_pic.image = strat_1_changed_image
    strat_2_pic.config(image=strat_2_changed_image)
    strat_2_pic.image = strat_2_changed_image
    strat_3_pic.config(image=strat_3_changed_image)
    strat_3_pic.image = strat_3_changed_image
    strat_4_pic.config(image=strat_4_changed_image)
    strat_4_pic.image = strat_4_changed_image
    armor_pic.config(image=armor_changed_image)
    armor_pic.image = armor_changed_image
    passive_pic.config(image=passive_changed_image)
    passive_pic.image = passive_changed_image

#roll btton
roll_btn = tk.Button(text="Roll for your loadout",width= 40,height=2,command=roll_loadout,font=('FS Sinclair Medium',20))
roll_btn.grid(row=0, column=0,columnspan=6, ipadx=6, ipady=6, padx=4, pady=4,sticky=EW)

#labels above rolled items
stratagems_upper = tk.Label(text="stratagems",font=('FS Sinclair Medium',14))
stratagems_upper.grid(row=1,columnspan=4,column=0, ipadx=2, ipady=2, padx=3, pady=3)

armor_upper = tk.Label(text="armor",font=('FS Sinclair Medium',14))
armor_upper.grid(row=1,column=4, ipadx=2, ipady=2, padx=3, pady=3)

passive_upper = tk.Label(text="passive",font=('FS Sinclair Medium',14))
passive_upper.grid(row=1,column=5, ipadx=2, ipady=2, padx=3, pady=3)


#stratagem labels
strat_1_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
strat_1_pic.grid(row=2,column=0, ipadx=2, ipady=2, padx=3, pady=3, sticky=W)

strat_2_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
strat_2_pic.grid(row=2,column=1, ipadx=2, ipady=2, padx=3, pady=3, sticky=W)

strat_3_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
strat_3_pic.grid(row=2,column=2, ipadx=2, ipady=2, padx=3, pady=3, sticky=W)

strat_4_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
strat_4_pic.grid(row=2,column=3, ipadx=2, ipady=2, padx=3, pady=3, sticky=W)


#armor and passive labels
armor_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
armor_pic.grid(row=2,column=4, ipadx=10, ipady=2, padx=5, pady=2, sticky=E)

passive_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
passive_pic.grid(row=2,column=5, ipadx=1, ipady=2, padx=1, pady=2, sticky=E)

#weapons upper text
primary_upper = tk.Label(text="primary",font=('FS Sinclair Medium',14))
primary_upper.grid(row=3,column=0, ipadx=2, ipady=2, padx=3, pady=3)

secondary_upper = tk.Label(text="secondary",font=('FS Sinclair Medium',14))
secondary_upper.grid(row=3,column=2, ipadx=2, ipady=2, padx=3, pady=3)

grenade_upper = tk.Label(text="grenade",font=('FS Sinclair Medium',14))
grenade_upper.grid(row=3,column=4, ipadx=2, ipady=2, padx=3, pady=3)

#weapons labels
primary_pic = tk.Label(width=220, height=120, image=questionmark_placeholder_wide)
primary_pic.grid(row=4,column=0,columnspan=2, ipadx=2, ipady=2, padx=2, pady=2, sticky=NW)

secondary_pic = tk.Label(width=220, height=120, image=questionmark_placeholder_wide)
secondary_pic.grid(row=4,column=2,columnspan=2, ipadx=2, ipady=2, padx=2, pady=2, sticky=NW)

grenade_pic = tk.Label(width=120, height=120, image=questionmark_placeholder)
grenade_pic.grid(row=4,column=4, ipadx=2, ipady=2, padx=2, pady=2, sticky=NW)


#warbonds upper text
warbonds_upper = tk.Label(text="WARBONDS",font=('FS Sinclair Medium',16))
warbonds_upper.grid(row=6,column=1, columnspan=3, ipadx=2, ipady=2, padx=3, pady=3)


#warbonds checkboxes
ca_check = tk.Checkbutton(text="Chemical\nAgents",onvalue=1, variable=ca,font=('FS Sinclair Medium',13))
ca_check.grid(row=7,column=0, ipadx=2, ipady=2)

ce_check = tk.Checkbutton(text="Cutting\nEdge",onvalue=1, variable=ce,font=('FS Sinclair Medium',13))
ce_check.grid(row=7,column=1, ipadx=2, ipady=2)

dd_check = tk.Checkbutton(text="Democratic\nDetonation",onvalue=1, variable=dd,font=('FS Sinclair Medium',13))
dd_check.grid(row=7,column=2, ipadx=2, ipady=2)

pp_check = tk.Checkbutton(text="Polar\nPatriots",onvalue=1, variable=pp,font=('FS Sinclair Medium',13))
pp_check.grid(row=7,column=4, ipadx=2, ipady=2)

ff_check =  tk.Checkbutton(text="Freedom\nFlames",onvalue=1, variable=ff,font=('FS Sinclair Medium',13))
ff_check.grid(row=7,column=3, ipadx=2, ipady=2)

sof_check = tk.Checkbutton(text="Servants\nof Freedom",onvalue=1, variable=sof,font=('FS Sinclair Medium',13))
sof_check.grid(row=7,column=5, ipadx=2, ipady=2)

sv_check = tk.Checkbutton(text="Steeled\nVeterans",onvalue=1, variable=sv,font=('FS Sinclair Medium',13))
sv_check.grid(row=8,column=0, ipadx=2, ipady=2)

te_check = tk.Checkbutton(text="Truth\nEnforcers",onvalue=1, variable=te,font=('FS Sinclair Medium',13))
te_check.grid(row=8,column=1, ipadx=2, ipady=2)

ul_check = tk.Checkbutton(text="Urban\nLegends",onvalue=1, variable=ul,font=('FS Sinclair Medium',13))
ul_check.grid(row=8,column=2, ipadx=2, ipady=2)

vc_check = tk.Checkbutton(text="Viper\nCommandos",onvalue=1, variable=vc,font=('FS Sinclair Medium',13))
vc_check.grid(row=8,column=3, ipadx=2, ipady=2)


#modes upper text
modes_upper = tk.Label(text="MODES",font=('FS Sinclair Medium',16))
modes_upper.grid(row=9,column=1, columnspan=3, ipadx=2, ipady=2, padx=3, pady=3)


#roll modes checkboxes
balanced_check = tk.Checkbutton(text = 'Balanced', onvalue=1, variable=balanced_toggled,font=('FS Sinclair Medium',13),state = 'disabled')
balanced_check.grid(row=10, column=1, columnspan=2, ipadx=2, ipady=2, padx=2, pady=2, sticky=W)

weapons_check = tk.Checkbutton(text="Randomize\nweapons",onvalue=1, variable=weapons_toggled,font=('FS Sinclair Medium',13))
weapons_check.grid(row=10, column=4, columnspan=2, ipadx=2, ipady=2, padx=2, pady=2, sticky=W)


root.mainloop()