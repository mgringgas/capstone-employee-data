# Sistem Data Karyawan (Employee Management CLI)

Program CLI (Command Line Interface) berbasis Python untuk mengelola data karyawan sebuah perusahaan — mulai dari pencatatan data, pencarian, update gaji massal, hingga laporan statistik payroll. Cocok untuk latihan konsep CRUD, struktur data list of dictionaries, dan manipulasi data di Python.

Project ini dibuat sebagai **Capstone Project Module 2 Python** di **Purwadhika JCBDA (Job Connector Business Data Analyst)**.

## Fitur

- **Tampilkan Data Karyawan**
  - Lihat seluruh karyawan aktif dalam tabel rapi (`tabulate`)
  - Cari karyawan berdasarkan ID
  - Cari karyawan berdasarkan nama (partial match / tidak case-sensitive)
  - Filter karyawan berdasarkan divisi
  - Urutkan data (gaji tertinggi–terendah, terendah–tertinggi, atau nama A–Z) menggunakan algoritma Bubble Sort
- **Tambah Karyawan Baru**
  - ID karyawan baru (`EMP00X`) digenerate otomatis
  - Validasi input untuk setiap kolom (nama, divisi, jabatan, gaji)
  - Konfirmasi sebelum data disimpan
- **Ubah Data Karyawan**
  - Update satu kolom tertentu (nama/divisi/jabatan/gaji) untuk satu karyawan
  - Kenaikan gaji massal berdasarkan divisi (dengan persentase kenaikan)
- **Hapus / Resign Karyawan**
  - Karyawan yang dihapus tidak langsung hilang, tapi dipindahkan ke riwayat resign beserta alasan resign-nya
- **Riwayat Resign**
  - Lihat daftar karyawan yang sudah resign beserta alasan dan gaji terakhirnya
- **Restore Karyawan Resign**
  - Kembalikan karyawan dari riwayat resign menjadi karyawan aktif kembali
- **Laporan Statistik Payroll**
  - Total karyawan aktif
  - Total payroll (jumlah seluruh gaji)
  - Rata-rata gaji
  - Karyawan dengan gaji tertinggi & terendah
  - Breakdown jumlah karyawan per divisi

## Teknologi

- Python 3
- [`tabulate`](https://pypi.org/project/tabulate/) — untuk menampilkan data dalam bentuk tabel

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/mgringgas/capstone-employee-data.git
   cd capstone-employee-data
   ```
2. Install dependency yang dibutuhkan:
   ```bash
   pip install tabulate
   ```
3. Jalankan program:
   ```bash
   python main.py
   ```
   *(sesuaikan nama file dengan nama file Python-mu)*

## Cara Penggunaan

Setelah program dijalankan, kamu akan disambut dengan menu utama:

```
=========================================
 Selamat datang di Sistem Data Karyawan
=========================================
List Menu:
1. Menampilkan Data Karyawan
2. Menambah Data Karyawan
3. Mengubah Data Karyawan
4. Hapus / Resign Karyawan
5. Lihat Riwayat Resign
6. Restore Karyawan Resign
7. Laporan Statistik Payroll
8. Exit Program
```

Tinggal masukkan angka sesuai menu yang ingin dijalankan, lalu ikuti instruksi di layar.

> **Tips:** Di sebagian besar input, kamu bisa mengetik `kembali`, `exit`, `batal`, atau `keluarmenu` untuk membatalkan proses dan kembali ke menu sebelumnya.

## Struktur Data

Data karyawan disimpan sementara di memori (in-memory, belum tersambung ke database/file), dengan format:

```python
{
    "id": "EMP001",
    "nama": "Andi",
    "divisi": "HR",
    "jabatan": "Manager",
    "gaji": 15000000
}
```

Karyawan yang resign akan memiliki tambahan field `alasan` yang berisi alasan resign.

## Catatan

- Seluruh data akan **hilang** setiap kali program ditutup, karena data hanya disimpan di variabel Python (belum ada penyimpanan permanen ke file/database).
- Cocok digunakan sebagai bahan belajar/latihan, bukan untuk penggunaan produksi.
