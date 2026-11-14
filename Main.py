import Admin
import Gudang
import Kasir
import KerjaDatabase
import sys

gagal=0
batas=5
print("===========================================================================")
print("                       Selamat Datang di SMK MART              ")
print("===========================================================================")
while True:
    print("\nMasukkan Username Anda:\n")
    username=input()
    print("\nMasukkan Password Anda:\n")
    password = input()
    validasiuser=KerjaDatabase.login(username,password)
    if validasiuser =="YaAdmin" :
        Admin.punyaadmin(username, "ADMIN")
    elif validasiuser=="YaKasir":
        Kasir.Kasirnya("KASIR", username)
    elif validasiuser=="YaGudang":
        Gudang.Gudangnya("PENGELOLA GUDANG")
    else:
        print("Username, Password, atau Role Anda tidak valid!")
        gagal+=1
        if gagal==batas:
            sys.exit()
        else:
            print(f"Kesempatan login tersisa {batas-gagal} kali lagi!")
