saraksts = [ "T", str(2), "k", "a" ]
saraksts.append("s")
print(saraksts)

# while <expr>:
while True:
    print("Kaut kas")
    break

# for .. 
for x in range(0, 10):
    print(x*2)

saraksts = [ "T", str(2), "k", "a" ]
for vertiba in saraksts:
    print(vertiba, end="") 

print() #print("kautkas") == kautkas\n

length = len(saraksts)
index = 0
while index < length:
    print(saraksts[index], end="")
    index += 1

# Uzdevums: masīvā x saglabāt 10 lietotāja ievades. Var lietot
#while 
# vai
#for
# ciklu.


# Izvada katru otro vērtību
saraksts = [ "T", str(2), "k", "a" ]
for vertiba in saraksts[0::2]:
    print(vertiba, end=",")

# Uzdevums: Uzrakstat ciklu, kas izvada sekojošu izvadi:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# Uzdevums: For cikls, kas izvada skaitļus no 0 līdz 10
# atskaitot skaitļus 4 un 6
