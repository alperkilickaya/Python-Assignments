age = input("75 Yaş ve Üzeri Sigara Bağımlısı mısınız? (Evet veya Hayır) ").strip().lower()  # can be assigned only True/False
chronic = input("Kronik Rahatsızlığınız Var mı? (Evet veya Hayır) ").strip().lower() # can be assigned only True/False
immune = input("Bağışıklık Sisteminiz Zayıf mı? (Evet veya Hayır) ").strip().lower()  # can be assigned only True/False

if ((age != "evet" and age != "hayır") or (chronic != "evet" and chronic != "hayır") or (immune != "evet" and immune != "hayır")):
  print("Lütfen İstenilen Formatta Cevap Veriniz.\n\"Evet\" veya \"Hayır\" Yazınız.") 
elif (age == "evet") and (chronic == "evet") and (immune == "evet"):
  print("Risk Grubundasınız!")
else:
  print("Risk Grubunda Değilsiniz")  