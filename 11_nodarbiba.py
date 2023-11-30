# Uzdevums
# Izveidot programmu, kura izveido vārdnīcu kurai
# Atslēgas ir skaitļi no 0 līdz 10
# Vērtības šīm atslēgām ir gadījumskaitļi (random)
# neaizmirstam: import random
import random
vardnica = {}
for i in range(1, 11):
    #vardnica[i] = random.randint(0, 100)
    vardnica.update({i: random.randint(0, 100)})
print(vardnica)

# Uzdevums
# Izveidot programmu, kas no dotajām vārdnīcām izveido trešo,
# apvienoto vārdnīcu (satur atslēgas un vērtības no vardnica1 un 
# vardnica2).
# import random
# vardnica1 = {
#     1: 10,
#     "2": 30,
#     4: random.randint(0,100)
# }
# vardnica2 = {
#     3: "!!!",
#     5: random.randint(0,100),
#     6: False
# }
# vardnica3 = {}
# for atslega, vertiba in vardnica1.items():
#     vardnica3[atslega] = vertiba
# for atslega, vertiba in vardnica2.items():
#     vardnica3[atslega] = vertiba
# print(vardnica3)
# for vardnica in (vardnica1, vardnica2):
#     vardnica3.update(vardnica)
# print(vardnica3)

# Uzdevums
# Izveidot vārdnīcu no sarakstiem atslegas un vertibas,
# kur saraksts atslegas ir vertibas, un saraksts vertibas ir šo
# atslēgu vērtības. Ir garantēts, ka abi saraksti ir vienāda garuma.
atslegas = [ 1, "2", 3, -1, 5 ]
vertibas = [ "!", -1, True, random.randint(0, 100), [1,2,4]]
#vardnica = {}
# for i in range(0, len(atslegas)):
#     vardnica[atslegas[i]] = vertibas[i]
vardnica = dict(zip(atslegas, vertibas))
print(vardnica)

# Uzdevums
# Izveidot programmu, kas izfiltrē atslēgas un vērtības no 
# vardnica1, kuras ir lielākas par 500 un ievieto tās vardnica2.
# Piemēram, ja vardnica1 = {0: 337, 1: 600, 2: 266, 3: 580 }
# tad vardnica2 = { 1: 600, 3: 580 }
import random
vardnica = {}
for i in range(0, 1000):
    vardnica[i] = random.randint(0, 1000)
vardnica2 = {}
# ...