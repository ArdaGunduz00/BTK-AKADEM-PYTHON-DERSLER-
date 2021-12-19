#kullanıcıya adını sorsun,admin yazılınca hoşgeldin desin. Admin yazılmadığı sürece
# tekrar kullanıcı adı istesin(sürekli)
isim=""# While şartında kullanabilmek için tanımlamak zorundayım

while isim!="admin":
    isim=input("Kullanıcı adınız").lower()
    if isim=="admin":
          print("Hoşgeldiniz")
print("Burdan devam eder")                                                                         








