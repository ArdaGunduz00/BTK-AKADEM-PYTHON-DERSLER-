"""
kullanıcıdan 10 tane isim alarak isimler adında bir listeye tanımlayınız
"""
isimler = []
for i in range(5):
    isim = input(str(i+1)+".İsim Giriniz:")
    isimler.append((isim))
for i in range (5):
    print(str(i+1)+".isim",isimler[i])
#ödev:bir veya 2 basamaklı bir sayı giridliğinde okunşunu yazsın örnek: 12 girdi çıktığısı oniki
#örnek 56 girdi çıktıısı ellialtı parçalamam gerekir: 10 a tam bölme// 2ye ulaşmak için 10
#böldüğünde kalan 12½10=2 sonucunu verir

#sayginoztunc@gmail.com
#github sandıkodasi
#metaverse ve sanaltarla araştırılcak
