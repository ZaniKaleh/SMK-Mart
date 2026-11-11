import Admin
import Gudang
import Kasir
import KerjaDatabase

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
        Admin.punyaadmin(username, "Admin")
    elif validasiuser=="YaKasir":
        Kasir.Kasirnya("Kasir", username)
    elif validasiuser=="YaGudang":
        Gudang.Gudangnya("Pengelola Gudang")
    else:
        print("Username, Password, atau Role Anda tidak valid!")
