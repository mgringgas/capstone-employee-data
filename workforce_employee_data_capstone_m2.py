from tabulate import tabulate

# 1. Database Dummy
listKaryawan = [
    {"id": "EMP001", "nama": "Andi", "divisi": "HR", "jabatan": "Manager", "gaji": 15000000},
    {"id": "EMP002", "nama": "Budi", "divisi": "IT", "jabatan": "Developer", "gaji": 10000000},
    {"id": "EMP003", "nama": "Cici", "divisi": "Finance", "jabatan": "Staff", "gaji": 8000000},
    {"id": "EMP004", "nama": "Deni", "divisi": "IT", "jabatan": "Senior Developer", "gaji": 13000000},
    {"id": "EMP005", "nama": "Evi", "divisi": "Marketing", "jabatan": "Manager", "gaji": 14000000},
    {"id": "EMP006", "nama": "Fajar", "divisi": "Marketing", "jabatan": "Content Creator", "gaji": 7000000},
    {"id": "EMP007", "nama": "Gita", "divisi": "HR", "jabatan": "Recruiter", "gaji": 7500000},
    {"id": "EMP008", "nama": "Hadi", "divisi": "Operations", "jabatan": "Manager", "gaji": 14500000}
]

listResign = [
    {"id": "EMP000", "nama": "Bambang", "divisi": "IT", "jabatan": "Intern", "gaji": 4000000, "alasan": "Melanjutkan Studi"}
]


# 2. Validasi Input & Generator ID
EXIT_KEYWORDS = ['kembali', 'exit', 'batal', 'keluarmenu']

def inputAngka(prompt):
    text = input(prompt).strip()
    if text.lower() in EXIT_KEYWORDS:
        return None
    while not text.isdigit():
        print("Harus berupa angka! (Ketik 'kembali' untuk membatalkan)")
        text = input(prompt).strip()
        if text.lower() in EXIT_KEYWORDS:
            return None
    return int(text)

def inputTeks(prompt):
    text = input(prompt).strip()
    if text.lower() in EXIT_KEYWORDS:
        return None
    while len(text) == 0:
        print("Tidak boleh kosong! (Ketik 'kembali' untuk membatalkan)")
        text = input(prompt).strip()
        if text.lower() in EXIT_KEYWORDS:
            return None
    return text

def generateNewId():
    # Menentukan ID baru (mencari ID terbesar dari seluruh data)
    maxNum = 0
    semuaData = listKaryawan + listResign
    
    for k in semuaData:
        num = int(k['id'].replace("EMP", ""))
        if num > maxNum:
            maxNum = num
            
    return f"EMP{maxNum + 1:03d}"


# 3. Render Tabel
def printKaryawan(data=None):
    if data is None:
        data = listKaryawan
        
    print('\nDaftar Karyawan Aktif')
    if data:
        tabel = []
        for i in range(len(data)):
            k = data[i]
            gajiFormatted = f"Rp {k['gaji']:,}".replace(",", ".")
            tabel.append([i, k['id'], k['nama'], k['divisi'], k['jabatan'], gajiFormatted])
        
        headers = ["Index", "ID", "Nama", "Divisi", "Jabatan", "Gaji"]
        print(tabulate(tabel, headers=headers, tablefmt="fancy_grid"))
    else:
        print('Tidak terdapat Data Karyawan')

def printResign():
    print('\nRiwayat Karyawan Resign')
    if listResign:
        tabel = []
        for i in range(len(listResign)):
            k = listResign[i]
            gajiFormatted = f"Rp {k['gaji']:,}".replace(",", ".")
            tabel.append([i, k['id'], k['nama'], k['divisi'], k['jabatan'], gajiFormatted, k['alasan']])
            
        headers = ["Index", "ID", "Nama", "Divisi", "Jabatan", "Gaji Terakhir", "Alasan"]
        print(tabulate(tabel, headers=headers, tablefmt="fancy_grid"))
    else:
        print('Belum ada riwayat karyawan resign')


