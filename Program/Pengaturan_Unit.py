import os
import inquirer
import time
import Data
from prettytable import PrettyTable

def Pengaturan_Unit():
    Go_Back_Pengaturan_Unit = False
    while not Go_Back_Pengaturan_Unit:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Unit", message="Pilih Opsi", choices=["Daftar Unit", "Tambah Unit", "Status Unit", "Hapus Unit", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Pilihan_Menu = jawaban["Opsi Pilih Pengaturan Unit"]
        if Pilihan_Menu == "Daftar Unit":
            Lihat_Unit()
        elif Pilihan_Menu == "Tambah Unit":
            Tambah_Unit()
        elif Pilihan_Menu == "Status Unit":
            Status_Unit()
        elif Pilihan_Menu == "Hapus Unit":
            Hapus_Unit()
        elif Pilihan_Menu == "Kembali":
            Go_Back_Pengaturan_Unit = True

def Lihat_Unit():
    os.system("cls")
    print("=========================================================================================")
    print("                                   DAFTAR SELURUH UNIT                                   ")
    print("=========================================================================================")
    if len(Data.Daftar_Unit) == 0:
        print("Belum Ada Data Unit Di Dalam Daftar")
        print()
    else:
        tabelUnit = PrettyTable()
        tabelUnit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Nomor Kontak"]
                
        for Nomor_Unit, dataUnit in Data.Daftar_Unit.items():
            tabelUnit.add_row([Nomor_Unit,
                                dataUnit['Tipe Unit'],
                                dataUnit['Harga Unit'],
                                dataUnit['Status Unit'],
                                dataUnit['Nama Penghuni'],
                                dataUnit['Nomor Kontak']
                                ])
        print(tabelUnit)
    print()  
    print('=' * 40)
    kembali = input('Tekan Enter Untuk Kembali')

