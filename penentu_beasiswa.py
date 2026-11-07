ipk = int(input("Masukan IPK anda : "))
penghasilan = int(input("Masukan penghasilan orang tua anda : "))
if ipk >= 3.5 and penghasilan <= 2000000:
    print("Selamat anda mendapatkan beasiswa Reguler")
elif ipk >= 3.5 and penghasilan > 2000000:
    print("Selamat anda mendapatkan beasiswa Non Reguler")
else:
    print("Maaf anda tidak mendapatkan beasiswa")