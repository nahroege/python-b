import os
dizin=input("Hangi dizin silincek")
dosyalar=os.listdir(dizin)
for dosya in dosyalar:
	os.remove(dizin+"/"+dosya)
os.rmdir(dizin)
