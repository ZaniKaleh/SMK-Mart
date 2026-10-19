from ast import While
import sys

import KerjaDatabase


def MGudang():
    role="Pengelola Gudang"
    while True:
        print("\nMasukkan Username Gudang:\n")
        username=input()
        print("\nMasukkan Password Gudang:\n")
        password = input()
        validasiuser=KerjaDatabase.login(username,password,role)
        if validasiuser == True:
            Gudangnya(role)
        else:
            print("Username, Password, atau Role Anda tidak valid!")
def Gudangnya(role):
        while True:
                print("\n---------Selamat Datang di Bagian Gudang---------")
                print("Tugas Apa yang Ingin Dijalankan?")
                print("1= Data Barang")
                print("2= Edit Stok Barang")
                print("3= Tambahkan Barang Baru")
                print("4= Aktifkan atau Nonakifkan barang")
                print("0= Keluar Menu\n")
                tugas=input()
                match tugas:
                    case "1":
                        print("\nPilih metode pengurutan:")
                        print("1. Ascending  (Gabungan A - Z)")
                        print("2. Descending (Gabungan Z - A)")
                        print("3. Berdasarkan Kategori")
                        metode = input("Masukkan pilihan:\n")
                        if metode == "1" or metode == "2":
                            status_descending = True if metode == "2" else False
                            barang_terurut = KerjaDatabase.urutygy(role, descending=status_descending)
                            print("\n=== DAFTAR SELURUH BARANG SMK MART ===")
                            for Aidi, detail in barang_terurut:
                                print(f"[{Aidi}] {detail['Nama Barang']}")
                                print(f"      Stok  : {detail['Stok']}")
                                print(f"      Harga : Rp {detail['Harga']:,.0f}".replace(",", "."))
                                if role=="Admin":
                                    if detail['Kondisi']==1:
                                        print("      Status: Aktif")
                                    elif detail['Kondisi']==0:
                                        print("      Status: Nonaktif")
                            print("======================================\n")

                        elif metode == "3":
                            Sementara = KerjaDatabase.spilstok(role)
                            for kategori, IsiKategori in Sementara.items():
                                print(f"\n>> Kategori: {kategori.upper()}")
                                barang_terurut = KerjaDatabase.BucketSort(IsiKategori, descending=False)
                                for Aidi, detail in barang_terurut:
                                    print(f"[{Aidi}] {detail['Nama Barang']}")
                                    print(f"      Stok  : {detail['Stok']} pcs")
                                    print(f"      Harga : Rp {detail['Harga']:,.0f}".replace(",", "."))
                                    if role=="Admin":
                                        if detail['Kondisi']==1:
                                            print("      Status: Aktif")
                                        elif detail['Kondisi']==0:
                                            print("      Status: Nonaktif")
                            print("\n===========================")
                    case "2":
                        cekstok=KerjaDatabase.spilstok(role)
                        for Kategori, isikategori in cekstok.items():
                            print(f"\n>> Kategori: {Kategori.upper()}")
                            for Aidi, detail in isikategori.items():
                                print(f"\n[{Aidi}] {detail['Nama Barang']}")
                                print(f"      Stok  : {detail['Stok']}")
                                print(f"      Harga : Rp {detail['Harga']:,.0f}".replace(",", "."))
                                print(f"Stok Minimum: {detail['Stok Minimum']}")
                                if role=="Admin":
                                    if detail['Kondisi']==1:
                                        print("      Status: Aktif")
                                    if detail['Kondisi']==0:
                                        print("      Status: Nonaktif")
                        print("")
                        ubah=input("Masukkan ID barang yang ingin anda edit stoknya!\n").upper()
                        try:
                            stokbaru=int(input("Stoknya ingin anda ubah menjadi berapa?\n"))
                            validasistok=KerjaDatabase.editbarang(ubah, stokbaru)
                            if validasistok=="Berhasil":
                                print("Perubahan data berhasil!")
                                cekstok=KerjaDatabase.spilstok(role)
                                for _, isikategori in cekstok.items():
                                    for Aidi, detail in isikategori.items():
                                        if ubah==Aidi:
                                            print(f"\n[{Aidi}] {detail['Nama Barang']}")
                                            print(f"      Stok  : {detail['Stok']}")
                                            print(f"      Harga : Rp {detail['Harga']:,.0f}".replace(",", "."))
                                            if role=="Admin":
                                                if detail['Kondisi']==1:
                                                    print("      Status: Aktif")
                                                if detail['Kondisi']==0:
                                                    print("      Status: Nonaktif")

                            elif validasistok=="IDgagal":
                                print("ID stok yang anda masukkan tidak valid!!")
                            else:
                                print("Stok baru yang anda masukkan di bawah stok minimum!")
                        except ValueError:
                            print("Masukkan angka yang valid!")
                    case "3":
                        KerjaDatabase.nambahbarang()
                    case "4":
                        while True:
                            try:
                                opsi4=int(input("Ingin menghapus atau mengaktifkan barang?\n1= Hapus\n2= Aktifkan\n0= Keluar\n\n"))
                            except ValueError:
                                print("Masukkan angka")
                                continue
                            match opsi4:
                                case 1:
                                    KerjaDatabase.hapusbarang()
                                case 2:
                                    KerjaDatabase.diaktifkan()
                                case 0:
                                    break
                                case _:
                                    print("Masukkan antara angka 1, 2, atau 0!")
                    case "0":
                        sys.exit()
                    case _:
                        print("Input anda tidak valid!")
