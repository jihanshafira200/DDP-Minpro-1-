catatan = []

while True:
    print("\nSistem Catatan Kegiatan Sosial Mahasiswa")
    print("1. Tambah Kegiatan")
    print("2. Hapus Kegiatan")
    print("3. Lihat Semua Kegiatan")
    print("4. Keluar")

    pilihan = input("Pilih Menu (1/2/3/4): ")

    if pilihan == "1":
        judul = input("Masukkan Kegiatan: ")
        tanggal = input("Masukkan Tanggal Kegiatan: ")
        lokasi = input("Masukkan Lokasi Kegiatan: ")
        kegiatan = (judul, tanggal, lokasi)
        catatan.append(kegiatan)
        print("Kegiatan berhasil ditambahkan!")


    elif pilihan == "2":
        hapus = input("Masukkan Kegiatan yang Ingin Dihapus: ")
        for kegiatan in catatan:
            if kegiatan[0]== hapus:
                catatan.remove(kegiatan)
                print("Kegiatan berhasil dihapus.")
                
        else:
            print("Kegiatan tidak ditemukan.")

    elif pilihan == "3":
        if not catatan:
            print("Belum ada kegiatan.")
        else:
            print("Daftar Semua Kegiatan:")
            print(catatan)
        
    elif pilihan == "4":
        print("Keluar Dari Program.")
    
    else:
        print("Pilihan Tidak Valid.")