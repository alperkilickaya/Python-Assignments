password = "alper12345" #  sabit olan şifres
name = ('Alper', 'alper', 'ALPER') # Kendi ismim. Büyük ve küçük harf kullanılabileceği için tuple kullandım. Tuple kullanarak değişmez yaptım.
enter_name = input("İsminizi Giriniz: ") # Kullanıcı tarafından girilen isim.

if enter_name in name: # Girdiğim isim daha önce name değişkeninde sakladığım herhangi bir isme eşit ise.
  print("Hoş Geldin {}. Şifreniz:\033[1m '{}' \033[1m.".format(enter_name, password)) # \033[1m kullanımı BOLD olmasını sağlıyor.
else:
  print("Hoş Geldin {}. İyi Günler Dileriz".format(enter_name)) # \033[1m kullanımı BOLD olmasını sağlıyor.