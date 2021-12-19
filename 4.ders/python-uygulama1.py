#klavyeden q harfi igirilne kadar girilen sayıları listeye atıcaksınız,en son
# q girildiğinde listeyi ekrana yazdıran kod
sayılar=[]
girilensayi=""
while girilensayi!="q":
    girilensayi=input("Sayı giriniz")
    if girilensayi!= "q":
       if girilensayi!="":
           try:
            sayılar.append(int(girilensayi))
           except ValueError:
               print("Sadece sayı girmelisiniz")

print(sayılar)
