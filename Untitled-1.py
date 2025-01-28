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

# Globālie mainīgie
kopēja_cena = 0
lietotaja_preces = []
preces_daudzums = {}

# Funkcija, kas atjauno ekrānu ar kopējo cenu
def atjaunot_ekrānu():
    kases_aprāts_ekrāns.delete(1.0, END)  # Dzēš visu esošo tekstu
    for produkts in lietotaja_preces:
        daudzums = preces_daudzums.get(produkts, 1)  # Ja daudzums nav norādīts, uzstādām pēc noklusējuma 1
        kases_aprāts_ekrāns.insert(END, f"{produkts} - {daudzums} gab. - €{cenas[produkts] * daudzums:.2f}\n")
    kases_aprāts_ekrāns.insert(END, f"\nKopā: €{round(kopēja_cena, 2)}\n")

# Funkcija, kas pievieno preces izvēli
def lietotaja_izvēle(produkts):
    global kopēja_cena
    lietotaja_preces.append(produkts)
    preces_daudzums[produkts] = 1  # Sākumā pieņemam, ka daudzums ir 1
    kopēja_cena += cenas[produkts]
    atjaunot_ekrānu()

# Funkcija, kas atjauno daudzumu, kad tiek nospiests cipars
def ievadit_daudzumu(cipars):
    if lietotaja_preces:
        produkts = lietotaja_preces[-1]  # Ņem pēdējo pievienoto produktu
        preces_daudzums[produkts] = preces_daudzums.get(produkts, 1) * 10 + cipars  # Atjaunojam daudzumu
        # Pārskaitām kopējo cenu
        global kopēja_cena
        kopēja_cena = sum(cenas[produkts] * preces_daudzums.get(produkts, 1) for produkts in lietotaja_preces)
        atjaunot_ekrānu()

# Funkcija, lai pievienotu produktus un ievadītu daudzumu
def cipari_pogas(cipars):
    ievadit_daudzumu(cipars)

# GUI sākotnējie elementi
augli_darzeni_poga = Button(logs, text='Augļu un dārzeņi', fg='white', bg='#3b3b3b', width=30, height=3,)

kases_aprāts_ekrāns = Text(logs, width=40, height=15, bg='lightblue', font='Helvetica', padx=10, pady=10)
kases_aprāts_ekrāns.place(x=350, y=55)

# Ritinātājs
ritinātājs = Scrollbar(logs)
kases_aprāts_ekrāns.config(yscrollcommand=ritinātājs.set)
ritinātājs.config(command=kases_aprāts_ekrāns.yview)
ritinātājs.place(x=770, y=55, height=300)

# Ciparu pogas
for i in range(10):
    button = Button(logs, text=str(i), bg='lightgrey', padx=20, pady=20, command=lambda i=i: cipari_pogas(i))
    button.place(x=430 + (i % 3) * 70, y=380 + (i // 3) * 90)

# Testa pogas
logs.mainloop()
