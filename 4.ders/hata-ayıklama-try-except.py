while True:
    try: #hata verebilecek bu blok içine yazılır
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))
        print(sayi2+sayi1)
        break
    except ValueError:
        print("Lütfen bir sayı giriniz!")
    except ZeroDivisionError:
        print("Bir sayı 0 a bölünmez!")
#    except: #       print(" Burası genel hata mesajı")
#       print(" Burası genel hata mesajı")

