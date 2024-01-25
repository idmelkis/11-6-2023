# Jāizveido klase "Banka Konts". 
class BankasKonts:
  # * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
  atlikums = 0.0
  def __str__(self):
    return f"Konta ir {self.atlikums}"
  # * Izveidojat funkcijas, kas ļauj ieskaitīt un/vai izņemt naudu no konta
  def ieskaitit(self, summa):
    self.atlikums += summa
  def iznemt(self, summa):
    # * Neļaut lietotājam izņemt naudu, 
    #   ja kontā ir zem €50 (if...)
    if self.atlikums >= 50:
       self.atlikums -= summa
    else:
       print("Nevar iznemt")
# Izveidojat apakšklasi "Krājkonts" (manto no "Bankas konts").
class Krajkonts(BankasKonts):
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju,
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110).
  def iznemt(self, summa):
    self.atlikums -= summa + (summa*0.10)
# Izveidojat objektus no šīm klasēm
# jana_konts = Krajkonts()...
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100),
#   izsaucat izņemšanas funkciju €60.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €90
# Izvadat abu kontu atlikumus
konts1 = BankasKonts()
konts1.ieskaitit(100)
konts1.iznemt(60)
print(konts1)
konts2 = Krajkonts()
konts2.ieskaitit(100)
konts2.iznemt(90)
print(konts2)

# + Precēm var izveidot klasi "Prece". 
class Prece:
  # + Šī klase satur preces nosaukumu un cenu (abas vērtības uzstāda init funkcijā)
  nosaukums: str = ""
  cena: float = ""
  def __init__(self, _nosaukums, _cena) -> None:
    self.nosaukums = _nosaukums
    self.cena = _cena
  def __str__(self) -> str:
    return f"{self.nosaukums}"
  # + vai izmantot vārdnīcu.
  # { "nosaukums": cena }

# Izveidojat klasi "Grozs".
class Grozs:
  # Šī klase satur preces un to daudzumu. 
  preces :'dict[Prece, float]' = {} # Prece: daudzums
  # Klasei "Grozs" jānodrošina funkcijas, 
  #   + kas ļauj pievienot preces, 
  def pievienot(self, _prece :Prece, _daudzums :float):
    self.preces[_prece] = _daudzums
  #   + un aprēķināt groza kopējo vērtību (preču vērtība * to skaits)
  def aprekinat_vertibu(self) -> float:
    vertiba = 0.0
    for key, value in self.preces.items():
      vertiba += key.cena * value # cena * daudzums
    return vertiba
  def __str__(self) -> str:
    return f"Groza vērtība: {self.aprekinat_vertibu()}."
  #   + izņemt preces
  # def iznemt(self, nosaukums :str):
  #   for key in self.preces.keys():
  #     if nosaukums == key.nosaukums:
  #       self.preces.pop(key)
  def iznemt(self, _prece :Prece):
    self.preces.pop(_prece)
        
prece1 = Prece("Piens", 1.0)
prece2 = Prece("Maize", 0.5)
grozs = Grozs()
grozs.pievienot(prece1, 1)
grozs.pievienot(prece2, 2)
print(grozs)
grozs.iznemt(prece2)
print(grozs)

# Izveidojat klasi, kura pieņem katru rindu kā parametrus inicializatora funkcijai
class Darbinieks:
  id :int
  vards :str
  alga :float
  amats :str
  stazs :int
  def __init__(self, _id, _vards, _alga, _amats, _stazs) -> None:
    self.id = _id
    self.vards = _vards
    self.alga = _alga
    self.amats = _amats
    self.stazs = _stazs
  # Izveidojat funkciju, kura izvada objekta (darbinieka) datus
  def __str__(self) -> str:
    return f"ID: {self.id}, Vārds: {self.vards}, Alga: {self.alga}, Amats: {self.amats}, Stāžs: {self.stazs}, Izmaksāts: {self.izmaksats()}"
  # Izveidojat funkciju, kas aprēķina cik daudz naudas ir izmaksāts darbiniekam
  #   (mēnešalga * stāžs), piem. Jānim ir izmaksāts 24*1000 eur.
  def izmaksats(self) -> float:
    return self.alga * self.stazs

# Izveidojat objektus, kas satur visus dotos datus
# Doti sekojoši dati: 
# ID	    Vārds	   Alga (mēn)	    Amats	                Stāžs (mēn)
# "1",    "Jānis",   1000,         "Slotas operators",        24
# "2",    "Ēriks",   2000,         "Tirgotājs",	            30
# "3",    "Anna",    500,          "Laborante",	            2
# "4",    "Kārlis",  9001,         "Direktors",               36
janis = Darbinieks(1, "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks(2, "Ēriks", 2000, "Tirgotājs", 30)
anna = Darbinieks(3, "Anna", 500, "Laborante", 2)
karlis = Darbinieks(4, "Kārlis", 9001, "Direktors", 36)
print(janis)
print(eriks)
print(anna)
print(karlis)