from ast import While
from datetime import datetime
import random

from Main import username

def spilstok(job):
    stok = {}
    try:
        with open('Stok.txt', 'r') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split('|')
                    kat = parts[0]
                    aidi = parts[1]
                    nama = parts[2]
                    stok_jml = int(parts[3])
                    harga = int(parts[4])
                    stok_min = int(parts[5])
                    aktif = int(parts[6]) if len(parts) > 6 else 1

                    if job != "ADMIN" and aktif==0:
                        continue

                    if kat not in stok:
                        stok[kat] = {}
                    stok[kat][aidi] = {
                        'Nama Barang': nama,
                        'Stok': stok_jml,
                        'Harga': harga,
                        'Stok Minimum': stok_min,
                        'Kondisi': aktif
                    }
    except FileNotFoundError:
        pass
    return stok

def spiluser(Tanda):
    users = {}
    try:
        with open('User.txt', 'r') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split('|')
                    aidi = parts[0]
                    uname = parts[1]
                    role = parts[2]
                    pwd = parts[3]
                    kondisi = parts[4]
                    if Tanda=="Neg":
                        if kondisi=="0":
                            users[aidi] = {
                                "Username": uname,
                                "Role": role,
                                "Password": pwd,
                                "Kondisi": kondisi
                            }
                        else:
                            pass
                    elif Tanda=="Pos":
                        if kondisi=="1":
                            users[aidi] = {
                                "Username": uname,
                                "Role": role,
                                "Password": pwd,
                                "Kondisi": kondisi
                            }
                        else:
                            pass
                    elif Tanda=="Uni":
                        users[aidi] = {
                            "Username": uname,
                            "Role": role,
                            "Password": pwd,
                            "Kondisi": kondisi
                        }

    except FileNotFoundError:
        pass
    return users

def tambahuser():
    while True:
        print("\n== Tambah User Baru ==")
        uname = input("\n0 untuk keluar\nMasukkan Username:\n").strip()
        if uname=="0".strip():
            return
        role = input("Masukkan Role (Admin/Kasir/Pengelola Gudang):\n").upper().strip()
        if role=="ADMIN" or role=="KASIR" or role=="PENGELOLA GUDANG":
            pwd = input("Masukkan Password:\n").strip()
            if uname=="" or role=="" or pwd=="":
                print("Semua kolom harus diisi")
            elif "|" in uname or "|" in pwd or "|" in role:
                print("Nama, Role, atau Password tidak boleh mengandung '|'!")
            else:
                break
        else:
            print("Pilih salah satu di antara Admin, Kasir, atau Pengelola Gudang!")
    users = spiluser("Uni")
    yangada=True
    while True:
        aidi=str(random.randrange(100000,999999))
        yangada=False
        for iduser in users.keys():
            if iduser.strip()==aidi:
                yangada=True
                break
        if yangada==False:
            break
    users[aidi] = {"Username": uname, "Role": role, "Password": pwd}

    with open('User.txt', 'w') as file:
        for id_u, det in users.items():
            file.writelines(f"{id_u}|{det['Username']}|{det['Role']}|{det['Password']}|{det.get('Kondisi', '1')}\n")
    print("User berhasil ditambahkan!")

def hapususer():
    while True:
        print("\n== Hapus User ==")
        aidi_hapus = input("Masukkan ID User yang akan dihapus\n0 untuk keluar\n")
        if aidi_hapus=="0".strip():
            return
        users = spiluser("Pos")
        for aidi, ditel in users.items():
            if aidi_hapus in aidi:
                ditel['Kondisi']="0"
                with open('User.txt', 'w') as file:
                    for id_u, det in users.items():
                        file.writelines(f"{id_u}|{det['Username']}|{det['Role']}|{det['Password']}|{det.get('Kondisi', '1')}\n")
                print("User berhasil dihapus dari sistem!")
                return
            else:
                print("ID User tidak ditemukan!")

