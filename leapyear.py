try:
  yil = int(input("Lütfen bir yıl giriniz: "))  
  if (yil % 4) == 0:  
   if (yil % 100) == 0:  
       if (yil % 400) == 0:  
           print("{0} artık yıldır.".format(yil))  
       else:  
           print("{0} artık yıl değildir.".format(yil))  
   else:  
       print("{0} artık yıldır.".format(yil))  
  else:  
   print("{0} artık yıl değildir.".format(yil))  
except:
  print('Lütfen sadece yıl giriniz.')