#kullanıcıya ortalamasını sorarak takdir  teşekkür veya hiçbir şey alamadınız şeklinde mesaj veren python uygulamınasını
#fonksiyon kullanarak yapınız
def sonuc(ortalama):
    if 85<ortalama<100:
        print("Takdir alabiliyorsun")
    elif ortalama<85 and ortalama>=75:
        print("Teşekkür alabiliyorsun")
    else:
        print("Hiçbir şey alamadınız")
try:
    ort=int(input("Ortalama giriniz:"))
    sonuc(ort)
except ValueError:
    print("Sayısal değer giriniz")