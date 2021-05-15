def sayac(cumle):
  yeni_cumle = list(cumle.replace(' ',''))
  sayac = {} # boş dict oluşturdum
  for kelime in yeni_cumle: # her bir kelime
    if kelime in sayac.keys(): # eğer kelime dict'de varsa (ilkinde boş dict olduüu için value = 0 (integer))
      sayac[kelime] = sayac[kelime] + 1 # varsa dict'deki bu anahtarın value'sunu bir arttır. Value zaten integer
    else:
      sayac[kelime] = 1 # eğer kelime dict'de yoksa value'suna 1 (ineteger) ata.
  return sayac

cumle = input('Birşeyler yazınız: ').strip()

sayac(cumle)