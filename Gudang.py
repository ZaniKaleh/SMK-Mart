from ast import While
from copyreg import dispatch_table
import Main
import sys

import KerjaDatabase


def Gudangnya(username, role):
    from Admin import punyaadmin
    while True:
                print("\n---------Selamat Datang di Bagian Gudang---------")
                print("Tugas Apa yang Ingin Dijalankan?")
                print("1= Data Barang")
                print("2= Kelola Barang")
                print("3= Tambahkan Barang Baru")
                print("4= Pulihkan atau Hapus barang")
                print("999= Kembali ke Login")
                print("0= Keluar Menu\n")
                if role=="ADMIN":
                    print("000= Kembali ke Menu Admin")
                tugas=input()
                match tugas:
                    case "1":
                        while True:
                            print("\nPilih metode pengurutan:")
                            print("1. Ascending  (Gabungan A - Z)")
                            print("2. Descending (Gabungan Z - A)")
                            print("3. Berdasarkan Kategori")
                            print("4. Kembali")
                            metode = input("Masukkan pilihan:\n").strip()
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
                            elif metode=="4":
                                break
                            else:
                                print("Masukkan input yang valid!")
                    case "2":
                        while True:
                            pilih2=input("1= Edit Harga informasi barang (Edit nama barang/Harga Jual/Stok minimum)\n2= Restock barang\n3= Kurangi/Hapus barang\n0= Kembali\n\n")
                            match pilih2:
                                case "1":
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
                                    print()
                                    ubah=input("Masukkan ID barang yang ingin Anda edit!\n").upper().strip()
                                    while not ubah.isalnum():
                                        ubah=input("Hanya masukkan huruf dan angka!\n").upper().strip()
                                    try:
                                        namabaru=input("Ubah nama barang menjadi apa? (0 untuk lewati)\n").strip()
                                        while "|" in namabaru:
                                            namabaru=input("Tidak boleh terdapat '|' pada nama barang!\n")
                                        hargabaru=input("Ubah harga jual menjadi berapa? (0 untuk lewati)\n")
                                        while not hargabaru.isdigit():
                                            hargabaru=input("Hanya masukkan angka yang valid!")
                                        hargabaru=int(hargabaru)
                                        minimbaru=input("Ubah stok minimum menjadi berapa? (0 untuk lewati)\n")
                                        while not minimbaru.isdigit():
                                            minimbaru=input("Hanya masukkan angka yang valid!")
                                        minimbaru=int(minimbaru)
                                        validasistok=KerjaDatabase.editbarang(ubah, namabaru,hargabaru,minimbaru)
                                        if validasistok=="Berubah":
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
                                        elif validasistok=="NoPerubahan":
                                            print("Tidak ada perubahan yang dilakukan!")
                                        elif validasistok=="Belum":
                                            print("ID stok yang anda masukkan tidak valid!!")
                                    except ValueError:
                                        print("Masukkan angka yang valid!")
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
                                    print()
                                    ubah=input("Masukkan ID barang yang ingin Anda restock!\n").upper().strip()
                                    while not ubah.isalnum():
                                        ubah=input("Hanya masukkan huruf dan angka!\n").upper().strip()
                                    ditambah=input("Stoknya ingin ditambah berapa?\n")
                                    while not ditambah.isdigit():
                                        ditambah=input("Hanya masukkan angka bulat!\n")
                                    ditambah=int(ditambah)
                                    hasilrestok=KerjaDatabase.restokbarang(ubah, ditambah)
                                    match hasilrestok:
                                        case "Blum":
                                            print("ID tidak ditemukan!")
                                        case "Udah":
                                            print("Berhasil restock!")
                                case "3":
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
                                    print()
                                    ubah=input("Masukkan ID barang yang ingin Anda kurangi stoknya!\n").upper().strip()
                                    while not ubah.isalnum():
                                        ubah=input("Hanya masukkan huruf dan angka!\n").upper().strip()
                                    dikurang=input("Stoknya ingin dikurangi berapa? (Masukkan seluruh stok yang tersedia untuk menghapus)\n")
                                    while not dikurang.isdigit():
                                        dikurang=input("Hanya masukkan angka!\n")
                                    dikurang=int(dikurang)
                                    hapushasil=KerjaDatabase.kurangibarang(ubah, dikurang)
                                    match hapushasil:
                                        case "Blum":
                                            print("ID Barang tidak valid!")
                                        case "Dihapus":
                                            print("ID Barang berhasil dihapus!")
                                        case "Dikurangi":
                                            print("Barang berhasil dikurangi!")
                                case "0":
                                    break
                    case "3":
                        KerjaDatabase.nambahbarang()
                    case "4":
                        while True:
                            try:
                                opsi4=int(input("Ingin menghapus atau memulihkan barang?\n1= Hapus\n2= Pulihkan\n0= Keluar\n\n"))
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
                    case "999":
                        Main.Login()
                    case "0":
                        sys.exit()
                    case "000":
                        if role=="ADMIN":
                            punyaadmin(username,role)
                        else:
                            print("Input anda tidak valid!")
                    case _:
                        print("Input anda tidak valid!")
