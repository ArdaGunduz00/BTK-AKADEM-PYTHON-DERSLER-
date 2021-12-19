#kullanıcı adı ve parolosunu sorsun,admin ve paroloya 123456 yazılınca hoşgeldin desin
# tektar kullanıcı adı ve parola istesin
kullaniciadi=""
kullansifre=""
while kullaniciadi!="admin" or kullansifre!="123456":
    kullaniciadi=input("Kullanıcı adınız".lower())
    kullansifre = input("Kullanıcı şifreniz".lower())

    if kullaniciadi=="admin" and kullansifre=="123456":
          print("Hoşgeldiniz")
    else:
        print("Kullanıcıadı veya şifreniz hatalı")
print("Burdan devam eder")
