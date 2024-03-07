# 1. Uzdevums
# # Izveidojat mapi "faili". 
# import os
# os.mkdir("faili")

# # Izveidojat mapē failus ar nosaukumiem no 0 līdz 100.
# import random
# for i in range(0,101):
#     with open(f'faili/{i}', 'w') as f:
#         # Katrā failā noglabājat gadījumskaitli.
#         f.write(str(random.randint(0, 100000)))

# # Prasat lietotājam atvērt kādu no šiem failiem,
# #   un ievadīt vērtību, kas ir failā.
# randomFile = random.choice(os.listdir("faili"))
# #randomFile = random.randint(0, 100)
# inp = input(f"Lūdzu ievadat vērtību no faila {randomFile}: ")

# # Atkarībā no tā vai ievadīts pareizi, izvadīt "pareizi", vai "nepareizi".
# with open(f'faili/{randomFile}', 'r') as f:
#     val = f.readline()
#     if val == inp:
#         print('Pareizi')
#     else:
#         print('Nepareizi')

# # Kad programma beidz darbu, izdzēšat šo mapi.
# import shutil
# shutil.rmtree(f"faili")

# 2. Uzdevums
# with open('fails.txt', 'r') as f:
#     line = f.readline().strip()
#     splitline = line.split(" ")
#     print(f"Failā ir {len(splitline)} vārdi")

# 3. Uzdevums
# * atver šo failu
# * izveido failu ar to pašu nosaukumu + "_uppercase"
#   (piem. fails.txt -> fails_uppercase.txt). 
#   Ja fails jau eksistē izvadat kļūdu.
# * otrajā failā saglabājat pirmā faila saturu pārveidojot visus burtus par lielajiem.
#   (.upper())
import os
with open('fails.txt', 'r') as f:
    #filename = 'fails.txt'.split('.')[0]+"_uppercase.txt"
    #from pathlib import Path
    #Path('fails.txt').stem
    fileName = 'fails_uppercase.txt'
    if os.path.exists('fails_uppercase.txt'):
        print('Kļūda')
        #raise Exception('Fails jau eksistē')
    else:
        with open(fileName, 'w') as wf:
            for line in f:
                wf.write(line.upper())
        


