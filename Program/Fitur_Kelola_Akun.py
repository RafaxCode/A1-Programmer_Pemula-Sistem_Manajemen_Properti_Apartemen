import os
import inquirer
import time
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Tampilan_Akun_Penyewa(Username_Log_In):
    os.system("cls")
    print("=" * 110)
    print("KELOLA AKUN".center(110))
    print('=' * 110)
    for i in Data["Data Akun"]:
        if Username_Log_In == Data["Data Akun"][i]["Username"]:
            print(f'Username : {Data["Data Akun"][i]["Username"]}')
            print(f"No. Hp : {Data["Data Akun"][i]["No. Hp"]}")
            print(f"Unit Sewa : {Data["Data Akun"][i]["Unit Sewa"]}")
            print(f"Status Bayar Sewa : {Data["Data Akun"][i]["Status Bayar Sewa"]}")
            print(f"Pesan Pengingat : {Data["Data Akun"][i]["Pesan Pengingat"]}")
    print("-" * 110)

def Setup_Username_Baru_Penyewa():
    for i in Data["Data Akun"]:
        if Username_Baru == Data["Data Akun"][i]["Username"] or Username_Baru == Data["Username Admin"]:
            return "Username Sudah Ada"
    if not Username_Baru:
        return "Username Kosong"

def Setup_Password_Baru_Penyewa():
    if not Password_Baru:
        return "Password Kosong"

def Countdown():
    detik = 30
    while detik > 0:
        print(f"\rDemi keamanan, program dihentikan sementara. Silakan coba lagi dalam {detik:02d} detik", end="", flush=True)
        time.sleep(1)
        detik -= 1

def Fitur_Kelola_Akun(Username_Log_In):
    while True:
        Kesempatan = 3
        Tampilan_Akun_Penyewa(Username_Log_In) 
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Kelola Akun", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Kelola Akun"]
        if Hasil_Opsi == "Ubah Username":
            Ganti_Username(Username_Log_In)
        elif Hasil_Opsi == "Ubah Password":
            Ganti_Password(Username_Log_In, Kesempatan)
        elif Hasil_Opsi == "Kembali":
            break

def Ganti_Username(Username_Log_In):
    global Username_Baru
    Tampilan_Akun_Penyewa()
    Username_Baru = input("Masukkan Username Baru : ").strip()
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan username ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    if jawaban is None:
        return
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        if Setup_Username_Baru_Penyewa() == "Username Sudah Ada":
            os.system("cls")
            print("=====Username sudah digunakan=====")
            time.sleep(1)
        elif Setup_Username_Baru_Penyewa() == "Username Kosong":
            os.system("cls")
            print("=====Input tidak boleh kosong=====")
            time.sleep(1)
        else:
            os.system("cls")
            for i in Data["Data Akun"]:
                if Username_Log_In == Data["Data Akun"][i]["Username"]:
                    Data["Data Akun"][i]["Username"] = Username_Baru
                    Username_Log_In = Username_Baru
                    Simpan_Data()
                    print("Username berhasil diganti!")
                    print("--------------------------")
                    input("Tekan Enter Untuk Kembali")
    elif Hasil_Opsi == "Tidak":
        pass

def Ganti_Password(Username_Log_In, Kesempatan):
    if Kesempatan == 0:
        Countdown()
    else:
        global Password_Baru
        Tampilan_Akun_Penyewa
        Verifikasi_Password = input("Masukkan password akun anda sekarang : ").strip()
        for i in Data["Data Akun"]:
            if Username_Log_In == Data["Data Akun"][i]["Username"]:
                if Verifikasi_Password == Data["Data Akun"][i]["Password"]:
                    Password_Baru = input("Masukkan Password Baru : ").strip()
                    opsi = [
                        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    if jawaban is None:
                        return
                    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                    if Hasil_Opsi == "Ya":
                        if Setup_Password_Baru_Penyewa() == "Password Kosong":
                            os.system("cls")
                            print("=====Input tidak boleh kosong=====")
                            time.sleep(1)
                            break
                        else:
                            os.system("cls")
                            for i in Data["Data Akun"]:
                                if Username_Log_In == Data["Data Akun"][i]["Username"]:
                                    Data["Data Akun"][i]["Password"] = Password_Baru
                                    Simpan_Data()
                                    print("Password telah diganti")
                                    print("-------------------------")
                                    input("Tekan Enter Untuk Kembali")
                                    break
                    elif Hasil_Opsi == "Tidak":
                        pass
                else:
                    os.system("cls")
                    print("=====Password salah=====")
                    time.sleep(1)
                    return Ganti_Password(Username_Log_In, Kesempatan - 1)