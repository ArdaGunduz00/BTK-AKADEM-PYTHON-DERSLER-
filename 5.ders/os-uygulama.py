import os
def klasor_olustur(x):
    for i in range(x):
        os.mkdir("virüs"+str(i+1))
sayi=int(input("Kaç tane klasor oluşturulsun"))
klasor_olustur(sayi)