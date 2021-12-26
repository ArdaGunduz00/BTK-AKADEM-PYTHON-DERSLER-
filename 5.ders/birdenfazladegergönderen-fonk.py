"""
kendisine gönderilen tüm değerleri toplayıp ekrana basan fonksiyon 3 tane de gönderilebeilir,5tanede,10tanede
"""
def topla(*degerler):#Gönderilen tüm değerler sayılar adında bir demete(tuple) atandı
    toplam=0
    for i in degerler:
        toplam+=i # toplam=toplam+i
    print(toplam)
topla(10,2,15,15,15,15,)