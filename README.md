# SMK Mart - Sistem Manajemen Kasir dan Gudang

SMK Mart adalah aplikasi antarmuka teks (CLI) berbasis Python yang dirancang untuk mengelola operasional minimarket. Aplikasi ini mendukung tiga peran utama pengguna, yaitu Admin, Kasir, dan Petugas Gudang. Sebagai sistem penyimpanan data, program ini memanfaatkan manipulasi file teks secara langsung sehingga tidak memerlukan instalasi aplikasi database tambahan.

## Fitur Utama

*   **Sistem Login Terpusat**: Akses sistem dibatasi dan disesuaikan berdasarkan peran pengguna melalui verifikasi username dan password.
*   **Menu Admin**: Admin memiliki kontrol untuk menambah, melihat, dan menghapus akun pengguna sistem. Admin juga dapat mencetak laporan penjualan berdasarkan tanggal, serta memiliki hak akses penuh untuk masuk ke menu Gudang maupun Kasir.
*   **Menu Pengelola Gudang**: Petugas gudang dapat melihat daftar barang yang dilengkapi fitur pengurutan (sorting) secara ascending, descending, maupun per kategori. Tersedia juga fitur untuk mengedit stok, mendaftarkan barang atau kategori baru, serta menonaktifkan barang agar tidak tampil di kasir.
*   **Menu Kasir**: Kasir dapat mencari barang, memasukkan barang ke dalam keranjang belanja, dan menghitung subtotal secara otomatis. Sistem juga akan menghitung uang kembalian dan mencetak struk transaksi di layar.

## Struktur File

*   **Main.py**: File utama yang harus dieksekusi pertama kali untuk menjalankan program dan memilih peran.
*   **Admin.py**: Berisi antarmuka dan alur kerja khusus untuk menu kontrol Admin.
*   **Gudang.py**: Berisi antarmuka untuk fitur manajemen stok dan pendataan barang.
*   **Kasir.py**: Berisi antarmuka sistem point-of-sale untuk memproses transaksi pembeli.
*   **KerjaDatabase.py**: Modul inti yang berisi seluruh fungsi pemrosesan data, operasi baca-tulis file, hingga algoritma pengurutan data.
*   **Stok.txt**: File teks sebagai basis data daftar barang, harga, jumlah stok, dan status aktif.
*   **User.txt**: File teks sebagai basis data akun pengguna dan kata sandi.
*   **Kategori.txt**: File teks untuk menyimpan referensi nama kategori beserta inisial kodenya.

## Cara Menjalankan Program

1.  Pastikan bahasa pemrograman Python sudah terinstal di perangkat.
2.  Buka terminal atau command prompt.
3.  Arahkan direktori terminal ke folder tempat file-file Python ini disimpan.
4.  Ketik perintah `python Main.py` lalu tekan Enter.

## Akun Default (Untuk Uji Coba)

Gunakan kredensial berikut untuk masuk ke dalam sistem saat pertama kali dijalankan:

*   **Admin**
    *   Username: Kang_Admin
    *   Password: Admin#12345
*   **Petugas Gudang**
    *   Username: Kang_Gudang
    *   Password: Gudang#12345[cite: 4]
*   **Kasir**
    *   Username: Mbak_Kasir[cite: 4]
    *   Password: Kasir#12345[cite: 4]
