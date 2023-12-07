# Var pildīt mājās. Termiņš līdz nākošajai nedēļai. Par katru uzdevumu ir līdz 3 punktiem - 3 ir perfekti izpildīts, 2 ir izpildīts bet ar mazām kļūdām, 1 ir 'iesākts', un 0 ir 'neiesākts'.
# Dotos koda piemērus nemainīt - tikai papildināt

# 1. Uzdevums - piekļuve vārdnīcu vērtībām
# Ir dota sekojoša programma. Papildinat to, lai izvadītu aritmētisko vidējo vērtību vārdnīcas ierakstu vērtībām.
# piemēram vārdnīcai { 0: 100, 1: 2, 3: 400 } rezultāts būtu - "Lielākā - 3: 400, mazākā 1: 2".
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})
# ...

# 2. Uzdevums - vārdnīcu izveide
# Ir dota informācija par skolēniem divos sarakstos. Pirmais saraksts satur skolēnu vārdus. Otrais saraksts satur skolēnu atzīmes. Vērtība pirmajā sarakstā, pēc indeksa atbilst vērtībai otrajā sarakstā. Sarakstu garums ir identisks.
# Izveidojat programmu, kas ar cikla palīdzību izveido sarakstu ar vārdnīcām no šiem 2 sarakstiem. Vārdnīcai ir jābūt strukturētai sekojošā veidā: 
# {
#    "skolena_vards": vards,
#    "skolena_atzimes": [atzimes]
# }
skolenu_vardi = [ "Jānis", "Ernests", "Beāte", "Maija" ]
skolenu_atzimes = [ [1, 3, 5, 6], [2, 5, 9, 7], [5, 7, 6, 10], [1, 9, 2, 8] ]
sakartota_informacija = []

# 3. Uzdevums - Vērtību dzēšana
# Ir dota sekojoša programma, kas izveido vārdnīcu dict1. Papildinat šo programmu tā,
# lai šī programma izveidotu _izdzēstu_ vērtības no dict1, kas ir mazākas par 500.
# Nedrīkst veidot atsevišķu vārdnīcu vai papildus mainīgos - visām darbībām jānotiek ar dict1.
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})

# 4. Uzdevums - Vērtību ielāde un apstrāde
# Ir dots fails 'uzdevums.json'. Šis fails satur vārdnīcu json formātā. Atverat šo failu un izvadat šīs vārdnīcas vērtības formātā 
# "Atslēga: <atslēga>, Vērtība: <vērtība>" (ieskaitot leņķa iekavas - <>).

# 5. Uzdevums - Vērtību glabāšana
# Izveidot programmu, kas nodrošina -
# Vairāku (! - saraksts) cilvēku informācijas ievadi - vārdu, uzvārdu, vecumu. Informāciju par individuālu cilvēku glabāt vārdnīcā ar atslēgām "vards", "uzvards" un "vecums".
# Šīs informācijas izvadi failā ar nosaukumu 'dati.json'.