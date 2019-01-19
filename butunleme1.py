from functions import allprimes
from functions import isprime
import random
deneme = 0
koltuklar=allprimes(100)
while(len(koltuklar)>0):
    tercih = random.randint(1,200)%98
    deneme += 1
    if(isprime(tercih)==1 and koltuklar.count(tercih)==1):
        koltuklar.remove(tercih)
print(deneme)

