"""
kendisine gönderilen kullanıcı adı ve şifreyi kotrol ederek sonucunda Trıe ya da false gönderen fonksiyonun python kodu
lıllanıcıadı:adönin,şifre:123456 olmalı
"""
def admingiris(kullanıcıadı,sifre):
    if kullanıcıadı=="admin" and sifre=="123456":
        return True
    else:
        return False
while True:
    kullanıcıadı2=input("Kullanıcı adı giriniz:")
    kullannıcısifre2=(input("Şifre giriniz"))
    if admingiris(kullanıcıadı2,kullannıcısifre2)==True:
        print("Giriş başarılı")
        break
    else:
        print("Yanlış Şifre Ya Da Parola")




