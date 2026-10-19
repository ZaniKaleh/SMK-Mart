import KerjaDatabase


def MKasir():
    role = "Kasir"
    print("\nMasukkan Username Kasir:\n")
    username = input()
    print("\nMasukkan Password Kasir:\n")
    password = input()
    validasiuser = KerjaDatabase.login(username, password, role)

    if validasiuser == True:
        Kasirnya(role, username)
    elif validasiuser == False:
        print("Username, Password, atau Role anda tidak valid!")

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
                kata_kunci = input("Masukkan nama/ID barang yang dicari (0 untuk lihat semua):\n").lower()
                f = KerjaDatabase.spilstok(role)
                if kata_kunci=="0":
                    for kat, det in f.items():
                        print(f"\n>> {kat.upper()}")
                        for idi, laina in det.items():
                            print(f"[{idi}] {laina['Nama Barang']}")
                            print(f"      Stok  : {laina['Stok']}")
                            print(f"      Harga : Rp {laina['Harga']:,.0f}".replace(",", "."))
                            if role=="Admin":
                                if laina['Kondisi']==1:
                                    print("      Status: Aktif")
                                if laina['Kondisi']==0:
                                    print("      Status: Nonaktif")

                else:
                    for kat, det in f.items():
                        print(f"\n>> {kat.upper()}")
                        for idi, laina in det.items():
                            if kata_kunci in idi.lower() or kata_kunci in laina['Nama Barang'].lower():
                                print(f"[{idi}] {laina['Nama Barang']}")
                                print(f"      Stok  : {laina['Stok']}")
                                print(f"      Harga : Rp {laina['Harga']:,.0f}".replace(",", "."))
                                if role=="Admin":
                                    if laina['Kondisi']==1:
                                        print("      Status: Aktif")
                                    if laina['Kondisi']==0:
                                        print("      Status: Nonaktif")

            elif opsi == "2":
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

                            while lagi == "3":
                                if len(keranjang)>0:
                                    print("\n--- Isi Keranjang Sementara ---")
                                    for isi in keranjang:
                                        for idb, detail in isi.items():
                                            print(f"[{idb}] {detail['Nama Barang']} | Jumlah: {detail['Jumlah dibeli']} | Harga: Rp {detail['Harga']:,.0f}".replace(",", "."))
                                    print(f"Total sementara: Rp {total:,.0f}".replace(",", "."))
                                elif len(keranjang)<=0:
                                    print("Keranjang saat ini sedang kosong!")
                                lagi = input("\nApakah pelanggan ingin membeli lagi?\n1= Ya\n2= Tidak\n3= Lihat keranjang\n4= Hapus barang di keranjang")

                            match lagi:
                                case "2":
                                    selesai_belanja = True
                                case "1":
                                    continue
                                case "4":
                                    if len(keranjang)==0:
                                        print("Keranjang saat ini sedang kosong!")

                                case _:
                                    print("Input tidak valid!")
                    else:
                        print("Jumlah barang harus lebih dari 0!")
                else:
                    print("ID barang yang anda masukkan tidak terdaftar!")
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
                    else:
                        kembalian = uang_pembeli - total
                        print(f"Kembalian yang harus diberikan   : Rp {kembalian:,.0f}".replace(",", "."))
                        break
                except ValueError:
                    print("Harap masukkan angka nominal uang yang valid!")

            KerjaDatabase.strok(username, keranjang, total, uang_pembeli, kembalian)
