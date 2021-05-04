fibo =[1,1]

while True:
   fibo.append(int(fibo[-1]) + int(fibo[-2]))
   if fibo[-1] == 55:
     break
print(fibo)