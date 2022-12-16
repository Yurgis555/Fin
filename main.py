#Biudžetas


from biudzetas import Biudzetas
from irasas import Irasas
from pajamuirasas import PajamuIrasas
from islaiduirasas import IslaiduIrasas

mano_biudzetas = Biudzetas()

while True:
    print("Pasirinkite veiksmą: ")
    print("1 - Įvesti pajamas")
    print("2 - Įvesti išlaidas")
    print("3 - Gauti balansą")
    print("4 - Gauti ataskaitą")
    print("0 - Išeiti iš programos")
    pasirinkimas = input("Ivesk Nr. : ")
    if pasirinkimas == "1":
        print("Įveskite pajamas: ")
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
        print("Pajamos įvestos sėkmingai!")
    if pasirinkimas == "2":
        print("Įveskite išlaidas: ")
        suma = float(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        print("Išlaidos įvestos sėkmingai!")
    if pasirinkimas == "3":
        print(f"Sąskaitos balansas: {mano_biudzetas.gauti_biudzeto_balansa()}")
    if pasirinkimas == "4":
        mano_biudzetas.gauti_ataskaita()
    if pasirinkimas == "0":
        break
