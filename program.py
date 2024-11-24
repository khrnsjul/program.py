def penukaran_koin(jumlah):
    
    koin = [2, 3, 5, 10, 15]
    
    jumlah_koin = {}
    
    
    for k in sorted(koin, reverse=True):
        while jumlah >= k:
            jumlah -= k
            if k in jumlah_koin:
                jumlah_koin[k] += 1
            else:
                jumlah_koin[k] = 1
    
    return jumlah_koin
jumlah_uang = int(input("Masukkan jumlah uang yang ingin ditukarkan: "))
hasil = penukaran_koin(jumlah_uang)
print("Koin yang digunakan untuk penukaran:")
for koin, jumlah in hasil.items():
    print(f"Koin {koin}: {jumlah} buah")
