import random
#bilgisiyar sabit bir sayı tutsun, örn 10 kullanıcı tahmin etmeye çalışşın,büyük  ve ya küçült diyerek yönelndirsin
#bulunca tebrikler desin
sayi = random.randint(1,10)# bir ile 10 arasında rasgtele sayı
tahminsayi = int(input("Sayıyı giriniz:"))
if tahminsayi> sayi:
    print("Sayıyı küçült")
elif tahminsayi<sayi:
    print("Sayıyı Büyült")
elif tahminsayi==sayi:
    print("Tebrikler buldunuz")
else:
    print("Geçerli bir değer giriniz")
