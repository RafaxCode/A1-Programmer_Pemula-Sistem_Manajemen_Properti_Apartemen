import os
import time
from prettytable import PrettyTable
import json

def Baca_Data():
    global Data
    with open("Program/Data.json", "r") as file:
        Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Pengaturan_Pembayaran_Sewa():
    while True:
        Baca_Data()
        os.system("cls")
        print("=" * 110)
        print("PENGATURAN PEMBAYARAN SEWA".center(110))
        print("=" * 110)

        tabelUnit = PrettyTable()
        tabelUnit.field_names = ["Nomor Unit", "Nama Penghuni", "Nomor Kontak", "Harga Unit", "Status Pembayaran"]
        for Nomor_Unit in sorted(Data["Daftar Unit"]):
            dataUnit = Data["Daftar Unit"][Nomor_Unit]
            if dataUnit['Status Unit'] == "Terisi":
                tabelUnit.add_row([Nomor_Unit,
                                   dataUnit['Nama Penghuni'],
                                   dataUnit['Nomor Kontak'],
                                   dataUnit['Harga Unit'],
                                   dataUnit['Status Bayar Sewa']
                                   ])
        tabelUnit.hrules = 1
        print(tabelUnit)
        print("Masukkan 0 Untuk Kembali")
        try:
            Nomor_Unit = int(input("Masukkan Nomor Unit Penyewa: "))
        except ValueError:
            os.system("cls")
            print("=====Harap Masukkan Nomor Yang Valid=====")
            time.sleep(1)
            continue
        if Nomor_Unit == 0:
            break
        if str(Nomor_Unit) not in Data["Daftar Unit"]:
            os.system("cls")
            print("Nomor Unit Tidak Ada Di Dalam Daftar")
            time.sleep(1)
            continue
        elif Data["Daftar Unit"][str(Nomor_Unit)]['Status Unit'] != "Terisi":
            os.system("cls")
            print("Unit Tersebut Tidak Memiliki Penyewa")
            time.sleep(1)
            continue
        else:
            os.system("cls")
            print("=" * 110)
            print("PENGATURAN PEMBAYARAN SEWA".center(110))
            print("=" * 110)
            dataUnit = Data["Daftar Unit"][str(Nomor_Unit)]
            print("Nomor Unit        :", Nomor_Unit)
            print("Tipe Unit         :", dataUnit['Tipe Unit'])
            print("Harga Unit        :", dataUnit['Harga Unit'])
            print("Nama Penghuni     :", dataUnit['Nama Penghuni'])
            print("Nomor Kontak      :", dataUnit['Nomor Kontak'])
            print("Status Pembayaran :", dataUnit["Status Bayar Sewa"])
            print("----------------------------------------------------------")
            input("Tekan Enter Untuk Kembali")
            break