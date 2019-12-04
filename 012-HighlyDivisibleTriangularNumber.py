from functions import divisors

n, sayi = 1, 1

while(len(divisors(sayi))<500):
    n += 1
    sayi += n

print(sayi)
