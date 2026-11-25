import sys

import Admin
import Gudang
import Kasir
import KerjaDatabase


def Login():
    gagal=0
    batas=5
    print("===========================================================================")
    print("                       Selamat Datang di SMK MART              ")
    print("===========================================================================")
    while True:
        print("\nMasukkan Username Anda:\n")
        username=input()
        password = KerjaDatabase.Pewe("\nMasukkan Password Anda\n")
        validasiuser=KerjaDatabase.login(username,password)
        if validasiuser =="YaAdmin" :
            Admin.punyaadmin(username, "ADMIN")
        elif validasiuser=="YaKasir":
            Kasir.Kasirnya("KASIR", username)
        elif validasiuser=="YaGudang":
            Gudang.Gudangnya(username, "PENGELOLA GUDANG")
        else:
            print("Username, Password, atau Role Anda tidak valid!")
            gagal+=1
            if gagal==batas:
                print("\nTerlalu banyak percobaan gagal! Anda dikeluarkan dari program")
                sys.exit()
            else:
                print(f"Kesempatan login tersisa {batas-gagal} kali lagi!")

if __name__ == "__main__":
    Login()