def spillaporan():
    laporan = {}
    try:
        with open('Laporan.txt', 'r') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split('|')
                    tanggal = parts[1]
                    kasir = parts[2]
                    terjual = int(parts[3])
                    pembelian = int(parts[4])
                    uang=int(parts[5])
                    kembalian=int(parts[6])
                    barang_raw = parts[7]

                    tgl_kunci = tanggal.split(' ')[0]

                    if tgl_kunci not in laporan:
                        laporan[tgl_kunci] = []

                    list_barang = []
                    if barang_raw:
                        items = barang_raw.split('#')
                        for item in items:
                            b_parts = item.split(';')
                            idb = b_parts[0]
                            nama = b_parts[1]
                            jml = int(b_parts[2])
                            hrg_sat = int(b_parts[3])
                            hrg_tot = int(b_parts[4])
                            list_barang.append({
                                idb: {
                                    "Nama Barang": nama,
                                    "Jumlah dibeli": jml,
                                    "Harga Satuan": hrg_sat,
                                    "Harga": hrg_tot
                                }
                            })

                    laporan[tgl_kunci].append({
                        "Tanggal": tanggal,
                        "Kasir": kasir,
                        "Total Terjual": terjual,
                        "Total Pembelian": pembelian,
                        "Uang Pembeli": uang,
                        "Kembalian": kembalian,
                        "Barang yang dibeli": list_barang
                    })
    except FileNotFoundError:
        pass
    return laporan

def simpanstok(dataterbaru):
    with open('Stok.txt', 'w') as file:
        for kat, isikat in dataterbaru.items():
            for aidi, detail in isikat.items():
                kondisi = detail.get('Kondisi', 1)
                file.write(f"{kat}|{aidi}|{detail['Nama Barang']}|{detail['Stok']}|{detail['Harga']}|{detail['Stok Minimum']}|{kondisi}\n")

def simpanlaporan(omtewe, bulan):
    with open('Laporan.txt', 'a') as file:
        barang_strings = []
        for item in omtewe['Barang yang dibeli']:
            for idb, detail in item.items():
                b_str = f"{idb};{detail['Nama Barang']};{detail['Jumlah dibeli']};{detail['Harga Satuan']};{detail['Harga']}"
                barang_strings.append(b_str)
        barang_gabungan = "#".join(barang_strings)

        baris = f"{bulan}|{omtewe['Tanggal']}|{omtewe['Kasir']}|{omtewe['Total Terjual']}|{omtewe['Total Pembelian']}|{omtewe['Uang Pembeli']}|{omtewe['Kembalian']}|{barang_gabungan}\n"
        file.write(baris)

def BucketSort(IsiKategori1, descending=False):
    daftar_barang = list(IsiKategori1.items())
    buckets = [[] for _ in range(26)]

    for Aidi, detail in daftar_barang:
        huruf_awal = Aidi[0].upper()
        index_keranjang = ord(huruf_awal) - 65
        if index_keranjang < 0 or index_keranjang > 25:
            index_keranjang = 0
        buckets[index_keranjang].append((Aidi, detail))

    if descending == True:
        buckets.reverse()

    hasil_akhir = []
    for keranjang in buckets:
        keranjang.sort(key=lambda x: x[0], reverse=descending)
        hasil_akhir.extend(keranjang)

    return hasil_akhir

def urutygy(job, descending=False):
    Sementara = spilstok(job)
    semua_barang = {}

    for _, IsiKategori in Sementara.items():
        semua_barang.update(IsiKategori)

    return BucketSort(semua_barang, descending=descending)

def login(usernamecek,passwordcek):
    loginkan=spiluser("Pos")
    kondisilogin=""
    for _, detailuser in loginkan.items():
        if detailuser['Username']==usernamecek and detailuser['Password']==passwordcek and detailuser['Kondisi']=="1":
            if detailuser['Role'].upper()=="Admin".upper():
                kondisilogin="YaAdmin"
                break
            elif detailuser['Role'].upper()=="Kasir".upper():
                kondisilogin="YaKasir"
                break
            elif detailuser['Role'].upper()=="Pengelola Gudang".upper():
                kondisilogin="YaGudang"
                break
        elif detailuser['Username']==usernamecek and detailuser['Password']==passwordcek and detailuser['Kondisi']=="0":
            print("Akun ini sedang dinonaktifkan!")
    return kondisilogin

