#Soru 1: 3 ve 5'in katları
#3'ün veya 5'in katı olan 10'dan küçük tüm doğal sayıları listelersek, 3, 5, 6, ve 9'u elde ederiz. Bu katların toplamı 23'tür.

#3'ün veya 5'in 1000'den küçük tüm katlarının toplamını bulunuz.
list=[]
for i in range (3,1000):
    if i%3==0 or i%5==0 :
        list.append(i) 
print(sum(list))		
    
