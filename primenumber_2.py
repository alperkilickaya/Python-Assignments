n = int(input("Bir sayı giriniz: ").strip())
prime_list=[]
for i in range (1,n):
  if i>1:
    for j in range (2,i):
      if i % j == 0:
         break
    else:
      prime_list.append(i)    
print(prime_list)