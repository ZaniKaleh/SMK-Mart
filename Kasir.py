from ast import While

import KerjaDatabase


def Kasirnya(role,username):
        print("\n---------Selamat Datang di Bagian Kasir---------")
        keranjang = []
        total = 0

        selesai_belanja = False
        while not selesai_belanja:
            print("\nOpsi Kasir:")
            print("1 = Cari/Lihat Barang")
            print("2 = Jual Barang (Masukkan ID)")
            opsi = input("Pilih Opsi:\n")

            if opsi == "1":
                kluaropsi=opsi
                while kluaropsi=="1":
                    kata_kunci = input("Masukkan nama/ID barang yang dicari (0 untuk lihat semua)\n999. Keluar\n\n").lower()
                    f = KerjaDatabase.spilstok(role)
                    if kata_kunci=="0":
                        for kat, det in f.items():
                            print(f"\n>> {kat.upper()}")
                            for idi, laina in det.items():
                                print(f"[{idi}] {laina['Nama Barang']}")
                                print(f"      Stok  : {laina['Stok']}")
                                print(f"      Harga : Rp {laina['Harga']:,.0f}".replace(",", "."))
                                if role=="ADMIN":
                                    if laina['Kondisi']==1:
                                        print("      Status: Aktif")
                                    if laina['Kondisi']==0:
                                        print("      Status: Nonaktif")
                    elif kata_kunci.strip()=="999":
                        break

                    else:
                        for kat, det in f.items():
                            print(f"\n>> {kat.upper()}")
                            for idi, laina in det.items():
                                if kata_kunci in idi.lower() or kata_kunci in laina['Nama Barang'].lower():
                                    print(f"[{idi}] {laina['Nama Barang']}")
                                    print(f"      Stok  : {laina['Stok']}")
                                    print(f"      Harga : Rp {laina['Harga']:,.0f}".replace(",", "."))
                                    if role=="ADMIN":
                                        if laina['Kondisi']==1:
                                            print("      Status: Aktif")
                                        if laina['Kondisi']==0:
                                            print("      Status: Nonaktif")
                                else:
                                    print("Barang tidak ditemukan!")
            elif opsi == "2":
                Belilagi=True
                while Belilagi==True:
                    idygy = input("Masukkan ID Barang yang dibeli oleh pelanggan!\n").upper()
                    hasilbeli = KerjaDatabase.serch(idygy)

                    if hasilbeli == idygy:
                        try:
                            beli = int(input("Masukkan jumlah barang yang dibeli!\n"))
                        except ValueError:
                            print("Harap masukkan angka!")
                            continue

                        if beli > 0:
                            akhir = KerjaDatabase.transaksi(beli, hasilbeli)

                            if akhir == 0:
                                print("Pembelian gagal! Stok kurang atau ID tidak valid.")
                            else:
                                keranjang=KerjaDatabase.keranjangnya(idygy, keranjang, beli, akhir)
                                total += akhir
                                print(f"\nBarang ditambahkan ke keranjang. Subtotal item ini: Rp {akhir:,.0f}".replace(",", "."))
                                print(f"Total sementara: Rp {total:,.0f}".replace(",", "."))

                                lagi = input(
                                    "Apakah pelanggan ingin membeli lagi?\n1= Ya\n2= Tidak\n3= Lihat keranjang\n"
                                )
                                match lagi:
                                    case "2":
                                        selesai_belanja = True
                                        Belilagi=False
                                        break
                                    case "1":
                                        continue
                                    case "3":
                                        while lagi == "3":
                                            if len(keranjang)>0:
                                                print("\n--- Isi Keranjang Sementara ---")
                                                for isi in keranjang:
                                                    for idb, detail in isi.items():
                                                        print(f"[{idb}] {detail['Nama Barang']} | Jumlah: {detail['Jumlah dibeli']} | Harga: Rp {detail['Harga']:,.0f}".replace(",", "."))
                                                print(f"Total sementara: Rp {total:,.0f}".replace(",", "."))
                                            elif len(keranjang)<=0:
                                                print("Keranjang saat ini sedang kosong!")
                                            lagi1 = input("\nApakah pelanggan ingin membeli lagi?\n1= Ya\n2= Tidak\n3= Hapus barang di keranjang\n")
                                            match lagi1:
                                                case "1":
                                                    break
                                                case "2":
                                                    selesai_belanja=True
                                                    Belilagi=False
                                                    break
                                                case "3":
                                                    if len(keranjang)==0:
                                                        print("Keranjang saat ini sedang kosong!")
                                                    else:
                                                        idkeranjang=input("Masukkan ID barang di keranjang yang ingin dihapus!\n")
                                                        for isi in keranjang:
                                                            for idb, detail in isi.items():
                                                                if idkeranjang==idb:
                                                                    jumlahdikurangi=input("Berapa jumlah yang ingin dikurangi?\n")
                                                                    if jumlahdikurangi<=detail['Jumlah dibeli']:
                                                                        hasilkeranjang=KerjaDatabase.hapuskeranjang(jumlahdikurangi, idkeranjang)
                                                                        if hasilkeranjang==True:
                                                                            print("Berhasil menghapus barang dari keranjang!")
                                                                        elif hasilkeranjang==False:
                                                                            print("Gagal menghapus!")
                                                                    elif jumlahdikurangi>detail['Stok']:
                                                                        print("Jumlah yang dikurangi melebihi jumlah di keranjang!")

                                    case _:
                                        print("Input tidak valid!")

                        else:
                            print("Jumlah barang harus lebih dari 0!")
                    else:
                        print("ID barang yang anda masukkan tidak terdaftar!")
                    if Belilagi==False:
                        break
            else:
                print("Opsi tidak valid!")
            if selesai_belanja==True:
                break
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
