def fizbuz(a):
  if a%3==0 and a%5==0:
    print("fizzbuzz")
  elif a %5==0:
    print("buzz")
  elif a %3==0:
    print("fizz")
  else:
    print(a)
while True:
  a=(input("please, enter a number:")) 
  if a.isdigit():
    fizbuz(int(a))
  else:
    print("numerik sistemde girin")