angka_rahasia = 7
while True:
    tebakan = int(input("Tebak angka rahasia (1-10): "))
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan Anda benar.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakan Anda salah. Coba lagi. Angka rahasia lebih besar.")
    elif tebakan > angka_rahasia:
        print("Tebakan Anda salah. Coba lagi. Angka rahasia lebih kecil.")