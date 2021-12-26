"""
Kullanıcıdan verili alarak dikdörtgen ve üçgenin çevresini hesaplayınız
hesaplamaları fonksiyon ile yapınız
"""
def cevre(uzun,kisa):
    print("Sonuç:", 2 * sayi1 + 2 * sayi2)
def alan(uzun,kisa):
    print("Sonuç:",sayi1*sayi2)
secim = input("Alan ya da Çevre giriniz:").lower()#girilen yazıların hepisini küçük harfe çevirir
sayi1=int(input("1.Sayı giriniz:"))
sayi2=int(input("2.Sayı giriniz:"))

if secim=="çevre":
    cevre(sayi1,sayi2)
elif secim=="alan":
    alan(sayi1,sayi2)
else:
    print("Bir seçim yapınız")


