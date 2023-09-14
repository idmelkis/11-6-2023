# if <Loģiskā pārbaude>:
#    ...
"""
if "1" == str(1):
    print("Patiess")
patiess = True # False
if patiess:
    print("Arī patiess")

y = input("Ievade: ")
print(f"Ievadīts: {y}")
"""

x = [ 123, 456, 789 ]
print(x[1])
print(x[:2])
y = "Teksts" # == [ "T", "e", "k", "s", "t", "s" ]
print(y[1:4])
print(y[:4])
print(y[4:])

# Ievade: <Cilvēka> vārds
# Izvade: Sveiks <cilvēk>!
# Piem, ievade: Jānis
# Izvade: Sveiks Jāni!
#vards = "Jānis"
#vards = input("Vārds: ")
#print(f"Sveiks {vards[:-1]}!")
#print(f"Sveiks {vards[:len(vards)-1]}!")

#saraksts = [ "T", "e", "k", "s", "t", "s" ]
saraksts = [ "T", str(2), "k", "a" ]
print(",".join(saraksts)) # Apvieno sarakstu vienā tekstā
print(len(saraksts)) # Izvada teksta vai saraksta garumu

# Tuple
tuple = ( "T", str(2), "k", "a" )
print(tuple[2])

saraksts[2] = "e"
print(saraksts)
tuple[2] = "e" # Būs kļūda - Tuple nevar izmainīt

# ... Cikli
