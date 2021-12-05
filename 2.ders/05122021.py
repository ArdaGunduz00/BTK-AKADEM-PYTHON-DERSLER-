print("""   HESAP MAKİNESİ
      1- TOPLAMA
      2- ÇIKARMA
      3- ÇARPMA
      4- BÖLME
        """)
secim = input("Lütfen bir seçim yapınız:")
sayı1 = int(input("1.Lütfen sayıyı giriniz:"))
sayı2 = int(input("2.Lütfen sayıyı giriniz:"))
if secim =="1":
    print ("Sayılarınızın toplamı:",sayı1+sayı2)
elif secim =="2":
    print("Sayılarınızın farkı:", sayı1 - sayı2)
elif secim =="3":
    print("Sayılarınızın çarpımı:", sayı1 *sayı2)
elif secim =="4":
     print("Sayılarınızın çarpımı:", sayı1 /sayı2)
else:
    print("Geçerli bir seçim yapınız")







