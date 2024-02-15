#inp = int(input("Ievade"))
# class Klase:
#     def __init__(self) -> None:
#         pass
#     def funkcija(self):
#         def funkc():
#             a = 25
#             print(a)
#         asb = 235
#         print(asb)
#         funkc()
# for i in range (0, 20):
#     print(i)
# i = 10
# i *= 2
# i -= 10
# kl = Klase()
# kl.funkcija()
# i = 10
# j = 5
# k = i % j
# l = i / k

# Uzdevums
# Atrod mazāko skaitli sarakstā
# def min(list):
#     a = list[0]
#     for x in range(1, len(list)):
#         if list[x] < a:
#             a = list[x]
#     return a
# print(min([20, 10, 30]))
# Izņēmumu saraksts: https://docs.python.org/3/library/exceptions.html

class ManaKluda(Exception):
    def __init__(self, obligatsParametrs :str, *args: object) -> None:
        print(f"Kļūda: {obligatsParametrs}")
        super().__init__(*args)
    def kautkadaFunkc(self):
        print("Funkcija")

import traceback
class Klase:
    def __init__(self) -> None:
        #file = open('...')
        try:
            print("Vienk")
            raise ManaKluda("AAAA", "BBBBB", "CCCC") # throw
            #raise NotImplementedError("Nav izveidots")
            #raise Exception("Kļūda1")
        except NotImplementedError as e: # catch
            print(f"Notika noteikta kļūda: {e}")
        except ManaKluda as e:
            traceback.print_exc()
            e.kautkadaFunkc()
            raise e
        except Exception as _:
            print("Notika kļūda")
        finally:
            #file.close()
            print("Vienmēr palaists")
try:
    kl = Klase()
except:
    print("Apstrādāta kļūda")
print("Pēc visa koda")

inp = 0
while (True):
    try:
        inp = int(input("Ievadat skaitli: "))
        break
    except:
        print("Nepareizs skaitlis")
print(f"Ievadītais skaitlis: {inp}")