#Menginput nama dan nilai 
nama =input("Masukan Nama : ")
Tugas_Harian1 = float(input("Masukkan Nilai Harian1 : "))
Tugas_Harian2 = float(input("Masukkan Nilai Harian2 : "))
UTS =float(input("Masukan Nilai UTS: "))
UAS =float(input("Masukan Nilai UAS: "))

R_Tugas_Harian1 = int(Tugas_Harian1 * 15/100)
R_Tugas_Harian2 = int(Tugas_Harian2 * 15/100)
R_UTS=int(UTS* 30/100)
R_UAS=int(UAS* 40/100)

#Mengitung Nilai Akhir
Nilai_Akhir= R_Tugas_Harian1 + R_Tugas_Harian2 + R_UTS + R_UAS

#Menampilkan Nama dan Nilai
print ("nama: "+nama)
print ("Nilai Akhir: ",int(Nilai_Akhir))

if Nilai_Akhir >= 80 and Nilai_Akhir < 100:
    print("Grade : A")
elif Nilai_Akhir >= 60 and Nilai_Akhir < 80:
    print("Grade : B")
elif Nilai_Akhir >= 40 and Nilai_Akhir < 60:
    print("Grade : C")
elif Nilai_Akhir >= 20 and Nilai_Akhir < 40:
    print("Grade : D")
elif Nilai_Akhir >= 0 and Nilai_Akhir < 20:
    print("Grade : E")

if Nilai_Akhir >=60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")