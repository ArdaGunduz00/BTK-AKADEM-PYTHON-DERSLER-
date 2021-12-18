'''
Girilen bir sayınn asal olup olmadığını bulunuz.
'''

sayii = int(input('sayi: '))
asallmi = True
if sayi == 1:
	asallmi = False
for i in range(2,sayi):
	if (sayi% i == 0):
		asallmi = False
		break

if asallmi:
	print('sayi asaldir')
else:
	print('sayi asal değildir')
