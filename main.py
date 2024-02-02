import random
print("Lütfen şifrenizi 4 ten büyük olacak şekilde isteyiniz!")
sayi=int(input("Kaç harfli bir şifre oluşturmak istersiniz:"))
sifre=""
semboller="+-/*!&$#?=@.:"
sayilar="1234567890"
bharfler="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kharfler="abcdefghijklnopqrstuvwxyz"

for i in range(sayi):
    if i%4 == 0:
        sifre += random.choice(semboller)
    elif i%4 == 1:
        sifre += random.choice(sayilar)
    elif i%4 == 2:
        sifre += random.choice(bharfler)
    elif i%4 == 3:
        sifre += random.choice(kharfler)        


print(sifre)
