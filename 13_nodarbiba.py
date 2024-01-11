## Parametri
# + Marka
# + Riteņu skaits
# + Krāsa
# + Ātrumkārbas modelis
# + Ātrums
## Darbības - Metodes
# - Paātrināt
# - Bremzēt
# - Logu tīrīšana
# class <nosaukums>:
#     <parametri>
#     <funkcijas>
class Auto:
    marka :str = ""
    ritenu_skaits :int = 4
    krasa = ""
    atrumkarbas_mod :str
    atrums :float = 0.0
    ieslegts :bool = False

    def __init__(self, _marka, _krasa) -> None:
        """ Kaut kāds teksts """
        self.marka = _marka
        self.krasa = _krasa
    def __str__(self) -> str:
        return f"Marka: {self.marka}, Krasa: {self.krasa}, Ieslegta: {self.ieslegts}, Atrums: {self.atrums}"

    def paatrinat(self):
        if self.ieslegts:
            self.atrums += 0.5
        # Izmetīs kļūdu
        # self.atrumkarbas_mod = self.atrumkarbas_mod + ""
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 0.5
    def logu_tirisana(self):
        print("Tiram logus...")
    def ieslegt(self, status):
        self.ieslegts = status
    def status(auto):
        print(auto)

masina1 = Auto("BMW", "Melna")
masina1.ieslegt(True)

print(masina1)
print(type(masina1))
#masina1.status()
Auto.status(masina1)

masina2 = Auto("Audi", "Zils")
print(masina2)
#masina2.status()

masina1.paatrinat()
masina1.paatrinat()
print(masina1)