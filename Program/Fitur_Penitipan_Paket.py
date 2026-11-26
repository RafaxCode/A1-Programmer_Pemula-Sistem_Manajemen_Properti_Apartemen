import os
import inquirer
import time
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def cek_spesial(huruf):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in huruf):
        return True
    else:
        return False
    # Response: yes

def susun_ulang_data_paket():
    list_paket = [Data["Data Paket"][k] for k in sorted(Data["Data Paket"])]
    Data["Data Paket"].clear()
    for nomor, paket in enumerate(list_paket, start=1):
        Data["Data Paket"][nomor] = paket

def Tampilkan_data_paket(Nama_User):
    global paket_personal_ada
    os.system("cls")
    paket_personal_ada = False
    print ('=' * 60)
    print("List Paket".center(60))
    personal_paket_count = 0
    for i, paket in Data["Data Paket"].items():
        if Nama_User == paket['Nama Penerima']:
            paket_personal_ada = True
            personal_paket_count += 1
            print("PAKET #", personal_paket_count, 
                    "\nNama Penerima    :", paket['Nama Penerima'],
                    "\nNama Paket       :", paket['Nama Paket'],
                    "\nStatus Paket     :", paket['Status Paket'])
            print()
    if not paket_personal_ada:
        print("Saat ini, anda tidak sedang menitipkan paket!".center(60))

def Fitur_Penitipan_Paket(Nama_User):
    while True:
        os.system("cls")
        print("=" * 110)
        print("PENITIPAN PAKET".center(110))
        print("=" * 110)
        opsi = [
            inquirer.List("Opsi Pilih Fitur Penitipan Paket", message="Pilih Opsi", choices=["Buat Form", "Status Paket", "Hapus Form", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Fitur Penitipan Paket"]
        if jawaban == "Buat Form":
            Buat_Form(Nama_User)
        elif jawaban == "Status Paket":
            Status_Paket(Nama_User)
        elif jawaban == "Hapus Form":
            Hapus_Form(Nama_User)
        elif jawaban == "Kembali":
            break

def Buat_Form(Nama_User):
    os.system("cls")
    print("=" * 110)
    print("MEMBUAT FORM".center(110))
    print("=" * 110)
    nama_paket = input("Masukkan Nama Paket: ")
    if nama_paket is None:
        os.system("cls")
        print ("=====Nama Paket Tidak Boleh Kosong!=====")
        time.sleep(1)
    elif cek_spesial(nama_paket):
        os.system("cls")
        print("Nama Paket Tidak Boleh Selain Huruf Atau Angka!")
        time.sleep(1)

    temporary_paket = {"Nama Penerima" : Nama_User,
                    "Nama Paket"    : nama_paket,
                    "Status Paket"  : "Belum Sampai"}

    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin membuat form dengan nama ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        os.system("cls")
        Data["Data Paket"][f"{len(Data["Data Paket"]) + 1}"] = temporary_paket
        Simpan_Data()
        print("Form telah dibuat")
        print('-------------------------')
        input('Tekan Enter Untuk Kembali') 
    elif jawaban == "Tidak":
        pass


def Status_Paket(Nama_User):
    Tampilkan_data_paket(Nama_User)
    print('=' * 60)
    input('Tekan Enter Untuk Kembali')

def Hapus_Form(Nama_User):
    Tampilkan_data_paket(Nama_User)
    if not paket_personal_ada:
        print('=' * 60)
        input('Tekan Enter Untuk Kembali')
    else:
        print ("=" * 60)
        list_paket_user = []
        count = 0
        for value in Data["Data Paket"]:
            if Data["Data Paket"][value]["Nama Penerima"] == Nama_User:
                count += 1
                list_paket_user.append(f"Paket # {count}")
        list_paket_user.append("Batal")
        count = 0
                
        opsi = [
            inquirer.List("Opsi Paket Yang Ingin Dihapus", message="Pilih Form Paket Yang Ingin Dihapus", choices=list_paket_user)
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        jawaban = jawaban["Opsi Paket Yang Ingin Dihapus"]
        kunci_data_paket = int(jawaban[7:])
        if jawaban == "Batal":
            pass
        else:
            Tampilkan_data_paket(Nama_User)
            print ("=" * 60)
            opsi = [
                inquirer.List("Konfirmasi Penghapusan", message="Apakah Anda Yakin Ingin Menghapus Form Ini?", choices=["Iya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                return
            Hasil_Opsi = jawaban["Konfirmasi Penghapusan"]
            if Hasil_Opsi == "Iya":
                os.system("cls")
                print("Menghapus Form...")
                del Data["Data Paket"][str(kunci_data_paket)]
                susun_ulang_data_paket()
                Simpan_Data()
                time.sleep(1.5)
                os.system("cls")
                print("Form Telah Dihapus")
                print("-------------------------")
                input('Tekan Enter Untuk Kembali')
                Simpan_Data()
                return True
            elif Hasil_Opsi == "Tidak":
                return False