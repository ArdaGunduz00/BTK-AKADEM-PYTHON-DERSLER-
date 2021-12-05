"""
kullanıcıdan alıcagınız degerlerle dikdörtgenin alanını ve çevresini  hesaplayınız
"""


secim = input("Alan ya da Çevre giriniz:").lower()#girilen yazıların hepisini küçük harfe çevirir
if secim=="alan":
    uzunkenar = int(input("Dikdörtgenin uzun kenarını giriniz:"))
    kisakenar = int(input("Dikdörtgenin kısa kenarını giriniz:"))
    print("Dikdörtgenin alanı:",kisakenar*uzunkenar)

elif secim=="çevre":
     uzunkenar = int(input("Dikdörtgenin uzun kenarını giriniz"))
     kisakenar = int(input("Dikdörtgenin kısa kenarını giriniz"))
     print("Dikdörtgenin çevresi:",2*(kisakenar+uzunkenar))
else:
    print("Lütfen alan ya da çevre yazınız")




