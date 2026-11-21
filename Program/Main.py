import os
import inquirer

import Autentikasi
#fungsi dengan parameter (bukan prosedur) blum ada
#Bikin tampilkan data/sembarang pake fungsi rekursif
#Finally dan raise try sama else tidak ada


Go_Out = False
while not Go_Out:
    Autentikasi.Menu_Autentikasi()
    os.system("cls")
    opsi = [
        inquirer.List("Opsi Pilih Keluar", message="Apakah Anda ingin keluar?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Keluar"]
    if Hasil_Opsi == "Ya":
        Go_Out = True
    elif Hasil_Opsi == "Tidak":
        pass
    