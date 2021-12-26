import os
# print(dir(os)) #kütüphane içerisinde kullanabileceğimiz metotların listesi
print(os.getcwd()) #dosyamızın bulunduğu yolu veriyor
os.chdir("C:/Users/egitim.sinif2/Desktop/Kali-Linux-2019.4-vmware-amd64") #yolu değiştirdim




print(os.getcwd())



#print(os.listdir()) # liste şeklinde olduguğum yerin dosyalarını verir



#os.mkdir("Deneme1") #deneme1 adında klasor olusturur














#os.makedirs("Deneme2/Deneme3")

#os.rmdir("Deneme2/Deneme3")

# os.rename("Deneme1","Deneme2")
# os.removedirs("Deneme2/Deneme3")

# os.rename("test.txt","test2.txt") derin ile burda kaldık

# print(datetime.fromtimestamp(os.stat("metin.txt").st_atime)) # tarih şeklinde getirmek için

# degistirilme = os.stat("test2.txt").st_mtime

# print(datetime.fromtimestamp(degistirilme))


# for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):
#     print("Current Path",klasör_yolu)
#     print("Directories",klasör_isimleri)
#     print("Dosyalar",dosya_isimleri)
#     print("**********************************")