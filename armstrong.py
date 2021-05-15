
a = input("Bir sayı giriniz: ").strip()
if a.isdigit():
  rakam = int(a)
  liste = list(str(a))
  basamak = len(liste)
  toplam = 0
  for i in liste:
    toplam = toplam + (pow(int(i),basamak))
  if toplam==rakam:
    print(a, "sayısı Armstrong sayıdır.")
  else:
    print(a, "sayısı Armstrong sayı DEĞİLDİR.")
else:
 print ("lütfen uygun formatta giriniz!!")

