diskon = 0.10
belanja = int(input("Masukan total belanja : "))
if belanja >= 100000:
    total_belanja = belanja - (belanja * diskon)
    print("Selamat anda mendapatkan diskon 10%")
    print("Total belanja anda adalah : ", total_belanja)
else:
    print("Maaf anda tidak mendapatkan diskon")
    print("Total belanja anda adalah : ", belanja)