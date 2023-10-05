# Uzdevums: funkcija kas saskaita visas ievades
# Ievade - lietotājs ievada vairākus skaitļus [cikls, input]
# Programma saglabā šīs ievades. saraksts?
# Programma padod šīs ievades funkcijai kā argumentu
# programma iterē cauri sarakstam, saskaita šos skaitļus

x = []
while True:
    inp = input("Skaitlis: ")
    if inp == "x":
        break
    x.append(int(inp))

def sumArray(masivs):
    summa = 0
    for val in masivs:
        summa += val
    return summa
print(sumArray(x))