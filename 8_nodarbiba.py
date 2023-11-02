# 1. Uzdevums 
# uzrakstīt Programmu, kas ar ciklu izvada režģi ar simbolu #
# Izmēru ievada lietotājs
# Piem. - Izmērs - 4
# Izvada
"""
# # # #
# # # #
# # # #
# # # #
"""
# izmers = int(input("Režģa izmērs: "))
# for iii in range(0, izmers):
#     for jjj in range(0, izmers): # Jaunas rindas simbols - \n
#         print("#", end=" ")
#     print()

# 2. Uzdevums 
# Aprēķināt attālumu starp diviem punktiem (x1, y1), (x2, y2)
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# import math
# distance = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
# print(distance)

# 3. Uzdevums
# Izveidot programmu, kas pārveido no Celsija uz Fārenheitu vai otrādi.
# Ievades: 
# Grādi
# Kurā virzienā konvertējam
# Izvades:
# Temperatūra
# virziens = input("Virziens kurā konvertējam (celsijs/farenheits): ")
# gradi = int(input("Grādi: "))
# if virziens == "farenheits":
#     print(gradi * 9/5 + 32)
# elif virziens == "celsijs":
#     print((gradi - 32) * 5/9)

# 4. Uzdevums
# Izveidot programmu, kas uzzīmē histogrammas stabiņus, kuru izmēru nosaka lietotājs
# Ievades:
#   Stabiņu skaits
#   Izmēri
# Izvade: 
""" Ievade: 2, 5, 6
#####
######
"""
# skaits = int(input("Skaits: "))
# stabinu_izmeri = []
# for iii in range(0, skaits):
#     x = input(f"Stabins {iii}: ")
#     stabinu_izmeri.append(int(x))
# for iii in stabinu_izmeri:
#     for jjj in range(0, iii):
#         print("#", end="")
#     print()
#print("Rinda 1", end="")
#print("Rinda 2")

# 5. Uzdevums
# Jāizveido programmu, kas pieņem kādu teikumu, un izvada simbolu un vārdu skaitu
# Ievade: Teikums
# Izvade: Simbolu skaits, vārdu skaits
ievade = input()
simboli = 0
vardi = 0
for burts in ievade:
    simboli += 1
    if burts == ' ':
        vardi += 1
vardi += 1 # Jo pēc pēdējā vārda nav atstarpes
print(simboli)
print(vardi)