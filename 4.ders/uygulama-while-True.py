#isim yerine q girilince dursun,aksi takdirde sürekli isim istesin!
isim=""
isimler=[]
while True:

    isim=input("İsim Giriniz")
    if isim=="q":
        break
    isimler.append(isim)
print(isimler)

