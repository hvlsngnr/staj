while(True):#kullanici cikis yapmayana kadar girdigi her hatali dosya için tekrar dosya yolu soracak
 dosya_yolu=input("Cikis=0\nDosya yolunu  giriniz:")
 if(dosya_yolu[0]=="0"):
   print("Cikis yapiliyor...")
   break
 elif((dosya_yolu.find(":")!=-1) and (dosya_yolu.find("\\")!=-1)):
#girilen string ifadenin dosya yolu olup olmadigi kontrol ediliyor.
#Genel tum dosya yollarinda degismeyen sey,  dosya yolunun icinde ':' ve '\' barindirmasi
    try:
     kontrol="Girilen"
     file=open(dosya_yolu,"r",encoding="utf-8") 
    except: 
        print("Girilen dosya yolunda böyle bir dosya bulunmamaktadir.")
        kontrol="Olusturulan"
        file=open(dosya_yolu,"w+",encoding="utf-8")
        yazdir=input("Olusturulan dosyaya yazdirmak istediginiz metini giriniz:\n")
        file.write(yazdir)
        file.seek(0)#kullanici girdisi dosyaya yazdirildiktan sonra imlecin basa gelmesi saglaniyor.
                    #imlec basa gelmedigi taktirde okuma islemi basarisiz olacaktir.
    finally:
        print("{} dosyanin ilk iki bayti:{}".format(kontrol,file.read(2)))
        file.close()
        break
 else:
  print("Girmis oldugunuz dosya yolu hatali lütfen tekrar deneyiniz.")
input()