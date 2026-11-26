import os
import inquirer

import time
from prettytable import PrettyTable
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Fitur_Unit(Nama_Penghuni, Kontak_Penghuni = "-"):
    os.system("cls")
    try:
        while True:
            os.system("cls")
            opsi = [
                inquirer.List("Opsi Pilih Fitur Unit", message="Pilih Opsi", choices=["Tampilkan Daftar Unit", "Unit Sewa Anda", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                time.sleep(1.0)
                break
            Hasil_Opsi = jawaban["Opsi Pilih Fitur Unit"]
            if Hasil_Opsi == "Tampilkan Daftar Unit":
                Daftar_Unit(Nama_Penghuni, Kontak_Penghuni)
            elif Hasil_Opsi == "Unit Sewa Anda":
                Unit_Sewa(Nama_Penghuni)
            elif Hasil_Opsi == "Kembali":
                return
    except KeyboardInterrupt:
        os.system("cls")
        return

def cek_ketersediaan_unit():
    list_kunci = []
    for keys, values in sorted(Data["Daftar Unit"].items()):
        if values["Status Unit"] != "Terisi":
            list_kunci.append(keys)
    return list_kunci

def cek_unit_penyewa(Nama_Penghuni):
    list_kunci = []
    for keys, values in sorted(Data["Daftar Unit"].items()):
        if values["Nama Penghuni"] == Nama_Penghuni:
            list_kunci.append(keys)
    if list_kunci is None:
        return None
    else:
        return list_kunci

def Lihat_Unit(kunci):
    try:
        os.system("cls")
        print("=" * 110)
        print("DAFTAR SELURUH UNIT YANG TERSEDIA".center(110))
        print("=" * 110)
        if len(Data["Daftar Unit"]) == 0 or kunci is None or len(kunci) <= 0:
            print("Tidak Ada Data Unit Di Dalam Daftar")
            print("-----------------------------------")
            input("Tekan 'Enter' untuk kembali")
            os.system("cls")
            return False
        else:
            tabelUnit = PrettyTable()
            tabelUnit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Nomor Kontak"]
                    
            for Nomor_Unit, dataUnit in sorted(Data["Daftar Unit"].items()):
                for isi in kunci:
                    if isi != Nomor_Unit:
                        continue
                    tabelUnit.add_row([Nomor_Unit,
                                        dataUnit['Tipe Unit'],
                                        dataUnit['Harga Unit'],
                                        dataUnit['Status Unit'],
                                        dataUnit['Nama Penghuni'],
                                        dataUnit['Nomor Kontak']
                                        ])
            print(tabelUnit)
        print()  
        print("=" * 89)
    except KeyboardInterrupt:
        os.system("cls")
        return False

def Daftar_Unit(Nama_Penghuni, Kontak_Penghuni):
    try:
        os.system("cls")
        # di sini tampilkan daftar unit
        opsi = [
            inquirer.List("Opsi Pilih Informasi Unit", message="Apakah Anda ingin melihat informasi unit?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            os.system("cls")
            return
        Hasil_Opsi = jawaban["Opsi Pilih Informasi Unit"]

        if Hasil_Opsi == "Tidak":
            os.system("cls")
            return
        os.system("cls")
        while True:
            if Lihat_Unit(cek_ketersediaan_unit()) == False:
                return
            try:
                print("Masukkan 0 Jika Ingin Kembali")
                print("-" * 110)
                Nomor_Unit = input("Masukkan Nomor Unit: ")
                if int(Nomor_Unit) == 0:
                    break
                elif not Nomor_Unit in Data["Daftar Unit"]:
                    os.system("cls")
                    print("Nomor Unit tersebut tidak tersedia!")
                    time.sleep(1.0)
                elif Nomor_Unit in Data["Daftar Unit"] and Data["Daftar Unit"][Nomor_Unit]["Status Unit"] != "Kosong":
                    os.system("cls")
                    print("Unit tersebut sudah disewa!")
                    time.sleep(1.0)
            except ValueError:
                os.system("cls")
                print("Harap masukkan nomor yang benar!")
                time.sleep(1.0)
            except KeyboardInterrupt:
                os.system("cls")
                return
            if Nomor_Unit in Data["Daftar Unit"]:
                os.system("cls")
                break
        if int(Nomor_Unit) == 0 or Nomor_Unit in Data["Daftar Unit"] and Data["Daftar Unit"][Nomor_Unit]["Status Unit"] != "Kosong":
            os.system("cls")
            return
                
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menyewa unit ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            time.sleep(1.0)
            os.system("cls")
            return
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Tidak":
            print("Aksi Dibatalkan")
            input("Tekan 'Enter' Untuk Kembali! ")
            os.system("cls")
            return
        os.system("cls")
        for nomorUnit, isi in sorted(Data["Daftar Unit"].items()):
            if nomorUnit == Nomor_Unit:
                isi["Nama Penghuni"] = Nama_Penghuni
                isi["Status Unit"] = "Terisi"
                isi["Nomor Kontak"] = str(Kontak_Penghuni)
                isi["Status Bayar Sewa"] = "Belum"

        # di sini program bayar sewa awal bagi penyewa
        Simpan_Data()
        print("Unit berhasil disewa")
        print('=' * 40)
        input("Tekan Enter Untuk Kembali")
        os.system("cls")
    except KeyboardInterrupt:
        os.system("cls")
        return
    except EOFError:
        os.system("cls")
        return


def Unit_Sewa(Nama_Penghuni):
    while True:
        try:
            os.system("cls")
            opsi = [
                inquirer.List("Opsi Pilih Unit Sewa", message="Pilih Opsi", choices=["Batalkan Sewa", "Kembali"])
            ]
            kunci = cek_unit_penyewa(Nama_Penghuni)
            if Lihat_Unit(kunci) == False:
                return
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                os.system("cls")
                return
            Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
            if Hasil_Opsi == "Kembali":
                os.system("cls")
                return
            Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
            if Hasil_Opsi == "Batalkan Sewa":
                os.system("cls")
                opsi = [
                    inquirer.List("Opsi Pilih Batalkan Sewa", message="Apakah Anda ingin membatalkan sewa unit ini?", choices=["Ya", "Tidak"])
                ]
            print("Masukkan '0' Jika Anda Ingin Kembali! ")
            print("Masukkan '1' Untuk Menampilkan Kembali List Unit Anda!")
            Nomor_Unit = input("Masukkan Nomor Unit: ")
            Unit_Penyewa_Ada = False
            for Unit_Penghuni in kunci:
                if Unit_Penghuni == Nomor_Unit:
                    Unit_Penyewa_Ada = True
                    break
            if int(Nomor_Unit) == 0:
                os.system("cls")
                return
            elif int(Nomor_Unit) == 1:
                continue
            elif Data["Daftar Unit"][str(Nomor_Unit)]["Status Bayar Sewa"] != "Sudah Bayar":
                print("Lunasi Uang Sewa Terlebih Dahulu!")
                time.sleep(1.0)
                continue
            elif Unit_Penyewa_Ada != True:
                raise EOFError
            break
        except ValueError:
            print ("Harap Masukkan Nomor Yang Valid!")
            time.sleep(1.0)
            os.system("cls")
        except EOFError:
            print("Unit dengan nomor tersebut tidak ada!")
            time.sleep(1.0)
        except KeyboardInterrupt:
            os.system("cls")
            return
            
    jawaban = inquirer.prompt(opsi)
    if jawaban is None:
        os.system("cls")
        return
    Hasil_Opsi = jawaban["Opsi Pilih Batalkan Sewa"]

    if Hasil_Opsi == "Ya":
        os.system("cls")
        for nomorUnit, isi in sorted(Data["Daftar Unit"].items()):
            if nomorUnit == Nomor_Unit:
                isi["Nama Penghuni"] = "-"
                isi["Status Unit"] = "Kosong"
                isi["Nomor Kontak"] = "-"
        Simpan_Data()
        print("Kontrak Sewa Dibatalkan!")
        print('=' * 110)
        input("Tekan Enter Untuk Kembali")
        os.system("cls")
    elif Hasil_Opsi == "Tidak":
        print("Aksi Dibatalkan")
        input("Tekan 'Enter' Untuk Kembali! ")
        os.system("cls")