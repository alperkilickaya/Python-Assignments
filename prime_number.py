a = input("Bir sayı giriniz:").strip()
a=int(a)
if a ==2:
  print(a, 'asal sayıdır.')
if a > 1:
   for i in range(2,a):
     if (a % i) == 0:
       print(a,"asal sayı değildir.")
       break
     else:
       print(a,"asal sayıdır.")
else:
  print(a,"asal sayı değildir.")