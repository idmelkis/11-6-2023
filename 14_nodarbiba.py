# Polimorfisms
# Viena funkcija dažādās vidēs dara dažādas lietas
# class Auto:
#     marka :str = ""
#     krasa = ""
#     ieslegts :bool = False
#     def kautkada_funkcija(self):
#         print("Automašīna")
# class Lidmasina:
#     marka :str = ""
#     krasa = ""
#     ieslegts :bool = False
#     def kautkada_funkcija(self):
#         print("Lidmašīna")
# bmw = Auto()
# airbus = Lidmasina()
# for i in (bmw, airbus):
#     i.kautkada_funkcija()

# Mantošana
class Transportlidzeklis:
    marka :str = "Nedefinēts"
    krasa = ""
    ieslegts :bool = False
    def __init__(self) -> None:
        print("Izveidojām transportlīdzekli")
    def kautkada_funkcija(self):
        print("Kaut kas")
class Auto(Transportlidzeklis):
    krasa :str = "melna"
    durvju_skaits :int = 4
    def __init__(self) -> None:
        print("Izveidojām automašīnu")
    def kautkada_funkcija(self):
        pass
class Lidmasina(Transportlidzeklis):
    sparnu_platums :float = 10.0

bmw = Auto()
bmw.kautkada_funkcija()
print(bmw.krasa)
print(bmw.durvju_skaits)

#transports = Transportlidzeklis()
#print(transports.durvju_skaits)
airbus = Lidmasina()

# Uzdevums: Izveidojiet bāzes klasi, un mantojošo klasi. 
# Tēma: Pēc brīvas izvēles.
# Bāzes klasei divus mainīgos, vienu funkciju (var būt primitīva funkc. ar print())
# Mantojošā klase - unikāls mainīgais, pārrakstām funkciju

# Uzdevums i/ni: Izveidot programmu (var grafiku - neobligāti)
# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt un/vai izņemt naudu no konta
# def ieskaitit(???, ???):
# ...
# def iznemt(???, ???):
# ...
# * Neļaut lietotājam izņemt naudu, 
#   ja kontā ir zem €50 (if...)
# Izveidojat apakšklasi "Krājkonts" (manto no "Bankas konts").
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju,
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110).
# Izveidojat objektus no šīm klasēm
# jana_konts = Krajkonts()...
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100),
#   izsaucat izņemšanas funkciju €60.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €90
# Izvadat abu kontu atlikumus