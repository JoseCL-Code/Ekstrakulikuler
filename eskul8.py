# Simpan Data Siswa
data_siswa = {}

# Menambahkan data siswa


def tambah_siswa(nis, nama, kelas, program) :
    if nis not in data_siswa:
        data_siswa[nis]= {'nama': nama, 'kelas': kelas, 'program': program}
        print(f"Data siswa {nama} berhasil ditambahkan.")
    else:
        print((f"siswa dengan Nomor Induk Siswa {nis} sudah ada."))

#Mencari Siswa berdasarkan nama


def cari_siswa(nama):
    ditemukan = False
    for nis, info in data_siswa.items():
        if info ['nama'] == nama:
            print(f"Nomor Induk Siswa : {nis}")
            print(f"Nama : {info['nama']}")
            print(f"Kelas : {info['kelas']}")
            print(f"Program : {info['program']}")
            ditemukan = True
            break
        if not ditemukan:
            print(f"Siswa dengan nama {'nama'} tidak ditemukan.")

# Menampilkan daftar siswa


def tampilkan_semua_siswa():
    print("Daftar Semua Siswa")
    for nis, info in data_siswa.items():
        print(f"Nomor Induk Siswa: ")
        print(f"Nama :{info['nama']}")
        print(f"Kelas :{info['kelas']}")
        print(f"Program :{info['program']}")
        print("-" *20)

# Menu Utama


while True:
    print("\n M E N U")
    print("1. Tambah Siswa")
    print("2. Cari Siswa berdasarkan Nama")
    print("3. Tampilkan Daftar Semua Siswa")
    print("4. Keluar")

    pilihan = input("Pilih Menu (1/2/3/4): ")
    if pilihan == '1':
        nis = input("Masukan Nomor Induk Siswa: ")
        nama = input("Masukan Nama Siswa: ")
        kelas = input("Masukan Kelas Siswa: ")
        program = input("Masukan Program: ")
        tambah_siswa(nis, nama, kelas, program)
    elif pilihan == '2':
        nama = input("Masukan nama siswa yang dicari")
        cari_siswa(nama)
    elif pilihan == '3':
        tampilkan_semua_siswa()
    elif pilihan == '4':
        break
    else:
        print("Pilihan amda tidak valid, silahkan coba lagi")