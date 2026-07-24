# SOAL 1

filmAnda = input('Masukkan 5 Film Kesukaan anda dipisahkan dengan koma :')
filmTemanAnda = input('Masukkan 5 Film Kesukaan teman anda dipisahkan dengan koma :')

setAnda = set([film.strip() for film in filmAnda.split(',')])
setTemanAnda = set([film.strip() for film in filmTemanAnda.split(',')])

filmSama = setAnda.intersection(setTemanAnda)
jumlahSama = len(filmSama)

persentase = (jumlahSama / len(setAnda)) * 100

print(f'Kesukaan Film kalian yang sama sebesar {persentase}%')

# SOAL 2
listBuah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000]
]

while True:
    menuOption = int(input(f'''        Selamat datang di Pasar Buah

            List Menu:
            1. Menampilkan Daftar Buah
            2. Menambah Buah
            3. Menghapus Buah
            4. Membeli Buah
            5. Exit Program
            Masukkan angka yang ingin dijalankan : '''))
    
    if menuOption == 1:
        if listBuah:
            print(f"Index{'':<9}|Nama Buah{'':<6}|Stock Buah{'':<5}|Harga Buah{'':<5}|")
            for baris in range(len(listBuah)):
                print(f'{baris:<15}', end='')
                for menu in listBuah[baris]:
                    print(f'{menu:<15}|', end='')
                print('\t')
        else:
            print('Tidak terdapat Data Buah')

    elif menuOption == 2:
        namaBuahBaru = input('Masukkan Nama Buah      : ')
        stockBuahBaru = int(input('Masukkan Stock Buah     : '))
        hargaBuahBaru = int(input('Masukkan Harga Buah     : '))

        listBuah.append([namaBuahBaru, stockBuahBaru, hargaBuahBaru])
        if listBuah:
            print(f"Index{'':<9}|Nama Buah{'':<6}|Stock Buah{'':<5}|Harga Buah{'':<5}|")
            for baris in range(len(listBuah)):
                print(f'{baris:<15}', end='')
                for menu in listBuah[baris]:
                    print(f'{menu:<15}|', end='')
                print('\t')
        else:
            print('Tidak terdapat Data Buah')


    elif menuOption == 3:
        print('Daftar Buah')
        if listBuah:
            print(f"Index{'':<9}|Nama Buah{'':<6}|Stock Buah{'':<5}|Harga Buah{'':<5}|")
            for baris in range(len(listBuah)):
                print(f'{baris:<15}', end='')
                for menu in listBuah[baris]:
                    print(f'{menu:<15}|', end='')
                print('\t')
            
            indexHapus = int(input('Masukkan index buah yang ingin dihapus : '))
            if 0 <= indexHapus < len(listBuah):
                listBuah.pop(indexHapus)
            else:
                print('Index tidak ditemukan!')
        else:
            print('Tidak terdapat Data Buah')
        if listBuah:
            print(f"Index{'':<9}|Nama Buah{'':<6}|Stock Buah{'':<5}|Harga Buah{'':<5}|")
            for baris in range(len(listBuah)):
                print(f'{baris:<15}', end='')
                for menu in listBuah[baris]:
                    print(f'{menu:<15}|', end='')
                print('\t')
        else:
            print('Tidak terdapat Data Buah')

    elif menuOption == 4:
        print('Daftar Buah')
        if listBuah:
            print(f"Index{'':<9}|Nama Buah{'':<6}|Stock Buah{'':<5}|Harga Buah{'':<5}|")
            for baris in range(len(listBuah)):
                print(f'{baris:<15}', end='')
                for menu in listBuah[baris]:
                    print(f'{menu:<15}|', end='')
                print('\t')
        else:
            print('Tidak terdapat Data Buah')
            continue

        cart = []

        while True:
            indexBuahBeli = int(input('Masukkan index buah yang ingin dibeli : '))
            
            if indexBuahBeli < 0 or indexBuahBeli >= len(listBuah):
                print('Index buah tidak ditemukan!')
                continue
                
            qtyBuahBeli = int(input('Masukkan jumlah yang ingin dibeli : '))

            if qtyBuahBeli > listBuah[indexBuahBeli][1]:
                print(f'Stock tidak cukup, stock {listBuah[indexBuahBeli][0]} tinggal {listBuah[indexBuahBeli][1]}')
            else:
                cart.append([listBuah[indexBuahBeli][0], qtyBuahBeli, listBuah[indexBuahBeli][2], indexBuahBeli])
            
            print('Isi Cart :')
            print(f"Nama{'':<11}| Qty{'':<5}| Harga{'':<5}|")
            for item in cart:
                print(f"{item[0]:<15}| {item[1]:<8}| {item[2]:<10}|")
            
            lanjutBeli = input('Mau beli yang lain? (ya/tidak) = ').lower()
            if lanjutBeli != 'ya':
                break

        print('\nDaftar Belanja :')
        print(f"Nama{'':<11}| Qty{'':<5}| Harga{'':<5}| Total Harga{'':<5}")
        totalTagihan = 0
        
        for item in cart:
            totalPerBuah = item[1] * item[2]
            totalTagihan += totalPerBuah
            print(f"{item[0]:<15}| {item[1]:<8}| {item[2]:<10}| {totalPerBuah:<12}")
            
        print(f'Total Yang Harus Dibayar = {totalTagihan}')

        while True:
            bayar = int(input('Masukkan jumlah uang : '))

            if bayar < totalTagihan:
                print(f'Transaksi anda dibatalkan \nUangnya kurang sebesar {totalTagihan - bayar}\n')
                break 
            else:
                for item in cart:
                    idx = item[3]
                    qty = item[1]
                    listBuah[idx][1] -= qty
                    
                print('Terima kasih\n')
                if bayar > totalTagihan:
                    print(f'Uang kembali anda : {bayar - totalTagihan}')
                break
    elif menuOption == 5:
        print('Terima kasih telah berkunjung!')
        break
        
    else:
        print('Pilihan menu tidak valid!')