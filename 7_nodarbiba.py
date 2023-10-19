# Uzdevums: Ir dots kāds vārds, piem. 'Siers'
# Uzrakstīt programmu ar ciklu, kas 
# izvada burta 'S' (gan lielā, gan mazā)
# pozīcijas vārdā (piem. vārdam Siers - 1, 5)
def findLetter(str):
    y = 0
    while y < len(str):
        if str[y] == 's' or str[y] == 'S':
            print(y+1)
        y += 1

x = "Siers"
findLetter(x)
print()
findLetter("skurstenis") # 1,5,10
print()
findLetter("lielas saulesbrilles") # 6, 8, 13, 20

# Uzdevums:
# Uzrakstīt programmu, kas ar ciklu (neizmantot .replace() fun.)
# samaina vārdā visus burtus ar patskaņu (ā ī ū ē)
# garumzīmēm pret burtiem bez garumzīmēm
# Piem - Māja => Maja, Mašīna => Mašina
def changeLetter(str):
    vards = str
    y = 0
    while y < len(vards):
        if vards[y] == 'ā':
            vards = vards[:y] + 'a' + vards[y+1:]
        elif vards[y] == 'ī':
            vards = vards[:y] + 'i' + vards[y+1:]
        elif vards[y] == 'ū':
            vards = vards[:y] + 'u' + vards[y+1:]
        elif vards[y] == 'ē':
            vards = vards[:y] + 'e' + vards[y+1:]
        y += 1
    return vards
print(changeLetter("Māja"))
print(changeLetter("Mašīna"))

# Uzdevums: Uzrakstīt programmu kas apvieno divus sarakstus
# piem. Saraksts 1 - [ 10, 20, 30 ], Saraksts 2 - [ 50, 60, 70]
# Rezultāts - [ 10, 50, 20, 60, 30, 70 ]
import random
x = [ int(random.random()*100), int(random.random()*100), int(random.random()*100) ]
y = [ int(random.random()*100), int(random.random()*100), int(random.random()*100) ]
print(x, y)
z = []
a = 0
while a < len(x):
    z.append(x[a])
    z.append(y[a])
    a += 1
print(z)

# Uzdevums: Blokshēma un Programma
# Spēlei uzmini skaitli (2. darbs uz i/ni)
# bet ar dzīvībām (piem. max 5 mēģinājumi)
import random
skaitlis = int(random.random()*100)
dzivibas = 5
while dzivibas > 0:
    minejums = int(input("Minējums: "))
    if minejums==skaitlis:
        break
    elif minejums > skaitlis:
        print("Skaitlis ir mazaks")
    else:
        print("Skaitlis ir lielaks")
    dzivibas = dzivibas - 1

if dzivibas > 0:
    print("Uzvara")
else:
    print("Zaudejat")
print(f"skaitlis bija '{skaitlis}'!")