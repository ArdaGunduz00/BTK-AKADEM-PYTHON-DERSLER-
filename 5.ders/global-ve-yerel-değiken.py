b=20 #burasi global degisken, her yerde kullanilabilir
def fonksiyon():
    global b #dışarıdaki bir değişkeni fonksiyon içinde kullanabiliriz ve değerini değiştirebiliriz
    a=10 #burada a yerel degiskendir. sadece fonksiyonun içinde kullanılabilir
    print(b)

#print(a) değişkeni fonksiyon içinde oalcağı için kullanamayız
#yere değişken
fonksiyon()
print(b) #global b olarak tanımladğımız için ekrana 4 yazar
#eğer global b demeseydik ekrana 20 basardı