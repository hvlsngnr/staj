dosya_yolu=input("Dosya yolunu  giriniz: ")
try:
 with open(dosya_yolu,"r",encoding="utf-8") as file:
  aranacak_kelime=input("Aramak istediginiz kelimeyi giriniz: ")
  ofset=file.read().find(aranacak_kelime)#.find() metotu aranan kelimeyi bulursa ofset degerini verir eğer bulamazsa -1 döndürür
 if(ofset!=-1):#eger ofset -1'e esit degilse aranan kelime dosyada mevcuttur
  print(""""{}" ifadesi {} adresinde bulundu """.format(aranacak_kelime,ofset))
 else:
  print(""""{}" ifadesi herhangi bir konumda bulunamadi""".format(aranacak_kelime))
except FileNotFoundError:# dosya bulunamadi hatasi almak yerine dosya yolu yanlis girildiğinde veya dosya bulunamadiginda
 dosya_adi=""
 for x in dosya_yolu.split('\\'): #dosya ismini almak icin girilen dosya yolunu backslashlar ayirip sondaki backslashtan
  dosya_adi=x                     #sonra gelen dosya ismi olacagi için dosya_adi'na atadim
 print("Girilen Dosya yolu yanlis veya \"{}\" dosyasi bulunamadi.".format(dosya_adi))
input()