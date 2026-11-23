from ast import While
from pprint import PrettyPrinter
import Main
import sys

import KerjaDatabase


def Kasirnya(role,username):
    from Admin import punyaadmin

    print("\n---------Selamat Datang di Bagian Kasir---------")

    selesai_belanja = False
    while not selesai_belanja:
        uang_pembeli=0
        keranjang = []
        total = 0
        temu=False
        print("\nOpsi Kasir:")
        print("1 = Cari/Lihat Barang")
        print("2 = Jual Barang (Masukkan ID)")
        print("999= Kembali ke Login")
        print("0= Keluar")
        if role=="ADMIN":
            print("000= Kembali ke Menu Admin")
        opsi = input("Pilih Opsi:\n")

        if opsi == "1":
            kluaropsi=opsi
            while kluaropsi=="1":
                kata_kunci = input("Masukkan nama/ID barang yang dicari (0 untuk lihat semua)\n999. Keluar\n\n").lower()
                f = KerjaDatabase.spilstok(role)
                if kata_kunci=="0":
                    for kat, det in f.items():
                        print(f"\n>> Kategori: {kat.upper()}")
                        print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STATUS':<10}")
                        print("-"*88)
                        for idi, laina in det.items():
                            harga = f"Rp {laina['Harga']:,.0f}".replace(",", ".")
                            status = "Aktif" if laina['Kondisi']==1 else "Nonaktif"
                            if role=="ADMIN":
                                print(f"{idi:<10} | {laina['Nama Barang']:<30} | {laina['Stok']:>6} pcs | {harga:>16} | {status:<10}")
                            else:
                                print(f"{idi:<10} | {laina['Nama Barang']:<30} | {laina['Stok']:>6} pcs | {harga:>16} | {'':<10}")
                elif kata_kunci.strip()=="999":
                    break

                else:
                    ditemukan = False
                    for kat, det in f.items():
                        kategori_ditemukan = False
                        for idi, laina in det.items():
                            if kata_kunci in idi.lower() or kata_kunci in laina['Nama Barang'].lower():
                                if kategori_ditemukan==False:
                                    print(f"\n>> Kategori: {kat.upper()}")
                                    print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STATUS':<10}")
                                    print("-"*88)
                                    kategori_ditemukan = True
                                harga = f"Rp {laina['Harga']:,.0f}".replace(",", ".")
                                status = "Aktif" if laina['Kondisi']==1 else "Nonaktif"
                                if role=="ADMIN":
                                    print(f"{idi:<10} | {laina['Nama Barang']:<30} | {laina['Stok']:>6} pcs | {harga:>16} | {status:<10}")
                                else:
                                    print(f"{idi:<10} | {laina['Nama Barang']:<30} | {laina['Stok']:>6} pcs | {harga:>16} | {'':<10}")
                                ditemukan = True
                    if ditemukan==False:
                        print("Barang tidak ditemukan!")
        elif opsi == "2":
            Belilagi=True
            inilah=KerjaDatabase.spilstok(role)
            for kate, isine in inilah.items():
                print(f"\n>> Kategori: {kate.upper()}")
                print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16} | {'STOK MIN':>10} | {'STATUS':<10}")
                print("-"*101)
                for Aidi, detail in isine.items():
                    harga = f"Rp {detail['Harga']:,.0f}".replace(",", ".")
                    status = "Aktif"
                    print(f"{Aidi:<10} | {detail['Nama Barang']:<30} | {detail['Stok']:>6} pcs | {harga:>16} | {detail['Stok Minimum']:>10} | {status:<10}")
            while Belilagi==True:
                idygy = input("Masukkan ID Barang yang dibeli oleh pelanggan!\n").upper().strip()
                while not idygy.isalnum():
                    idygy=input("Hanya masukkan huruf dan angka!").upper().strip()
                hasilbeli = KerjaDatabase.serch(idygy, role)

                if hasilbeli == idygy:
                    while True:
                        try:
                            beli = int(input("Masukkan jumlah barang yang dibeli!\n"))
                        except ValueError:
                            print("Harap masukkan angka!")
                            continue
                        break

                    if beli > 0:
                        akhir,modal,rincian=KerjaDatabase.transaksi(beli, hasilbeli)

                        if akhir == 0:
                            print("Pembelian gagal! Stok kurang atau ID tidak valid.")
                        else:
                            keranjang=KerjaDatabase.keranjangnya(idygy, keranjang, beli, akhir,rincian)
                            total += akhir
                            print(f"\nBarang ditambahkan ke keranjang. Subtotal item ini: Rp {akhir:,.0f}".replace(",", "."))
                            while True:
                                print(f"Total sementara: Rp {total:,.0f}".replace(",", "."))
                                if len(keranjang)>0:
                                    print("\n--- Isi Keranjang Sementara ---")
                                    for isi in keranjang:
                                        for idb, detail in isi.items():
                                            print(f"[{idb}] {detail['Nama Barang']} | Jumlah: {detail['Jumlah dibeli']} | Harga: Rp {detail['Harga']:,.0f}".replace(",", "."))
                                    print(f"Total sementara: Rp {total:,.0f}".replace(",", "."))
                                elif len(keranjang)<=0:
                                    print("\nKeranjang saat ini sedang kosong!")
                                lagi = input(
                                    "Apakah pelanggan ingin membeli lagi?\n1= Ya\n2= Tidak\n3= Hapus Barang di keranjang\n"
                                )
                                match lagi:
                                    case "2":
                                        Belilagi=False
                                        break
                                    case "1":
                                        break
                                    case "3":
                                        if len(keranjang)==0:
                                            print("Keranjang saat ini sedang kosong!")
                                        else:
                                            idkeranjang=input("Masukkan ID barang di keranjang yang ingin dihapus!\n")
                                            for isi in keranjang:
                                                for idb, detail in isi.items():
                                                    if idkeranjang==idb:
                                                        temu=True
                                                        jumlahdikurangi=input("Berapa jumlah yang ingin dikurangi?\n")
                                                        while not jumlahdikurangi.isdigit():
                                                            jumlahdikurangi=input("Masukkan angka yang valid!")
                                                        jumlahdikurangi=int(jumlahdikurangi)
                                                        if 0< jumlahdikurangi<=detail['Jumlah dibeli']:
                                                            hasilkeranjang=KerjaDatabase.hapuskeranjang(jumlahdikurangi, idkeranjang, detail['Rincian'])
                                                            if hasilkeranjang==True:
                                                                total-=detail['Harga Satuan']*jumlahdikurangi
                                                                detail['Jumlah dibeli']-=jumlahdikurangi
                                                                detail['Harga']-=detail['Harga Satuan']*jumlahdikurangi
                                                                if detail['Jumlah dibeli']==0:
                                                                    keranjang.remove(isi)
                                                                print("Berhasil menghapus barang dari keranjang!")
                                                            elif hasilkeranjang==False:
                                                                print("Gagal menghapus!")
                                                        elif jumlahdikurangi>detail['Jumlah dibeli']:
                                                            print("Jumlah yang dikurangi melebihi jumlah di keranjang!")
                                                    if temu:
                                                        break
                                                if not temu:
                                                    print("Tidak terdapat barang dengan ID terebut di keranjangmu!")

                                    case _:
                                        print("Input tidak valid!")
                    else:
                        print("Jumlah barang harus lebih dari 0!")
                elif hasilbeli=="@#":
                    print("ID Barang ini sedang nonaktif!")
                elif hasilbeli=="#$":
                    print("ID barang yang anda masukkan tidak terdaftar!")
                if Belilagi==False:
                    break

        elif opsi=="999"   :
            Main.Login()
        elif opsi=="0":
            sys.exit()
        elif opsi=="000" and role=="ADMIN":
            punyaadmin(username,role)
        else:
            print("Opsi tidak valid!")
        if len(keranjang) > 0:
            print("\n================ PEMBAYARAN ================")
            print(f"Total Belanja yang harus dibayar : Rp {total:,.0f}".replace(",", "."))
            while True:
                try:
                    uang_pembeli = int(input("Masukkan jumlah uang tunai pembeli : Rp "))
                    if uang_pembeli < total:
                        kurang = total - uang_pembeli
                        print(f"Maaf, uang pembeli kurang Rp {kurang:,.0f}".replace(",", "."))
                    elif uang_pembeli==total:
                        print("Uang pembeli pas!")
                        kembalian=0
                        break
                    else:
                        kembalian = uang_pembeli - total
                        print(f"Kembalian yang harus diberikan   : Rp {kembalian:,.0f}".replace(",", "."))
                        break
                except ValueError:
                    print("Harap masukkan angka nominal uang yang valid!")

            KerjaDatabase.strok(username, keranjang, total, uang_pembeli, kembalian)
            while True:
                pembeli=input("Apakah ada pembeli lagi? (Y/n)\n").upper().strip()
                match pembeli:
                    case "Y":
                        break
                    case "":
                        break
                    case "N":
                        selesai_belanja=True
                        break
                    case _:
                        print("Masukkan input yang valid!")
            if selesai_belanja==True:
                break
            else:
                pass
