vardnica = {
    "atslega": "vertiba",
    "atslega2": "vertiba2",
    "cookie":
        ["A small, usually flat and crisp cake made from sweetened dough.", 
         " A person, usually of a specified kind"],
    123: True
}

print(vardnica["atslega"])

saraksts = []
saraksts.append("2")

vardnica.update({"atslega3": "vertiba!", "atslega4": "..."})
vardnica["jauna_atslega"] = "!!!"

print(vardnica)

# Uzdevums: Aizpildīt vārdnīcu ar vērtībām no 1: 1 līdz n: n^2, kur
# n ir lietotāja ievadīts skaitlis
# Izejas piemērs: n = 3
# {
#   1: 1
#   2: 4
#   3: 9
# }
n = int(input("Ievade: "))
vardnica = {}
# Te būs cikls, kurā katrā iterācijā augs skaitlis un vērtība:
#vardnica[1] = 1
#vardnica[2] = 4
# ....
for o in range(1, n+1):
    vardnica[o] = o**2 # o^2
    #vardnica[o] = o*o # o^2
    #vardnica.update({o: o*o})
    #vardnica.update({o: o**2})
print(vardnica)

# for i in vardnica.keys(): # == [ 1, 2, 3]
#     print(i)
# for i in vardnica.values(): # == [ 1, 4, 9]
#     print(i)
# for i,j in vardnica.items():
#     print(i,j)
#if 3 in vardnica.keys():
if 3 in vardnica:
    print("True")
else:
    print("False")

# Uzdevums:
# Uzrakstīt programmu, kas ar ciklu (neizmantot .replace() fun.)
# samaina vārdā visus burtus ar patskaņu (ā ī ū ē)
# garumzīmēm pret burtiem bez garumzīmēm
# Piem - Māja => Maja, Mašīna => Mašina
burtuVardnica = {
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ū": "U",
    "š": "s",
}
def changeLetter(str):
    # vards = str
    # y = 0
    # while y < len(vards):
    #     if vards[y] == 'ā':
    #         vards = vards[:y] + 'a' + vards[y+1:]
    #     elif vards[y] == 'ī':
    #         vards = vards[:y] + 'i' + vards[y+1:]
    #     elif vards[y] == 'ū':
    #         vards = vards[:y] + 'u' + vards[y+1:]
    #     elif vards[y] == 'ē':
    #         vards = vards[:y] + 'e' + vards[y+1:]
    #     y += 1
    # return vards
    jaunaisVards = ""
    y = 0
    while y < len(str):
        if str[y] in burtuVardnica:
            jaunaisVards += burtuVardnica[str[y]]
        else:
            jaunaisVards += str[y]
        y += 1
    return jaunaisVards
print(changeLetter("Māja"))
print(changeLetter("Mašīna"))

# Uzdevums: Pārveidot vārdnīcas "vardnica" vērtības reizinot tās kvadrātā
# Piemērs rezultātam:
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16  
# }
vardnica = {
    1: 1,
    "2": 2,
    "n": 3,
    "4": 4,
    6: 10,
}
# for i in vardnica.keys():
#     print(i)
# VAI
# for i,j in vardnica.items():
#     print(i,j)
for i in vardnica.keys():
    print(f"i: {i}")
    print(f"Vērtība vārdnīcā ar atslēgu i: {vardnica[i]}")
    vardnica[i] = vardnica[i] * vardnica[i]
# for i,j in vardnica.items():
#     vardnica[i] = vardnica[i] * vardnica[i]
print(vardnica)