def editbarang(Aidibarang, editstok):
    cekdata=spilstok("ADMIN")
    berhasiledit="IDgagal"
    for _, detailygy in cekdata.items():
        for AidiT, ditel in detailygy.items():
            if AidiT==Aidibarang:
                if editstok<ditel['Stok Minimum']:
                    berhasiledit="Ngawur"
                    break
                else:
                    ditel['Stok']=editstok
                    simpanstok(cekdata)
                    berhasiledit="Berhasil"
                    break
        if berhasiledit=="Berhasil":
            break
    return berhasiledit

def hapusbarang():
    print("\n== Nonaktifkan Barang ==")
    Aidibarang = input("Masukkan ID barang yang ingin dinonaktifkan:\n").upper()
    cekdata = spilstok("ADMIN")
    ditemukan = False
    for isikategori in cekdata.values():
        if Aidibarang in isikategori:
            isikategori[Aidibarang]['Kondisi'] = 0
            simpanstok(cekdata)
            print(f"Barang {Aidibarang} berhasil dinonaktifkan!")
            ditemukan = True
            break
    if not ditemukan:
        print("ID barang tidak ditemukan!")

def serch(Aidibarang):
    otw=spilstok(0)
    for _, isinya in otw.items():
        for Aidiya, ditails in isinya.items():
            if Aidibarang==Aidiya:
                print("\n>> Ditemukan!")
                print(f"{'ID BARANG':<10} | {'NAMA BARANG':<30} | {'STOK':>10} | {'HARGA':>16}")
                print("-"*75)
                harga = f"Rp {ditails['Harga']:,.0f}".replace(",", ".")
                print(f"{Aidiya:<10} | {ditails['Nama Barang']:<30} | {ditails['Stok']:>6} pcs | {harga:>16}")
                return Aidiya
    return None

def transaksi(jumlahbeli, aidibrg):
    ambil=spilstok("ADMIN")
    ringkas=0
    for _, lain1 in ambil.items():
        for aidi, lain2 in lain1.items():
            if aidi==aidibrg:
                if lain2['Kondisi']==0:
                    return ringkas
                if lain2['Stok']>=jumlahbeli:
                    lain2['Stok']-=jumlahbeli
                    simpanstok(ambil)
                    return hitungharga(jumlahbeli, lain2['Harga'])
                else:
                    print("Stok barang tidak cukup!")
                    return ringkas
    return ringkas

def hitungharga(jumlah, hargabrg):
    ringkas=hargabrg*jumlah
    return ringkas

def keranjangnya(idygy, keranjang, beli, akhir):
    z=spilstok("ADMIN")
    ditemukan = False
    for _, ntar in z.items():
        for idi, sisay in ntar.items():
            if idi == idygy:
                ditemukan = True
                dikeranjang=False
                for item in keranjang:
                    if idygy in item:
                        item[idygy]['Jumlah dibeli']+=beli
                        item[idygy]['Harga']+=akhir
                        dikeranjang=True
                        break
                    if not dikeranjang:
                        keranjang.append({
                            idygy:{
                                'Nama Barang': sisay['Nama Barang'],
                                'Jumlah dibeli': beli,
                                'Harga Satuan': sisay['Harga'],
                                'Harga': akhir
                            }
                        })
                        break
                break
        if ditemukan==True:
            break
    return keranjang

