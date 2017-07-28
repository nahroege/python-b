class Kurs:
  adi = ""
  vantilator = 0

  def araVer(self):
    print(self.adi+" sınıfı ara veriyor")

  def vantilatorLazimMi(self):
    return self.vantilator < 2

php = Kurs()
php.adi = "PHP"
php.araVer()
php.vantilator = 10
python = Kurs()
python.adi = "Python"
python.araVer()

while python.vantilatorLazimMi():
  print(str(python.vantilator)+" yetmez "+str(python.vantilator+1)+" olsun")
  python.vantilator += 1

