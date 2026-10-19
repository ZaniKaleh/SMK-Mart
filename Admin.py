import KerjaDatabase
import Gudang
import Kasir
import sys

def MAdmin():
    role="Admin"
    while True:
        print("\nMasukkan Username Admin:\n")
        username=input()
        print("\nMasukkan Password Admin:\n")
        password = input()
        validasiuser=KerjaDatabase.login(username,password,role)
        if validasiuser == True:
            while True:
                print("---------Selamat Datang di Kontrol Admin---------")
                print("Tugas apa yang ingin dilakukan?")
                print("1= Manajemen User (Lihat/Tambah/Hapus)")
                print("2= Buat laporan Penjualan")
                print("3= Buka Menu Gudang")
                print("4= Buka Menu Kasir")
                tugasadmin=input("0= Untuk keluar\n")
                match tugasadmin:
                    case "1":
                        print("\n1. Lihat User\n2. Tambah User\n3. Hapus User")
                        pilih = input("Pilih aksi:\n")
                        if pilih == "1":
                            daftaruser=KerjaDatabase.spiluser()
                            for AidiUser, lainUser in daftaruser.items():
                                print(f"\nID User: {AidiUser}")
                                print(f"Username: {lainUser['Username']}")
                                print(f"Password: {lainUser['Password']}")
                                print(f"Role: {lainUser['Role']}")
                                if lainUser.get('Kondisi')=="1":
                                    print("Kondisi: Aktif")
                                elif lainUser.get('Kondisi')=="0":
                                    print("Kondisi: Nonaktif")
                        elif pilih == "2":
                            KerjaDatabase.tambahuser()
                        elif pilih == "3":
                            KerjaDatabase.hapususer()
                        else:
                            print("Input tidak valid!")
                    case "2":
                        while True:
                            try:
                                tahun = int(input("Masukkan tahun (contoh: 2026):\n"))
                                bulan = int(input("Masukkan bulan (1-12):\n"))
                                tanggal = int(input("Masukkan tanggal (1-31):\n"))
                                
                                if 1 <= bulan <= 12:
                                    hari_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                                    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                                        hari_max[1] = 29
                                        
                                    if 1 <= tanggal <= hari_max[bulan - 1]:
                                        tgl_cari = f"{tahun}-{bulan:02d}-{tanggal:02d}"
                                        KerjaDatabase.laporan(tgl_cari)
                                        break
                                    else:
                                        print("Tanggal tidak valid untuk bulan/tahun tersebut!")
                                else:
                                    print("Bulan tidak valid! Masukkan angka 1-12.")
                            except ValueError:
                                print("Masukkan angka yang valid!")
                    case "3":
                        Gudang.Gudangnya(role)
                    case "4":
                        Kasir.Kasirnya(role, username)
                    case "0":
                        sys.exit()
                    case _:
                        print("Input tidak valid!")
            break
        elif validasiuser==False:
            print("Username, Password, atau Role Anda tidak valid!")