def strok(username, keranjang, total, uang, kembalian):
    w=datetime.now()
    Posisi=w.strftime("%Y-%m-%d %H:%M")
    bulan=w.strftime("%m")
    terjual=0
    print("\n================= STRUK PEMBELIAN =================")
    print(f"Kasir : {username}")
    no = 1
    for isi in keranjang:
        for idb, detail in isi.items():
                print(f"{no}. {detail['Nama Barang']} (ID: {idb})")
                print(f"    Jumlah        : {detail['Jumlah dibeli']}")
                print(f"    Harga Satuan  : Rp {detail['Harga Satuan']:,.0f}".replace(",", "."))
                print(f"    Subtotal      : Rp {detail['Harga']:,.0f}".replace(",", "."))
                no += 1
                terjual += detail['Jumlah dibeli']
    print("-----------------------------------------------------")
    print(f"TOTAL BELANJA   : Rp {total:,.0f}".replace(",", "."))
    print(f"TUNAI DIBAYAR   : Rp {uang:,.0f}".replace(",", "."))
    print(f"KEMBALIAN       : Rp {kembalian:,.0f}".replace(",", "."))
    print("")
    print(f"Waktu Pembelian : {Posisi}")
    print("=====================================================\n")

    formatakhir={
        "Tanggal": Posisi,
        "Kasir": username,
        "Total Terjual": terjual,
        "Total Pembelian": total,
        "Uang Pembeli": uang,
        "Kembalian": kembalian,
        "Barang yang dibeli": keranjang,
    }
    simpanlaporan(formatakhir, bulan)

def nambahbarang():
    print("================================================")
    print("             Penambahan Barang Baru")
    print("================================================\n")

    kat_dict = {}
    try:
        with open("Kategori.txt", "r") as file_kat:
            for line in file_kat:
                if line.strip():
                    p = line.strip().split('|')
                    kat_dict[p[0]] = p[1]
    except FileNotFoundError:
        print("File Kategori.txt tidak ditemukan!")
        return

    print("Kategori tersedia:")
    for k in kat_dict:
        print(f"- {k.title()}")

    print("- [Atau ketik 'BARU' untuk membuat kategori baru]")

    kat = input("\nMasukkan kategori barangmu:\n").lower()

    if kat == "baru":
        kat = input("Masukkan nama kategori baru (contoh: minuman):\n").lower()
        if kat in kat_dict:
            print("Kategori tersebut ternyata sudah terdaftar!")
            inisial = kat_dict[kat]
        else:
            while True:
                inisial = input(f"Masukkan inisial untuk {kat.title()} (contoh: MNM):\n").upper()
                if inisial in kat_dict.values():
                    print("Inisial tersebut sudah digunakan! Gunakan inisial yang berbeda.")
                elif len(inisial) == 0:
                    print("Inisial tidak boleh kosong!")
                elif len(inisial)<3:
                    print("Inisal tidak boleh kurang dari 3!")
                elif len(inisial)>3:
                    print("Inisial tidak boleh lebih dari 3!")
                else:
                    break

            with open("Kategori.txt", "a") as file_kat_append:
                file_kat_append.write(f"\n{kat}|{inisial}\n")

            kat_dict[kat] = inisial
            print(f">> Kategori '{kat.title()}' berhasil disimpan!")

    elif kat not in kat_dict:
        print("Kategori tidak valid/tidak terdaftar!")
        return
    else:
        inisial = kat_dict[kat]

    stok=spilstok("ADMIN")

    maks_id = 0
    if kat in stok:
        for existing_id in stok[kat].keys():
            try:
                angka = int(existing_id[len(inisial):])
                if angka > maks_id:
                    maks_id = angka
            except ValueError:
                pass

    eidi = f"{inisial}{maks_id + 1:03d}"
    print(f"\nID Otomatis dibuat: {eidi}")

    nam=input("Masukkan Nama Barangmu:\n")
    try:
        stk=int(input("Masukkan Stok awal:\n"))
        hrg=int(input("Masukkan harga:\n"))
        stkm=int(input("Masukkan stok minimum:\n"))
    except ValueError:
        print("Mohon masukkan angka!")
        return

    if kat not in stok:
        stok[kat]={}

    stok[kat][eidi]={
        'Nama Barang': nam,
        'Stok': stk,
        'Harga': hrg,
        'Stok Minimum': stkm,
        'Kondisi': 1
    }
    simpanstok(stok)
    print(f"{nam} berhasil ditambahkan!")

