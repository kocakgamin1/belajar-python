tm = int(input("Masukan Nilai TM : "))
kehadiran = int(input("Masukan Nilai kehadiran : "))
uts = int(input("Masukan Nilai uts : "))
uas = int(input("Masukan Nilai uas : "))

nilai_akhir = (tm * 0.2) + (kehadiran * 0.1)+(uts * 0.3)+(uas * 0.4)
if nilai_akhir >= 70:
    print("Nilai Akhir Anda diatas 70 : ", nilai_akhir)
else:
    print("Nilai Akhir Anda dibawah 70 : ", nilai_akhir)