# # import json
# # with open("fails.json") as f:
# #     json.dump(dict,f)

# https://docs.python.org/3/library/functions.html#open
# with open("mape/fails.txt", "w") as file:
# #     # t = file.readline()
# #     # print(t)
#     # for line in file:
#     #     print(line.strip())
# #     # text = f.readline()
# #     # print(text)
#     file.write("Jauns fails!\n")

# import sys
# print(sys.argv)
# if sys.argv[1] == "--help":
#     print("...")
# import os
# dir = os.path.dirname(__file__)
# print(dir)
#print()
# os.path.exists(f"{dir}\\mape")
# os.path.isfile(f"{dir}\\mape")
# if not os.path.isdir(f"{dir}\\mape"):
#     os.mkdir(f"{dir}\\mape")

# # os.rmdir(f"{dir}\\mape")
# with open(f"{dir}\\mape\\fails.txt", "w") as file:
# #     # t = file.readline()
# #     # print(t)
#     # for line in file:
#     #     print(line.strip())
# #     # text = f.readline()
# #     # print(text)
#     file.write("Jauns fails!\n")

# # for file in os.listdir(f"{dir}\\mape"):
# #     #print(file)
# #     os.remove(f"{dir}\\mape\\{file}")
# # os.rmdir(f"{dir}\\mape")

# # import shutil
# # shutil.rmtree(f"{dir}\\mape")

# Uzdevums - Dots fails ar darbībām 
# (skaitlis, atdalīts ar atstarpi)
# 8 * 10
# 10 - 2
# 4 - 3
# Nolasīt failu un izvadīt katras 
# rindas darbības rezultātu

with open(f"fails", "r") as file:
    #file.read(<simbolu skaitu>)
    # Neiesaku - diezgan manuāls process
    # Atver failu noteiktā vietā
    # file.buffer()
    for line in file:
        # Šādi lūdzu nedarīt
        # print(eval(line.strip()))
        darb = line.strip().split(" ")
        if darb[1] == '*':
            print(int(darb[0]) * int(darb[2]))
        elif darb[1] == '-':
            print(int(darb[0]) - int(darb[2]))
        elif darb[1] == '+':
            print(int(darb[0]) + int(darb[2]))
        #print(darb)

import csv
# with open(f"fails", "r") as file:
#     csv_reader = csv.reader(file, delimiter=" ")
#     next(csv_reader)
#     for line in csv_reader:
#         print(line)
ls = ["123", "312", "sad"]
with open(f"test.csv", "w") as file:
    csv_writer = csv.writer(file, lineterminator="\n")
    #csv_writer.writerow(ls)
    csv_writer.writerows(ls)