def laporan(bulan):
    laporan_data = spillaporan()
    if bulan in laporan_data:
        hitung=0
        Jbarang=0
        barang=0
        total=0
        print(f"\n==== LAPORAN PENJUALAN TANGGAL {bulan} ====")
        for transaksi in laporan_data[bulan]:
            print("")
            print("-"*40)
            print(f"Tanggal: {transaksi['Tanggal']}")
            print(f"Kasir: {transaksi['Kasir']}")
            print("Barang yang dibeli:")
            hitung += 1
            for item in transaksi['Barang yang dibeli']:
                for idb, detail in item.items():
                    print(f"\n  - {detail['Nama Barang']} (ID: {idb})")
                    print(f"    Jumlah: {detail['Jumlah dibeli']}")
                    print(f"    Harga Satuan: Rp {detail['Harga Satuan']:,.0f}".replace(",", "."))
                    print(f"    Subtotal: Rp {detail['Harga']:,.0f}".replace(",", "."))
                    Jbarang+=1
                    barang+=detail['Jumlah dibeli']
            print(f"\nTotal barang yang terjual: {transaksi['Total Terjual']}")
            print(f"Total transaksi: Rp {transaksi['Total Pembelian']:,.0f}".replace(",", "."))
            print(f"Uang Pembeli   : Rp {transaksi['Uang Pembeli']:,.0f}".replace(",","."))
            print(f"Kembalian      : Rp {transaksi['Kembalian']:,.0f}".replace(",","."))
            total += transaksi['Total Pembelian']
            print("-"*40)
        print("")
        print("="*40)
        print(f"Total Pembelian: Rp {total:,.0f}".replace(",", "."))
        print(f"Jumlah Transaksi: {hitung}")
        print(f"Jumlah Barang Terjual: {barang}")
        print(f"Jenis Barang Terjual: {Jbarang}")
        print("="*40)
    else:
        print(f"Tidak ada data laporan penjualan untuk tanggal {bulan}.")

def hapuskeranjang(ygdihapus, IDdihapus):
    cek=spilstok("ADMIN")
    for _, iye in cek.items():
        for aidi, lain in iye.items():
            if aidi==IDdihapus:
                lain['Stok']+=ygdihapus
                simpanstok(cek)
                return True
    return False

def diaktifkan():
    print("\n== Aktifkan Barang ==")
    Aidibarang = input("Masukkan ID barang yang ingin diaktifkan:\n").upper()
    cekdata = spilstok("Admin")
    ditemukan = False
    for isikategori in cekdata.values():
        if Aidibarang in isikategori:
            isikategori[Aidibarang]['Kondisi'] = 1
            simpanstok(cekdata)
            print(f"Barang {Aidibarang} berhasil diaktifkan!")
            ditemukan = True
            break
    if not ditemukan:
        print("ID barang tidak ditemukan!")

def diaktifkanuser():
    while True:
        print("\n====================== DAFTAR USER SMK MART ======================")
        print(f"{'ID USER':<10} | {'USERNAME':<18} | {'ROLE':<20} | {'KONDISI':<10}")
        print("-"*67)
        daftar=spiluser("Neg")
        for idi, lainnya in daftar.items():
            kondisiuser="Nonaktif"
            print(f"{idi:<10} | {lainnya['Username']:<18} | {lainnya['Role']:<20} | {kondisiuser:<10}")
        aidi=input("Masukkan Aidi yang akan diaktifkan usernya!\n0 untuk keluar\n")
        yaitu=False
        for idi, lainnya in daftar.items():
            if aidi==idi:
                yaitu=True
        if yaitu==False:
            print("Aidi tidak ditemukan!")
