#Pesan untuk gw di masa depan, Ganti nama penerima soalnya yang ngakses admin bukan tenant
import os
import time
import inquirer

from Data import Data_Paket 

def susun_ulang_data_paket():
    list_paket = [Data_Paket[k] for k in sorted(Data_Paket)]
    Data_Paket.clear()
    for nomor, paket in enumerate(list_paket, start=1):
        Data_Paket[nomor] = paket

def Tampilkan_data_paket():
    size = len(Data_Paket)
    if size == 0:
        print ("Paket tidak ada!")
        return
    try:
        print ('=' * 55, "\n", ' ' * 20,
                "List Paket")
        #i = kunci, paket = DataPaket[i](kunci diksi dalam diksi)
        for i, paket in Data_Paket.items():
            print ("PAKET #", i, "\nNama Penerima    :", paket['Nama Penerima'],
                                 "\nNama Paket       :", paket['Nama Paket'],
                                 "\nStatus Paket     :", paket['Status Paket'])
    except KeyError:
        print ("Terjadi Kesalahan! Silahkan Coba Lagi!")
        return False
    return True

def Pengaturan_Penitipan_Paket():
    while True:
        Pilihan = [f"Paket #{i} " for i in Data_Paket]
        os.system("cls")
        if Tampilkan_data_paket() == False:
            Pilihan = ["Kembali"]
        else:
            Pilihan.append("Kembali")
            input ("Tekan 'Enter' untuk lanjut")
        
        opsi = [
                inquirer.List("Opsi Pilih Pengaturan Penitipan Paket", message="Pilih Opsi", choices=Pilihan)
            ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Pengaturan Penitipan Paket"]
        pilihan_paket = ""
        if jawaban == "Kembali":
            os.system("cls")
            break
        else:
            pilihan_paket = jawaban

        os.system("cls")

        #Ubah Status Paket
        opsi = [
            inquirer.List("Opsi Pilih Paket Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Paket Sampai"]

        kunci_data_paket = int(pilihan_paket[7:])
        #Status Paket diubah ke ya atau tidak
        if jawaban == "Ya":
            Data_Paket[kunci_data_paket]['Status Paket'] = "Sudah Sampai"
            print("Mengubah Status Paket...")
            time.sleep(1.5)
            os.system("cls")
            print("Status Paket Sukses Diganti!")
            input("Tekan 'Enter' Untuk Lanjut!")
        elif jawaban == "Tidak":
            Data_Paket[kunci_data_paket]['Status Paket'] = "Belum Sampai"
            print("Mengubah Status Paket...")
            time.sleep(1.5)
            os.system("cls")
            print("Status Paket Sukses Diganti!")
            input("Tekan 'Enter' Untuk Kembali!")
        os.system("cls")

        #Hapus Form Jika Paket sudah diterima
        opsi = [
            inquirer.List("Opsi Pilih Paket Diterima", message="Apakah paket sudah diterima?", choices=["Ya", "Tidak"])
            ]

        if jawaban == "Ya":
            jawaban = inquirer.prompt(opsi)
            jawaban = jawaban["Opsi Pilih Paket Diterima"]
            if jawaban == "Ya":
                print("Menghapus Form...")
                time.sleep(1.5)
                os.system("cls")
                # di sini program menghapus form penitipan paket
                del Data_Paket[kunci_data_paket]
                susun_ulang_data_paket()
                print("Form telah dihapus")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
            elif jawaban == "Tidak":
                print("Silahkan Menunggu Kedatangan Paket Anda!")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
    # else tidak ada paket
    print('=' * 40)
    os.system("cls")