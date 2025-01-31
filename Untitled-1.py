from tkinter import *
from collections import Counter

logs = Tk()
logs.title("Kases aparāts")
logs.geometry("800x700")
logs.configure(bg='#E5E5E5')

pirkums_pabeigts = False

produkta_cenas = {
    "Ābols": 0.50,
    "Bumbieris": 0.75,
    "Apelsīns": 1.00,
    "Tomāts": 0.80,
    "Gurķis": 0.60,
    "Paprika": 1.10,

    # Gaļas produkti
    "Vistas gaļa": 5.00,
    "Liellopu gaļa": 7.00,
    "Cūkgaļa": 6.50,
    "Jēra gaļa": 8.00,
    "Teļa gaļa": 9.00,
    "Tītara gaļa": 6.00,
    "Pīles gaļa": 7.50,
    "Truša gaļa": 8.50,

    # Graudu produkti
    "Griķi": 2.50,
    "Rīsi": 1.80,
    "Makaroni": 1.50,
    "Auzas": 1.20,
    "Grūbas": 1.30,
    "Kvinoja": 4.50,
    "Kuskuss": 2.20,
    "Bulgurs": 2.00,

    # Saldētie produkti
    "Pelmeņi": 3.50,
    "Dārzeņu maisijums": 2.80,
    "Augļu maisijums": 3.20,
    "Frī kartupeļi": 2.50,
    "Saldējums": 3.00,
    "Pica": 4.50,
    "Kārtainā mīkla": 2.00,
    "Ledus": 1.00,

    # Piena produkti
    "Piens": 1.20,
    "Siers": 5.50,
    "Biezpiens": 2.80,
    "Krējums": 1.50,
    "Saldais krējums": 1.80,
    "Paniņas": 0.90,
    "Sviests": 2.50,
    "Jogurts": 1.30
}


