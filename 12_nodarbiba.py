# pop
saraksts = [ 0, 23, 4, 5, 11 ]
print(saraksts)
print(saraksts.pop(2)) # indekss
print(saraksts)

vardnica = {
    "Indekss1": False,
    "Vardnica": -1,
    2131: 342,
    123: 123,
}
print(vardnica)
vardnica.pop("Vardnica")
print(vardnica)
# Sintakse: <mainigais>.pop(<atslega>)

# Uzdevums:
# Izņemt no vārdnīcas vardnica katru otro vērtību (pāra sk. atslēgas)
# Nemainīt doto kodu. Neveidot jaunu vārdnīcu.
import random
vardnica = {}
for i in range(1, 41):
    vardnica[i] = random.randint(0, 100)
# # for i in range(1, len(vardnica), 2):
# #     vardnica.pop(i)
# # for i in range(1, len(vardnica)):
# #     if i % 2 == 0:
# #         vardnica.pop(i)

# # Tehniski pareizākais variants - jo atslēgas var būt teksts (str)
# # un var nebūt secīgi skaitļi
a = 0
for i in list(vardnica.keys()):
    if a % 2 == 0:
        vardnica.pop(i)
    a += 1

# json
import json
vardnica = {
    "Indekss1": False,
    "Vardnica": -1,
    2131: 342,
    123: 123,
}
print(vardnica)
print(json.dumps(vardnica))
vardnica = json.loads('{"Indekss1": false, "Vardnica": -1, "2131": 342, "123": 123}')
print(vardnica)
print(vardnica["2131"])
# Vecāka sintakse - lūdzu neizmantot
# f = open('fails.txt', 'w')
# f.close()
# Faila atvēršanas režīmi: https://docs.python.org/3/library/functions.html#open
# Faila atvēršana (a = papildināšana, w = rakstīšana pārrakstot)
with open('fails.txt', 'a') as f:
    f.write('Kaut kas\n')
# Vairāku rindu ielāde no faila
with open('fails.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
        
# Uzdevums
# Izvadīt failā 'fails.txt' skaitļus no 1 līdz 100. Katru skaitli
# izvadīt atsevišķā rindā.
with open('fails.txt', 'w') as f:
    for i in range (1, 101):
        f.write(str(i) + "\n")

import json
vardnica = {
    "Indeks1": False,
    "Vardnica": -1,
    2131: 342,
    123: 123,
}
# JSON saglabāšana failā
with open('fails.json', 'w') as f:
    json.dump(vardnica, f)
# JSON ielāde no faila
with open('fails.json', 'r') as f:
    vardnica = json.load(f)
    print(vardnica)
    print(vardnica["Indeks1"])