# 4. Logika Pemrosesan Data Khusus (Sort, Search, Batch Update, Restore)
def menuSort():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return

    while True:
        print('\n--- Pilih Urutan Data ---')
        print('1. Gaji Tertinggi ke Terendah')
        print('2. Gaji Terendah ke Tertinggi')
        print('3. Nama Karyawan (A - Z)')
        pilihan = inputAngka('Pilih (1-3 / ketik "kembali") : ')

        if pilihan is None:
            print("\nBatal mengurutkan data.")
            return

        if 1 <= pilihan <= 3:
            break
        print('Pilihan urutan tidak valid!')

    dataSorted = [k for k in listKaryawan]

    # Mengurutkan copy data dengan algoritma Bubble Sort
    n = len(dataSorted)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pilihan == 1:
                if dataSorted[j]['gaji'] < dataSorted[j + 1]['gaji']:
                    dataSorted[j], dataSorted[j + 1] = dataSorted[j + 1], dataSorted[j]
            elif pilihan == 2:
                if dataSorted[j]['gaji'] > dataSorted[j + 1]['gaji']:
                    dataSorted[j], dataSorted[j + 1] = dataSorted[j + 1], dataSorted[j]
            elif pilihan == 3:
                if dataSorted[j]['nama'].lower() > dataSorted[j + 1]['nama'].lower():
                    dataSorted[j], dataSorted[j + 1] = dataSorted[j + 1], dataSorted[j]

    printKaryawan(dataSorted)

def cariNamaPartial():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return
        
    keyword = inputTeks('Masukkan nama / potongan nama (ketik "kembali" untuk batal) : ')
    if keyword is None:
        print("\nPencarian dibatalkan.")
        return
        
    hasilCari = [k for k in listKaryawan if keyword.lower() in k['nama'].lower()]
    printKaryawan(hasilCari)

def naikGajiMassal():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return

    divisiTarget = inputTeks('Masukkan Nama Divisi yang Naik Gaji (ketik "kembali" untuk batal) : ')
    if divisiTarget is None:
        print("\nProses kenaikan gaji dibatalkan.")
        return
    divisiTarget = divisiTarget.upper()

    persen = inputAngka('Masukkan Persentase Kenaikan Gaji (%) : ')
    if persen is None:
        print("\nProses kenaikan gaji dibatalkan.")
        return

    count = 0
    for k in listKaryawan:
        if k['divisi'].upper() == divisiTarget:
            k['gaji'] = int(k['gaji'] + (k['gaji'] * persen / 100))
            count += 1

    if count > 0:
        print(f"\nBerhasil menaikkan gaji {count} karyawan di divisi {divisiTarget} sebesar {persen}%!")
        printKaryawan()
    else:
        print(f"\nTidak ditemukan karyawan pada divisi {divisiTarget}.")

def restoreKaryawan():
    if not listResign:
        print('Riwayat Resign Kosong!')
        return

    printResign()
    while True:
        indexRestore = inputAngka('Masukkan index karyawan resign yang ingin di-restore (ketik "kembali" untuk batal) : ')
        
        if indexRestore is None:
            print("\nRestore dibatalkan.")
            return
            
        if 0 <= indexRestore < len(listResign):
            break
        print('Index tidak ditemukan!')

    konfirmasi = inputTeks('Yakin ingin mengembalikan karyawan ini ke status aktif? (ya/tidak) : ')
    if konfirmasi and konfirmasi.lower() == 'ya':
        karyawanKembali = listResign.pop(indexRestore)
        del karyawanKembali['alasan']
        listKaryawan.append(karyawanKembali)
        print('\nKaryawan berhasil dikembalikan ke status aktif!')
        printKaryawan()
    else:
        print('\nRestore dibatalkan.')


# 5. Handler Menu Fitur CRUD & Statistik
def menuRead():
    while True:
        print('''
Menu Report Data Karyawan:
1. Tampilkan Semua Karyawan Aktif
2. Cari Karyawan Berdasarkan ID
3. Cari Karyawan Berdasarkan Nama (Partial Match)
4. Filter Karyawan Berdasarkan Divisi
5. Urutkan Data Karyawan (Sorting)
6. Kembali ke Menu Utama''')
        
        pilihan = inputAngka('Masukkan pilihan menu (1-6) : ')
        if pilihan is None or pilihan == 6:
            break

        if pilihan == 1:
            printKaryawan()
        elif pilihan == 2:
            if not listKaryawan:
                print('Data Karyawan kosong!')
                continue
            cariID = inputTeks('Masukkan ID Karyawan (ketik "kembali" untuk batal) : ')
            if cariID is None:
                print("\nPencarian dibatalkan.")
                continue
                
            hasilCari = [k for k in listKaryawan if k['id'].upper() == cariID.upper()]
            printKaryawan(hasilCari)
        elif pilihan == 3:
            cariNamaPartial()
        elif pilihan == 4:
            if not listKaryawan:
                print('Data Karyawan kosong!')
                continue
            cariDivisi = inputTeks('Masukkan Nama Divisi (ketik "kembali" untuk batal) : ')
            if cariDivisi is None:
                print("\nFilter dibatalkan.")
                continue
                
            hasilFilter = [k for k in listKaryawan if k['divisi'].upper() == cariDivisi.upper()]
            printKaryawan(hasilFilter)
        elif pilihan == 5:
            menuSort()
        else:
            print('Pilihan menu tidak valid!')

