import Admin
import Gudang
import Kasir

print("===========================================================================")
print("                       Selamat Datang di SMK MART              ")
print("===========================================================================")
while True:
    print("Siapakah anda? \n1=Admin \n2=Kasir \n3=Petugas Gudang")
    role = input("\n")
    match role:
        case "1":
            Admin.MAdmin()
            break
        case "2":
            Kasir.MKasir()
            break
        case "3":
            Gudang.MGudang()
            break
        case _:
            print("Masukkan input yang valid!")
