import os
import inquirer
import time
import maskpass
import json

import Menu_Utama_Admin
import Menu_Utama_Penyewa

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Setup_Log_In_Admin():
    if Username_Log_In == Data["Username Admin"] and Password_Log_In == Data["Password Admin"]:
        return True

def Setup_Log_In_Penyewa():
    for i in Data["Data Akun"]:
        if Username_Log_In == Data["Data Akun"][i]["Username"] and Password_Log_In == Data["Data Akun"][i]["Password"]:
            return True

def Cari_Kontak_User():
    for i in Data["Data Akun"]:
        if Username_Log_In == Data["Data Akun"][i]["Username"] and Password_Log_In == Data["Data Akun"][i]["Password"]:
            return Data["Data Akun"][i]["No. Hp"]
    return "-"

def Countdown():
    detik = 30
    while detik > 0:
        print(f"\rDemi keamanan, program dihentikan sementara. Silakan coba lagi dalam {detik:02d} detik", end="", flush=True)
        time.sleep(1)
        detik -= 1

def Menu_Autentikasi():
    while True:
        Kesempatan = 3
        os.system("cls")
        print("=" * 120)
        print("     ▄▄                                                        ▄▄▄     ▄▄▄                                   \n"\
              "   ▄█▀▀█▄                     █▄                                ███▄ ▄███         █▄                               \n"\
              "   ██  ██               ▄    ▄██▄      ▄              ▄         ██ ▀█▀ ██         ██          ▄▄           ▄       \n"\
              "   ██▀▀██   ████▄ ▄▀▀█▄ ████▄ ██ ▄█▀█▄ ███▄███▄ ▄█▀█▄ ████▄     ██     ██   ▄▀▀█▄ ████▄ ▄▀▀█▄ ██ ▄█▀ ▄▀▀█▄ ███▄███▄\n"\
              " ▄ ██  ██   ██ ██ ▄█▀██ ██    ██ ██▄█▀ ██ ██ ██ ██▄█▀ ██ ██     ██     ██   ▄█▀██ ██ ██ ▄█▀██ ████   ▄█▀██ ██ ██ ██\n"\
              " ▀██▀  ▀█▄█▄████▀▄▀█▄██▄█▀   ▄██▄▀█▄▄▄▄██ ██ ▀█▄▀█▄▄▄▄██ ▀█   ▀██▀     ▀██▄▄▀█▄██▄██ ██▄▀█▄██▄██ ▀█▄▄▀█▄██▄██ ██ ▀█\n"\
              "            ██                                                                                                     \n"\
              "            ▀".center(120))
        print ("<||||[Selamat Datang di Apartemen Mahakam]||||>".center(120))
        print("=" * 120)
        opsi = [
            inquirer.List("Opsi Pilih Menu Autentikasi", message="Silakan melakukan autentikasi terlebih dahulu", choices=["Log In", "Sign In", "Keluar"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        Hasil_Opsi = jawaban["Opsi Pilih Menu Autentikasi"]
        if Hasil_Opsi == "Log In":
            Menu_Log_In(Kesempatan)
        elif Hasil_Opsi == "Sign In":
            Menu_Sign_In()
        elif Hasil_Opsi == "Keluar":
            break

def Menu_Log_In(Kesempatan):
    if Kesempatan == 0:
        Countdown()
    else:
        os.system("cls")
        global Username_Log_In, Password_Log_In
        print("=" * 110)
        print("LOG IN AKUN".center(110))
        print("=" * 110)
        print("Tekan Ctrl Kiri untuk Ubah Tampilan Password")
        print("-" * 110)
        Username_Log_In = input("Masukkan Username : ").strip()    
        print("Masukkan Password : ", end="")
        Password_Log_In = maskpass.advpass(prompt="", mask="*")
        print("-" * 110)
        opsi = [
            inquirer.List("Opsi Pilih Menu Log In", message="Apakah Anda ingin masuk?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        Hasil_Opsi = jawaban["Opsi Pilih Menu Log In"]
        if Hasil_Opsi == "Ya":
            if Setup_Log_In_Admin():
                os.system("cls")
                print("Login berhasil!")
                print("------------------------")
                input("Tekan Enter Untuk Lanjut")
                Menu_Utama_Admin.Menu_Utama_Admin()
            elif Setup_Log_In_Penyewa():
                Kontak_User = Cari_Kontak_User()
                os.system("cls")
                print("Login berhasil!")
                print("------------------------")
                input("Tekan Enter Untuk Lanjut")
                Menu_Utama_Penyewa.Menu_Utama_Penyewa(Username_Log_In, Kontak_User)
            else:
                os.system("cls")
                print("=====Login Gagal=====")
                time.sleep(1)
                return Menu_Log_In(Kesempatan - 1)
        elif Hasil_Opsi == "Tidak":
            pass

def Menu_Sign_In():
    os.system("cls")
    print("=" * 110)
    print("SIGN IN AKUN".center(110))
    print("=" * 110)
    Username_Sign_In = input("Masukkan Username : ").strip()    
    Password_Sign_In = input("Masukkan Password : ").strip()
    No_Hp = input("Masukkann Nomor Hp : ").strip()
    print("-" * 110)
    opsi = [
        inquirer.List("Opsi Pilih Menu Sign In", message="Simpan Akun?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    if jawaban is None:
        return
    Hasil_Opsi = jawaban["Opsi Pilih Menu Sign In"]
    if Hasil_Opsi == "Ya":
        for i in Data["Data Akun"]:
            if Username_Sign_In == Data["Data Akun"][i]["Username"] or Username_Sign_In == Data["Username Admin"]:
                os.system("cls")
                print("=====Username sudah digunakan=====")
                time.sleep(1)
                break
            elif not Username_Sign_In or not Password_Sign_In or not No_Hp:
                os.system("cls")
                print("=====Input tidak boleh kosong=====")
                time.sleep(1)
                break
            else:
                os.system("cls")
                ID_Baru = int(next(reversed(Data["Data Akun"]))) + 1
                Data["Data Akun"][ID_Baru] = {
                    "Username" : Username_Sign_In,
                    "Password" : Password_Sign_In,
                    "No. Hp" : No_Hp,
                    "Unit Sewa" : "-",
                    "Status Bayar Sewa" : "-"
                }
                Simpan_Data()
                print("Akun berhasil dibuat!")
                print("-------------------------")
                input("Tekan Enter Untuk Kembali")
                break
    elif Hasil_Opsi == "Tidak":
        pass