def Tambah_Unit():
    os.system("cls")
    print("=========================================================================================")
    print("                                   MENAMBAHKAN UNIT                                      ")
    print("=========================================================================================")
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menambahkan unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        while True:
            os.system("cls")
            print("=========================================================================================")
            print("                                   MENAMBAHKAN UNIT                                      ")
            print("=========================================================================================")
            print("Contoh Format Nomor Unit : 315")
            print("3 untuk Lantai dan 15 untuk Nomor Kamar")
            print("Lantai : Min. 1 dan Max. 5")
            print("Nomor Kamar : Min. 1 dan Max. 15")
            try:
                Nomor_Unit = int(input("Masukkan Nomor Unit: "))
            except ValueError:
                os.system("cls")
                print("Harap Masukkan Nomor Yang Valid")
                time.sleep(1)
                continue
            if Nomor_Unit <= 0:
                os.system("cls")
                print("Harap Masukkan Nomor Yang Valid")
                time.sleep(1)
                continue
            else:
                Lantai = Nomor_Unit // 100
                Nomor_Kamar = Nomor_Unit % 100
                if Lantai < 1 or Lantai > 5 or Nomor_Kamar < 1 or Nomor_Kamar > 15:
                    os.system("cls")
                    print("Lantai atau Nomor Kamar Tidak Sesuai Ketentuan!")
                    time.sleep(1)
                    continue
                elif Nomor_Unit in Data.Daftar_Unit:
                    os.system("cls")
                    print("Nomor Tersebut Telah Ada Di Dalam Daftar")
                    time.sleep(1)
                    continue
                else:
                    opsi = [
                        inquirer.List("Pilihan Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Ingin Ditambahkan", choices=["Kecil", "Besar"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi = jawaban["Pilihan Tipe Unit"]
                    if Hasil_Opsi == "Kecil":
                        Tipe_Unit = "Kecil"
                        Harga_Unit = 1000000
                    else:
                        Tipe_Unit = "Besar"
                        Harga_Unit = 2000000

                    Unit_Baru = {
                        'Tipe Unit': Tipe_Unit,
                        'Harga Unit': Harga_Unit,
                        'Status Unit': "Kosong",
                        'Nama Penghuni': "-",
                        'Nomor Kontak': "-"
                    } 
                    Data.Daftar_Unit[Nomor_Unit] = Unit_Baru
                    print("Berhasil!, Unit No", Nomor_Unit, "Telah Ditambahkan")
                    print('=' * 40)
                    kembali = input('Tekan Enter Untuk Kembali')
                    break 
    elif Hasil_Opsi == "Tidak":
        pass

def Status_Unit():
    while True:
        os.system("cls")
        print("=========================================================================================")
        print("                                  MENGUBAH STATUS UNIT                                   ")
        print("=========================================================================================")
        if len(Data.Daftar_Unit) == 0:
            print("Belum Ada Data Unit Di Dalam Daftar")
            print()  
            print('=' * 40)
            input('Tekan Enter Untuk Kembali')
            break
        else:
            opsi = [
                inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengubah status Unit?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
            if Hasil_Opsi == "Ya":
                while True:
                    os.system("cls")
                    try:
                        Nomor_Tujuan = int(input("Masukkan Nomor Unit Yang Ingin Diubah: "))
                    except ValueError:
                        print("Harap Masukkan Nomor Unit Yang Valid!")
                        time.sleep(2)
                        continue
                    if Nomor_Tujuan <= 0:
                        os.system("cls")
                        print("Harap Masukkan Nomor Unit Yang Valid")
                        time.sleep(2)
                        continue
                    if Nomor_Tujuan in Data.Daftar_Unit:
                        os.system("cls")
                        Unit = Data.Daftar_Unit[Nomor_Tujuan]
                        if Unit['Status Unit'] == "Terisi":
                            print("Unit No", Nomor_Tujuan, "Saat Ini Diisi Oleh", Unit['Nama Penghuni'])
                            opsi = [
                                inquirer.List("Pilihan1", message="Apakah Anda Ingin Mengosongkan Unit Ini?", choices=["Ya", "Tidak"])
                            ]
                            jawaban = inquirer.prompt(opsi)
                            Hasil_Opsi = jawaban["Pilihan1"]
                            if Hasil_Opsi == "Ya":
                                Unit['Status Unit'] = "Kosong"
                                Unit['Nama Penghuni'] = "-"
                                Unit['Nomor Kontak'] = "-"
                                print("Berhasil!, Unit No", Nomor_Tujuan, "Telah Dikosongkan")
                                time.sleep(2)
                                break

                            else:
                                break
                        else:
                            os.system("cls")
                            print("Unit No", Nomor_Tujuan, "Saat Ini Kosong")
                            opsi = [
                                inquirer.List("Pilihan2", message="Apakah Anda Ingin Mengisi Unit Ini?", choices=["Ya", "Tidak"])
                            ]
                            jawaban = inquirer.prompt(opsi)
                            Hasil_Opsi = jawaban["Pilihan2"]
                            if Hasil_Opsi == "Ya":
                                Nama_Penghuni = input("Masukkan Nama Penghuni: ")
                                Nomor_Kontak = input("Masukkan Kontak Penghuni: ")
                                Unit['Status Unit'] = "Terisi"
                                Unit['Nama Penghuni'] = Nama_Penghuni
                                Unit['Nomor Kontak'] = Nomor_Kontak
                                print("Berhasil!, Unit No", Nomor_Tujuan, "Telah Diisi Oleh", Unit['Nama Penghuni'])
                                time.sleep(1)
                                break
                            else: 
                                break
                    else:
                        print("Nomor Tersebut Tidak Ditemukan Di Dalam Daftar")
                        time.sleep(2)
                        break
            else:
                break
        

    
def Hapus_Unit():
    os.system("cls")
    print("=========================================================================================")
    print("                                      MENGHAPUS UNIT                                     ")
    print("=========================================================================================")
    if len(Data.Daftar_Unit) == 0:
        print("Belum Ada Data Unit Di Dalam Daftar")
        print()  
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')
    else:
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menghapus unit?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Ya":
            while True:
                try:
                    Nomor_Hapus = int(input("Masukkan Nomor Unit Yang Ingin Dihapus: "))
                except ValueError:
                    os.system("cls")
                    print("Harap Masukkan Nomor Yang Valid")
                    time.sleep(1)
                    continue
                if Nomor_Hapus <= 0:
                    os.system("cls")
                    print("Harap Masukkan Nomor Yang Valid")
                    time.sleep(1)
                    continue
                if Nomor_Hapus in Data.Daftar_Unit:
                    Unit = Data.Daftar_Unit[Nomor_Hapus]
                    if Unit['Status Unit'] == "Terisi":
                        os.system("cls")
                        print("Harap Kosongkan Kamar Terlebih Dahulu!")
                        time.sleep(2)
                        break
                    else:
                        opsi = [
                            inquirer.List("pilihan", message="Apakah Anda Ingin Menghapus Unit ini?", choices=["Ya", "Tidak"])
                        ]
                        jawaban = inquirer.prompt(opsi)
                        Hasil_Opsi = jawaban["pilihan"]
                        if Hasil_Opsi == "Ya":
                            del Data.Daftar_Unit[Nomor_Hapus]
                            print("Berhasil!, Unit No", Nomor_Hapus, "Telah Dihapus Dari Daftar")
                            time.sleep(2)
                            break
                        else:
                            break
                else:
                    os.system("cls")
                    print("Nomor Tersebut Tidak Ditemukan Di Dalam Daftar")
                    time.sleep(2)
                    break
        else:
            pass