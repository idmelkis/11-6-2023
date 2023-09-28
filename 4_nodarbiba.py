# Uzdevums: FizzBuzz
# Programma izvada skaitļus no 1-100 (cikls), bet
# ja skaitlis dalās ar 3, tad tiek izvadīts 'Fizz'
# ja skaitlis dalās ar 5, tad tiek izvadīts 'Buzz'
# ja dalās gan ar 3, gan 5, tad tiek izvadīts 'FizzBuzz'
# Dalījuma atlikuma pārbaudei var izmantot modulus operatoru (%)
# -- piemērs. (x % 3 == 0)
# Piemērs programmas izvadei:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# ...
# 14
# FizzBuzz
# 16
# ... 
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

# Uzdevums (i/ni), jāiesniedz e-klasē
# "Uzmini skaitli" spēli
# Tiek uzģenerēts skaitlis no 0 līdz 100 
import random
x = int(random.random()*100)
# (Ciklā) lietotājs ievada skaitli
# Programma saglabā lietotāja ievadi sarakstā
# Programma pārbauda vai ievadītais skaitlis ir vienāds ar uzģenerēto
# Ja nav, programma izvada to, vai ģenerētais skaitlis ir lielāks/mazāks
# Kad lietotājs uzvar spēli, programma izvada 'uzvara', un
# izvada visus lietotāja minējumus, kopā ar minējumu skaitu.

#def fun_nosaukums(x, y, z):
    # ...

# Funkcijas definīcija
def sum(x :int, y :int) -> int:
    """Saskaita divus skaitļus"""
    return x+y
x = sum(10, 2)
print(x)

def fun() -> int:
    return 0
fun()

#import math
# Funkcija no cita faila
from nodarbiba24 import divide
print(divide(10, 2))

# Standarta vērtība
def minus_x(x :int, y :int = 5) -> int:
    return x - y
print(minus_x(15))
print(minus_x(15, 10))

# Bezgalīgs parametru skaits
def infinite_params(x: int, *param):
    print(param)
infinite_params(0, 10, 20, 30, 40, 4553)

# Funkcija funkcijā
def fun1(x):
    def fun2(y):
        return y
    return fun2(2)+x
print(fun1(10))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(4)) # 1 * 2 * 3 * 4 = 24

n = 4
total = 1
while n > 0:
    total *= n
    n -= 1
print(total)

# Uzdevums: funkcija kas saskaita visas ievades
# Ievade - lietotājs ievada vairākus skaitļus [cikls, input]
# Programma saglabā šīs ievades (saraksts?)
# Programma padod šīs ievades funkcijai kā argumentu
# programma iterē cauri sarakstam, saskaita šos skaitļus