#################################### Augļu logs
def augļi_darzeņi_logs():
    global auglu_darzenuLogs

    auglu_darzenuLogs = Toplevel()
    auglu_darzenuLogs.geometry('500x400')
    auglu_darzenuLogs.title('Augļi un dārzeņi')
    ābols = Button(auglu_darzenuLogs, text='Ābols', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Ābols"))
    ābols.place(x=80, y=50)
    Bumbieris = Button(auglu_darzenuLogs, text='Bumbieris', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Bumbieris"))
    Bumbieris.place(x=80, y=100)
    Apelsīns = Button(auglu_darzenuLogs, text='Apelsīns', fg='white', bg='#3b3b3b', width=12, height=2,
                      command=lambda: lietotaja_izvēle("Apelsīns"))
    Apelsīns.place(x=80, y=150)
    Mandarīni = Button(auglu_darzenuLogs, text='Mandarīni', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Mandarīni"))
    Mandarīni.place(x=80, y=200)
    Sīpoli = Button(auglu_darzenuLogs, text='Sīpoli', fg='white', bg='#3b3b3b', width=12, height=2,
                    command=lambda: lietotaja_izvēle("Sīpoli"))
    Sīpoli.place(x=270, y=50)
    Tomāts = Button(auglu_darzenuLogs, text='Tomāts', fg='white', bg='#3b3b3b', width=12, height=2,
                    command=lambda: lietotaja_izvēle("Tomāts"))
    Tomāts.place(x=270, y=100)
    Gurķis = Button(auglu_darzenuLogs, text='Gurķis', fg='white', bg='#3b3b3b', width=12, height=2,
                    command=lambda: lietotaja_izvēle("Gurķis"))
    Gurķis.place(x=270, y=150)
    Paprika = Button(auglu_darzenuLogs, text='Paprika', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Paprika"))
    Paprika.place(x=270, y=200)


################## Gaļas logs
def Gaļas_atver_logu():
    Gaļas_logs = Toplevel()
    Gaļas_logs.geometry('500x400')
    Gaļas_logs.title("Gaļas produkti")
    Vistas_gaļa = Button(Gaļas_logs, text='Vistas gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                         command=lambda: lietotaja_izvēle("Vistas gaļa"))
    Vistas_gaļa.place(x=80, y=50)
    Liellopu_gaļa = Button(Gaļas_logs, text='Liellopu gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                           command=lambda: lietotaja_izvēle("Liellopu gaļa"))
    Liellopu_gaļa.place(x=80, y=100)
    Cūkgaļa = Button(Gaļas_logs, text='Cūkgaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Cūkgaļa"))
    Cūkgaļa.place(x=80, y=150)
    Jēra_gaļa = Button(Gaļas_logs, text='Jēra gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Jēra gaļa"))
    Jēra_gaļa.place(x=80, y=200)
    Teļa_gaļa = Button(Gaļas_logs, text='Teļa gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Teļa gaļa"))
    Teļa_gaļa.place(x=270, y=50)
    Tītara_gaļa = Button(Gaļas_logs, text='Tītara gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                         command=lambda: lietotaja_izvēle("Tītara gaļa"))
    Tītara_gaļa.place(x=270, y=100)
    Pīles_gaļa = Button(Gaļas_logs, text='Pīles gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                        command=lambda: lietotaja_izvēle("Pīles gaļa"))
    Pīles_gaļa.place(x=270, y=150)
    Truša_gaļa = Button(Gaļas_logs, text='Truša gaļa', fg='white', bg='#3b3b3b', width=12, height=2,
                        command=lambda: lietotaja_izvēle("Truša gaļa"))
    Truša_gaļa.place(x=270, y=200)


def Graudu_produkti_atver_logu():
    global Graudu_produkti_logs

    Graudu_produkti_logs = Toplevel()
    Graudu_produkti_logs.geometry('500x400')
    Graudu_produkti_logs.title("Graudu produkti")
    Griķi = Button(Graudu_produkti_logs, text='Griķi', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Griķi"))
    Griķi.place(x=80, y=50)
    Rīsi = Button(Graudu_produkti_logs, text='Rīsi', fg='white', bg='#3b3b3b', width=12, height=2,
                  command=lambda: lietotaja_izvēle("Rīsi"))
    Rīsi.place(x=80, y=100)
    Makaroni = Button(Graudu_produkti_logs, text='Makaroni', fg='white', bg='#3b3b3b', width=12, height=2,
                      command=lambda: lietotaja_izvēle("Makaroni"))
    Makaroni.place(x=80, y=150)
    Auzas = Button(Graudu_produkti_logs, text='Auzas', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Auzas"))
    Auzas.place(x=80, y=200)
    Grūbas = Button(Graudu_produkti_logs, text='Grūbas', fg='white', bg='#3b3b3b', width=12, height=2,
                    command=lambda: lietotaja_izvēle("Grūbas"))
    Grūbas.place(x=270, y=50)
    Kvinoja = Button(Graudu_produkti_logs, text='Kvinoja', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Kvinoja"))
    Kvinoja.place(x=270, y=100)
    Kuskuss = Button(Graudu_produkti_logs, text='Kuskuss', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Kuskuss"))
    Kuskuss.place(x=270, y=150)
    Bulgurs = Button(Graudu_produkti_logs, text='Bulgurs', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Bulgurs"))
    Bulgurs.place(x=270, y=200)


def Saldētie_produkti_atver_logu():
    global Saldētie_produkti_logs

    Saldētie_produkti_logs = Toplevel()
    Saldētie_produkti_logs.geometry('500x400')
    Saldētie_produkti_logs.title("Graudu produkti")
    Pelmeņi = Button(Saldētie_produkti_logs, text='Pelmeņi', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Pelmeņi"))
    Pelmeņi.place(x=80, y=50)
    Dārzeņu_maisijums = Button(Saldētie_produkti_logs, text='Dārzeņu maisijums', fg='white', bg='#3b3b3b', width=12,
                               height=2, command=lambda: lietotaja_izvēle("Dārzeņu maisijums"))
    Dārzeņu_maisijums.place(x=80, y=100)
    Augļu_maisijums = Button(Saldētie_produkti_logs, text='Augļu maisijums', fg='white', bg='#3b3b3b', width=12,
                             height=2, command=lambda: lietotaja_izvēle("Augļu maisijums"))
    Augļu_maisijums.place(x=80, y=150)
    Frī_kartupeļi = Button(Saldētie_produkti_logs, text='Frī kartupeļi', fg='white', bg='#3b3b3b', width=12, height=2,
                           command=lambda: lietotaja_izvēle("Frī kartupeļi"))
    Frī_kartupeļi.place(x=80, y=200)
    Saldējums = Button(Saldētie_produkti_logs, text='Saldējums', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Saldējums"))
    Saldējums.place(x=270, y=50)
    Pica = Button(Saldētie_produkti_logs, text='Pica', fg='white', bg='#3b3b3b', width=12, height=2,
                  command=lambda: lietotaja_izvēle("Pica"))
    Pica.place(x=270, y=100)
    Kārtainā_mīkla = Button(Saldētie_produkti_logs, text='Kārtainā mīkla', fg='white', bg='#3b3b3b', width=12, height=2,
                            command=lambda: lietotaja_izvēle("Kārtainā mīkla"))
    Kārtainā_mīkla.place(x=270, y=150)
    Ledus = Button(Saldētie_produkti_logs, text='Ledus', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Ledus"))
    Ledus.place(x=270, y=200)


def piena_produkti_atver_logs():
    global piena_produkti_logs

    piena_produkti_logs = Toplevel()
    piena_produkti_logs.geometry('500x400')
    piena_produkti_logs.title("Piena produkti")
    Piens = Button(piena_produkti_logs, text='Piens', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Piens"))
    Piens.place(x=80, y=50)
    Siers = Button(piena_produkti_logs, text='Siers', fg='white', bg='#3b3b3b', width=12, height=2,
                   command=lambda: lietotaja_izvēle("Siers"))
    Siers.place(x=80, y=100)
    Biezpiens = Button(piena_produkti_logs, text='Biezpiens', fg='white', bg='#3b3b3b', width=12, height=2,
                       command=lambda: lietotaja_izvēle("Biezpiens"))
    Biezpiens.place(x=80, y=150)
    Krējums = Button(piena_produkti_logs, text='Krējums', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Krējums"))
    Krējums.place(x=80, y=200)
    Saldais_krējums = Button(piena_produkti_logs, text='Saldais krējums', fg='white', bg='#3b3b3b', width=12, height=2,
                             command=lambda: lietotaja_izvēle("Saldais krējums"))
    Saldais_krējums.place(x=270, y=50)
    Paniņas = Button(piena_produkti_logs, text='Paniņas', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Paniņas"))
    Paniņas.place(x=270, y=100)
    Sviests = Button(piena_produkti_logs, text='Sviests', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Sviests"))
    Sviests.place(x=270, y=150)
    Jogurts = Button(piena_produkti_logs, text='Jogurts', fg='white', bg='#3b3b3b', width=12, height=2,
                     command=lambda: lietotaja_izvēle("Jogurts"))
    Jogurts.place(x=270, y=200)


####################################### pogas
augli_darzeni_poga = Button(logs, text='Augļu un dārzeņi', fg='white', bg='#3b3b3b', width=30, height=3,
                            command=augļi_darzeņi_logs)
gaļas_poga = Button(logs, text='Gaļas', fg='white', bg='#3b3b3b', width=30, height=3, command=Gaļas_atver_logu)
graudu_produkti_poga = Button(logs, text='Graudu produkti', fg='white', bg='#3b3b3b', width=30, height=3,
                              command=Graudu_produkti_atver_logu)
saldētie_produkti_poga = Button(logs, text='Saldētie produkti', fg='white', bg='#3b3b3b', width=30, height=3,
                                command=Saldētie_produkti_atver_logu)
piena_produkti_poga = Button(logs, text='Piena produkti', fg='white', bg='#3b3b3b', width=30, height=3,
                             command=piena_produkti_atver_logs)

augli_darzeni_poga.place(x=85, y=60)
gaļas_poga.place(x=85, y=130)
graudu_produkti_poga.place(x=85, y=200)
saldētie_produkti_poga.place(x=85, y=270)
piena_produkti_poga.place(x=85, y=340)
########################################


kases_aprāts_ekrāns = Text(logs, width=40, height=15, bg='lightblue', font='Helvetica', padx=10, pady=10)
kases_aprāts_ekrāns.place(x=350, y=55)

ritinātājs = Scrollbar(logs)

lietotaja_preces = []


####### izmantoju AI
def lietotaja_izvēle(produkts):
    global cena

    if produkts in produkta_cenas:
        cena = produkta_cenas[produkts]
        lietotaja_preces.append((produkts, cena))
        kases_aprāts_ekrāns.insert(END, f"{produkts} - €{cena:.2f}\n")


def nonemt_preces():
    if lietotaja_preces:
        lietotaja_preces.pop()
        kases_aprāts_ekrāns.delete(1.0, END)
        for produkts, cena in lietotaja_preces:
            kases_aprāts_ekrāns.insert(END, f"{produkts} - €{cena:.2f}\n")


#########################


################## Kases aparāta funkcionalitāte
summa_text = Label(logs, text="Kopā: €0.00", font=("Helvetica", 12), bg='#E5E5E5')
summa_text.place(x=630, y=420)

# Inicializācija
cena = 0
lietoja_preces = []

# Funkcija, lai aprēķinātu un atjauninātu kopējo summu
def kopējā_summa():
    kopējā_cena = sum(cena for produkts, cena in lietotaja_preces)
    summa_text.config(text=f"Kopā: €{kopējā_cena:.2f}")

# Funkcija, kas apstrādā produkta izvēli
def lietotaja_izvēle(produkts):
    global cena

    if produkts in produkta_cenas:
        cena = produkta_cenas[produkts]
        lietotaja_preces.append((produkts, cena))
        kases_aprāts_ekrāns.insert(END, f"{produkts} - €{cena:.2f}\n")
        kopējā_summa() 
nonemt_preces_poga = Button(logs, text='Noņemt pēdējo preci', fg='white', bg='red', command=nonemt_preces, padx=27,
                            pady=20)
nonemt_preces_poga.place(x=440, y=580)







poga_1 = Button(logs, text="1 cents", bg='lightgrey', padx=20, pady=20)
poga_1.place(x=50, y=420)
poga_2 = Button(logs, text="2 centi", bg='lightgrey', padx=20, pady=20)
poga_2.place(x=140, y=420)
poga_3 = Button(logs, text="5 centi", bg='lightgrey', padx=20, pady=20)
poga_3.place(x=230, y=420)
poga_4 = Button(logs, text="10 centi", bg='lightgrey', padx=18, pady=20)
poga_4.place(x=50, y=500)
poga_5 = Button(logs, text="20 centi", bg='lightgrey', padx=18, pady=20)
poga_5.place(x=140, y=500)
poga_6 = Button(logs, text="50 centi", bg='lightgrey', padx=18, pady=20)
poga_6.place(x=230, y=500)
poga_7 = Button(logs, text="1 Eiro", bg='lightgrey', padx=24, pady=20)
poga_7.place(x=50, y=580)
poga_8 = Button(logs, text="2 Eiro", bg='lightgrey', padx=24, pady=20)
poga_8.place(x=140, y=580)
poga_9 = Button(logs, text="5 Eiro", bg='lightgrey', padx=24, pady=20)
poga_9.place(x=230, y=580)
poga_10 = Button(logs, text="10 Eiro", bg='lightgray', padx=20, pady=20)
poga_10.place(x=350, y=420)
poga_11 = Button(logs, text='20 Eiro', bg='lightgray', pady=20, padx=20)
poga_11.place(x=440, y=420)
poga_12 = Button(logs, text="50 Eiro", bg='lightgrey', pady=20, padx=20)
poga_12.place(x=530, y=420)
poga_13 = Button(logs, text='100 Eiro', bg='lightgrey', pady=20, padx=107)
poga_13.place(x=350, y=500)

poga_enter = Button(logs, text="enter", bg='lightgreen', padx=20, pady=20, command=kopējā_summa)
poga_enter.place(x=350, y=580)

poga_pabiegt_pirkumu = Button(logs, text="Pabeigt pirkumu", bg='lightgreen', padx=20, pady=20)
poga_pabiegt_pirkumu.place(x=620, y=580)

logs.mainloop()