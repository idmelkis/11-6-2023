a = 10
def fun():
    global a
    a = 15
    print(a)

fun()
print(a)

# Uzdevums
import random
a = int(random.random()*100)
b = int(random.random()*100)
# Funkcija, kas samaina a un b mainīgos vietām
def swap():
    global a, b
    print(a, b)
    c = a
    a = b
    b = c
swap()
# a jābūt iepriekšējai b vērtībai, b jābūt iepriekšējai a vērtībai
print(a, b)
