import os
import inquirer
import time
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Tampilan_Akun_Admin():
    os.system("cls")
    print("=" * 110)
    print("KELOLA AKUN".center(110))
    print('=' * 110)
    print(f'Username      : {Data["Username Admin"]}')
    print(f'Simpanan Uang : Rp{Data["Simpanan Uang Admin"]:,}'.replace("," , "X").replace("." , ",").replace("X" , "."))
    print("-" * 110)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Setup_Username_Baru_Admin():
    for i in Data["Data Akun"]:
        if Username_Baru == Data["Data Akun"][i]["Username"]:
            return "Username Sudah Ada"
    if not Username_Baru:
        return "Username Kosong"

def Setup_Password_Baru_Admin():
    if not Password_Baru:
        return "Password Kosong"

def Countdown():
    detik = 30
    while detik > 0:
        print(f"\rDemi keamanan, program dihentikan sementara. Silakan coba lagi dalam {detik:02d} detik", end="", flush=True)
        time.sleep(1)
        detik -= 1

def Pengaturan_Kelola_Akun():
    while True:
        Kesempatan = 3
        Tampilan_Akun_Admin()
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Kelola Akun", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Kelola Akun"]
        if Hasil_Opsi == "Ubah Username":
            Ganti_Username()
        elif Hasil_Opsi == "Ubah Password":
            Ganti_Password(Kesempatan)
        elif Hasil_Opsi == "Kembali":
            break

def Ganti_Username():
    global Username_Baru
    Tampilan_Akun_Admin()
    Username_Baru = input("Masukkan Username Baru : ").strip()
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan username ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    if jawaban is None:
        return
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        if Setup_Username_Baru_Admin() == "Username Sudah Ada":
            os.system("cls")
            print("=====Username sudah digunakan=====")
            time.sleep(1)
        elif Setup_Username_Baru_Admin() == "Username Kosong":
            os.system("cls")
            print("=====Input tidak boleh kosong=====")
            time.sleep(1)
        else:
            os.system("cls")
            Data["Username Admin"] = Username_Baru
            Simpan_Data()
            print("Username berhasil diganti!")
            print('--------------------------')
            input("Tekan Enter Untuk Kembali")
    elif Hasil_Opsi == "Tidak":
        pass
                
def Ganti_Password(Kesempatan):
    if Kesempatan == 0:
        Countdown()
    else:
        global Password_Baru
        Tampilan_Akun_Admin()
        Verifikasi_Password = input("Masukkan password akun anda sekarang terlebih dahulu untuk verifikasi: ").strip()
        if Verifikasi_Password == Data["Password Admin"]:
            Tampilan_Akun_Admin()
            Password_Baru = input("Masukkan Password Baru : ").strip()
            opsi = [
                inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                return
            Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
            if Hasil_Opsi == "Ya":
                if Setup_Password_Baru_Admin() == "Password Kosong":
                    os.system("cls")
                    print("=====Input tidak boleh kosong=====")
                    time.sleep(1)
                else:
                    os.system("cls")
                    Data["Password Admin"] = Password_Baru
                    Simpan_Data()
                    print("Password berhasil diganti!")
                    print('=' * 110)
                    input("Tekan Enter Untuk Kembali")
            elif Hasil_Opsi == "Tidak":
                pass
        else:
            os.system("cls")
            print("=====Password Salah=====")
            time.sleep(1)
            return Ganti_Password(Kesempatan - 1)