def menuCreate():
    printKaryawan()
    
    print("\n--- Form Tambah Karyawan Baru --- (Ketik 'kembali' di mana saja untuk batal)")
    idBaru = generateNewId()
    print(f"ID Karyawan Baru Ditentukan Otomatis : {idBaru}")
    
    namaBaru = inputTeks('Masukkan Nama Karyawan    : ')
    if namaBaru is None:
        print("\nPenambahan data dibatalkan.")
        return
    namaBaru = namaBaru.title()

    divisiBaru = inputTeks('Masukkan Divisi           : ')
    if divisiBaru is None:
        print("\nPenambahan data dibatalkan.")
        return
    divisiBaru = divisiBaru.upper()

    jabatanBaru = inputTeks('Masukkan Jabatan          : ')
    if jabatanBaru is None:
        print("\nPenambahan data dibatalkan.")
        return
    jabatanBaru = jabatanBaru.title()
    
    while True:
        gajiBaru = inputAngka('Masukkan Gaji Karyawan    : ')
        if gajiBaru is None:
            print("\nPenambahan data dibatalkan.")
            return
        if gajiBaru > 0:
            break
        print('Gaji harus lebih besar dari 0!')

    konfirmasi = inputTeks('Apakah Anda yakin ingin menyimpan data ini? (ya/tidak) : ')
    if konfirmasi and konfirmasi.lower() == 'ya':
        listKaryawan.append({
            "id": idBaru,
            "nama": namaBaru,
            "divisi": divisiBaru,
            "jabatan": jabatanBaru,
            "gaji": gajiBaru
        })
        print('\nData berhasil ditambahkan!')
        printKaryawan()
    else:
        print('\nPenambahan data dibatalkan.')

def menuUpdate():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return

    while True:
        print('''
--- Menu Update Data Karyawan ---
1. Ubah Detail Data 1 Karyawan
2. Kenaikan Gaji Massal per Divisi
3. Kembali ke Menu Utama''')
        pilihanUpdate = inputAngka('Pilih menu update (1-3 / ketik "kembali") : ')
        if pilihanUpdate is None or pilihanUpdate == 3:
            break

        if pilihanUpdate == 1:
            printKaryawan()
            while True:
                indexUbah = inputAngka('Masukkan index karyawan yang ingin diubah (ketik "kembali" untuk batal) : ')
                if indexUbah is None:
                    print("\nUpdate data dibatalkan.")
                    break
                if 0 <= indexUbah < len(listKaryawan):
                    break
                print('Index tidak ditemukan!')

            if indexUbah is None:
                continue

            print('''
Kolom yang ingin diubah:
1. Nama
2. Divisi
3. Jabatan
4. Gaji
5. Batal / Kembali''')
            
            pilihanKolom = inputAngka('Pilih nomor kolom (1-5) : ')
            if pilihanKolom is None or pilihanKolom == 5:
                print("\nUpdate data dibatalkan.")
                continue

            if pilihanKolom == 1:
                valBaru = inputTeks('Masukkan Nama Baru : ')
                if valBaru is None:
                    print("\nUpdate dibatalkan.")
                    continue
                valBaru = valBaru.title()
                keyUbah = 'nama'
            elif pilihanKolom == 2:
                valBaru = inputTeks('Masukkan Divisi Baru : ')
                if valBaru is None:
                    print("\nUpdate dibatalkan.")
                    continue
                valBaru = valBaru.upper()
                keyUbah = 'divisi'
            elif pilihanKolom == 3:
                valBaru = inputTeks('Masukkan Jabatan Baru : ')
                if valBaru is None:
                    print("\nUpdate dibatalkan.")
                    continue
                valBaru = valBaru.title()
                keyUbah = 'jabatan'
            elif pilihanKolom == 4:
                while True:
                    valBaru = inputAngka('Masukkan Gaji Baru : ')
                    if valBaru is None:
                        break
                    if valBaru > 0:
                        break
                    print('Gaji harus lebih besar dari 0!')
                if valBaru is None:
                    print("\nUpdate dibatalkan.")
                    continue
                keyUbah = 'gaji'
            else:
                print('Pilihan kolom tidak valid!')
                continue

            konfirmasi = inputTeks('Apakah Anda yakin ingin mengubah data ini? (ya/tidak) : ')
            if konfirmasi and konfirmasi.lower() == 'ya':
                listKaryawan[indexUbah][keyUbah] = valBaru
                print('\nData berhasil diperbarui!')
                printKaryawan()
            else:
                print('\nPerubahan data dibatalkan.')
                
        elif pilihanUpdate == 2:
            naikGajiMassal()
        else:
            print('Pilihan menu tidak valid!')

