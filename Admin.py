import KerjaDatabase
import Gudang
import Kasir
import sys

def punyaadmin(username, role):
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
                        while tugasadmin=="1":
                            print("\n1. Lihat User\n2. Tambah User\n3. Hapus User\n4. Aktifkan User\n0. Kembali\n")
                            pilih = input("Pilih aksi:\n")
                            daftaruser=KerjaDatabase.spiluser("Pos")
                            if pilih == "1":
                                if len(daftaruser)<=0:
                                    print("Tidak terdapat User!")
                                else:
                                    print("\n====================== DAFTAR USER SMK MART ======================")
                                    print(f"{'ID USER':<10} | {'USERNAME':<18} | {'ROLE':<20} | {'KONDISI':<10}")
                                    print("-"*67)
                                    for AidiUser, lainUser in daftaruser.items():
                                        kondisiuser = "Aktif"
                                        print(f"{AidiUser:<10} | {lainUser['Username']:<18} | {lainUser['Role']:<20} | {kondisiuser:<10}")
                                print("="*67+"\n")
                            elif pilih.strip()== "2":
                                KerjaDatabase.tambahuser()
                            elif pilih.strip()== "3":
                                if len(daftaruser)<=0:
                                    print("Tidak terdapat User!")
                                else:
                                    print("\n====================== DAFTAR USER SMK MART ======================")
                                    print(f"{'ID USER':<10} | {'USERNAME':<18} | {'ROLE':<20} | {'KONDISI':<10}")
                                    print("-"*67)
                                    for AidiUser, lainUser in daftaruser.items():
                                        kondisiuser = "Aktif"
                                        print(f"{AidiUser:<10} | {lainUser['Username']:<18} | {lainUser['Role']:<20} | {kondisiuser:<10}")
                                KerjaDatabase.hapususer()
                            elif pilih.strip()=="4":
                                KerjaDatabase.diaktifkanuser()
                            elif pilih.strip()=="0":
                                break
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
