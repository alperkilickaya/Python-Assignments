fibo =[1,1]

while True:
   fibo.append((fibo[-1]) + (fibo[-2]))
   if fibo[-1] == 55:
     break
print(fibo)