def menuDelete():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return

    printKaryawan()
    
    while True:
        indexHapus = inputAngka('Masukkan index karyawan yang keluar/hapus (ketik "kembali" untuk batal) : ')
        if indexHapus is None:
            print("\nPenghapusan data dibatalkan.")
            return
        if 0 <= indexHapus < len(listKaryawan):
            break
        print('Index tidak ditemukan!')

    alasanResign = inputTeks('Masukkan alasan resign : ')
    if alasanResign is None:
        print("\nPenghapusan data dibatalkan.")
        return
    
    konfirmasi = inputTeks('Yakin ingin memindahkan karyawan ini ke riwayat Resign? (ya/tidak) : ')
    if konfirmasi and konfirmasi.lower() == 'ya':
        karyawanKeluar = listKaryawan.pop(indexHapus)
        karyawanKeluar['alasan'] = alasanResign
        listResign.append(karyawanKeluar)
        print('\nData berhasil dipindahkan ke riwayat resign!')
        printKaryawan()
    else:
        print('\nPenghapusan data dibatalkan.')

def menuStatistik():
    if not listKaryawan:
        print('Data Karyawan kosong!')
        return

    # Kalkulasi total, rata-rata, max & min gaji
    totalGaji = 0
    for k in listKaryawan:
        totalGaji += k['gaji']

    rataRataGaji = totalGaji / len(listKaryawan)
    
    gajiMax = listKaryawan[0]
    gajiMin = listKaryawan[0]

    for k in listKaryawan:
        if k['gaji'] > gajiMax['gaji']:
            gajiMax = k
        if k['gaji'] < gajiMin['gaji']:
            gajiMin = k
    
    # Hitung jumlah karyawan per divisi
    divisiCount = {}
    for k in listKaryawan:
        div = k['divisi']
        if div not in divisiCount:
            divisiCount[div] = 1
        else:
            divisiCount[div] += 1

    # Format angka ke tampilan Rupiah
    totalGajiStr = f"Rp {totalGaji:,}".replace(",", ".")
    rataRataStr = f"Rp {int(rataRataGaji):,}".replace(",", ".")
    gajiMaxStr = f"Rp {gajiMax['gaji']:,}".replace(",", ".")
    gajiMinStr = f"Rp {gajiMin['gaji']:,}".replace(",", ".")

    # Tabel ringkasan utama
    tabelRingkasan = [
        ["Total Karyawan Aktif", f"{len(listKaryawan)} orang"],
        ["Total Payroll", totalGajiStr],
        ["Rata-rata Gaji", rataRataStr],
        ["Gaji Tertinggi", f"{gajiMax['nama']} ({gajiMaxStr})"],
        ["Gaji Terendah", f"{gajiMin['nama']} ({gajiMinStr})"]
    ]

    print('\n================ LAPORAN STATISTIK PAYROLL ================')
    print(tabulate(tabelRingkasan, headers=["Metrik", "Nilai"], tablefmt="fancy_grid"))

    # Tabel distribusi divisi
    tabelDivisi = [[div, f"{count} orang"] for div, count in divisiCount.items()]
    print('\nBreakdown Karyawan Per Divisi:')
    print(tabulate(tabelDivisi, headers=["Nama Divisi", "Jumlah Karyawan"], tablefmt="fancy_grid"))


# 6. Menu Utama
def menuUtama():
    while True:
        print('''
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
8. Exit Program''')
        
        menuOption = inputAngka('Masukkan angka yang ingin dijalankan (1-8) : ')

        if menuOption is None or menuOption == 8:
            print('Terima kasih telah menggunakan program ini!')
            break
        elif menuOption == 1:
            menuRead()
        elif menuOption == 2:
            menuCreate()
        elif menuOption == 3:
            menuUpdate()
        elif menuOption == 4:
            menuDelete()
        elif menuOption == 5:
            printResign()
        elif menuOption == 6:
            restoreKaryawan()
        elif menuOption == 7:
            menuStatistik()
        else:
            print('Pilihan menu tidak valid! Silakan masukkan angka 1-8.')

# Run Program
menuUtama()
