from tkinter import *

logs = Tk()
logs.title("Kases aparāts")
logs.geometry("800x700")
logs.configure(bg='#E5E5E5')

# Definē cenas katram produktam
cenas = {
    "Ābols": 0.99,
    "Bumbieris": 1.20,
    "Apelsīns": 1.50,
    "Mandarīni": 1.80,
    "Sīpoli": 0.70,
    "Tomāts": 1.30,
    "Gurķis": 1.00,
    "Paprika": 2.00
}

# Globālais mainīgais, kas uzglabās kopējo cenu
kopēja_cena = 0

def augļi_darzeņi_logs():
    global ābols
    global Bumbieris
    global Apelsīns
    global Mandarīni
    global Sīpoli
    global Tomāts
    global Gurķis
    global Paprika

    auglu_darzenuLogs = Toplevel()
    auglu_darzenuLogs.geometry('500x400')
    auglu_darzenuLogs.title('Augļi un dārzeņi')

    # Pievieno pogas katram produktam
    ābols = Button(auglu_darzenuLogs, text='Ābols', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Ābols"))
    ābols.place(x=80, y=50)
    Bumbieris = Button(auglu_darzenuLogs, text='Bumbieris', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Bumbieris"))
    Bumbieris.place(x=80, y=100)
    Apelsīns = Button(auglu_darzenuLogs, text='Apelsīns', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Apelsīns"))
    Apelsīns.place(x=80, y=150)
    Mandarīni = Button(auglu_darzenuLogs, text='Mandarīni', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Mandarīni"))
    Mandarīni.place(x=80, y=200)
    Sīpoli = Button(auglu_darzenuLogs, text='Sīpoli', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Sīpoli"))
    Sīpoli.place(x=270, y=50)
    Tomāts = Button(auglu_darzenuLogs, text='Tomāts', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Tomāts"))
    Tomāts.place(x=270, y=100)
    Gurķis = Button(auglu_darzenuLogs, text='Gurķis', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Gurķis"))
    Gurķis.place(x=270, y=150)
    Paprika = Button(auglu_darzenuLogs, text='Paprika', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Paprika"))
    Paprika.place(x=270, y=200)

def lietotaja_izvēle(produkts):
    global kopēja_cena

    kopēja_cena += cenas[produkts]  # Sareizināt izvēlēto produktu cenu ar tā cenu
    kases_aprāts_ekrāns.insert(END, produkts + " - €" + str(cenas[produkts]) + "\n")
    kases_aprāts_ekrāns.insert(END, "Kopā: €" + str(round(kopēja_cena, 2)) + "\n")

# GUI sākotnējie elementi
augli_darzeni_poga = Button(logs, text='Augļu un dārzeņi', fg='white', bg='#3b3b3b', width=30, height=3, command=augļi_darzeņi_logs)
augli_darzeni_poga.place(x=85, y=60)

kases_aprāts_ekrāns = Text(logs, width=40, height=15, bg='lightblue', font='Helvetica', padx=10, pady=10)
kases_aprāts_ekrāns.place(x=350, y=55)

# Ritinātājs
ritinātājs = Scrollbar(logs)
kases_aprāts_ekrāns.config(yscrollcommand=ritinātājs.set)
ritinātājs.config(command=kases_aprāts_ekrāns.yview)
ritinātājs.place(x=770, y=55, height=300)

logs.mainloop()
