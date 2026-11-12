from ast import While
import sys

import KerjaDatabase


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
                            print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STATUS':<10}")
                            print("-"*88)
                            for Aidi, detail in barang_terurut:
                                harga = f"Rp {detail['Harga']:,.0f}".replace(",", ".")
                                status = "Aktif" if detail['Kondisi']==1 else "Nonaktif"
                                if role=="ADMIN":
                                    print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {status:<10}")
                                else:
                                    print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {'':<10}")
                            print("="*88+"\n")

                        elif metode == "3":
                            Sementara = KerjaDatabase.spilstok(role)
                            for kategori, IsiKategori in Sementara.items():
                                print(f"\n>> Kategori: {kategori.upper()}")
                                print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STATUS':<10}")
                                print("-"*88)
                                barang_terurut = KerjaDatabase.BucketSort(IsiKategori, descending=False)
                                for Aidi, detail in barang_terurut:
                                    harga = f"Rp {detail['Harga']:,.0f}".replace(",", ".")
                                    status = "Aktif" if detail['Kondisi']==1 else "Nonaktif"
                                    if role=="ADMIN":
                                        print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {status:<10}")
                                    else:
                                        print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {'':<10}")
                            print("\n"+"="*88)
                    case "2":
                        cekstok=KerjaDatabase.spilstok(role)
                        for Kategori, isikategori in cekstok.items():
                            print(f"\n>> Kategori: {Kategori.upper()}")
                            print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STOK MIN':>10} | {'STATUS':<10}")
                            print("-"*101)
                            for Aidi, detail in isikategori.items():
                                harga = f"Rp {detail['Harga']:,.0f}".replace(",", ".")
                                status = "Aktif" if detail['Kondisi']==1 else "Nonaktif"
                                if role=="ADMIN":
                                    print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {detail['Stok Minimum']:>10} | {status:<10}")
                                else:
                                    print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {detail['Stok Minimum']:>10} | {'':<10}")
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
                                            harga = f"Rp {detail['Harga']:,.0f}".replace(",", ".")
                                            print(f"\n{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16}")
                                            print("-"*75)
                                            print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16}")
                                            if role=="ADMIN":
                                                status = "Aktif" if detail['Kondisi']==1 else "Nonaktif"
                                                print(f"Status: {status}")

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
