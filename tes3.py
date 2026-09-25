class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.pemain = []

    def tambah_pemain(self, pemain):
        self.pemain.append(pemain)

class TurnamenBasket:
    def __init__(self):
        self.daftar_tim = []

    def daftar_tim_baru(self, tim):
        self.daftar_tim.append(tim)

    def tampilkan_daftar_tim(self):
        print("Daftar Tim yang Terdaftar: ")
        for i, tim in enumerate(self.daftar_tim, start=1):
            print(f"{i}. {tim.nama}")

#Contoh penggunaan Program
turnamen = TurnamenBasket()

while True:
    print("\nMenu:")
    print("1. Daftarkan Tim Baru")
    print("2. Tampilkan Daftar Tim")
    print("3. Exit")

    pilihan = input("Masukan Pilihan (1/2/3): ")

    if pilihan == '1':
        nama_tim = input("Masukan nama tim: ")
        tim_baru = Tim(nama_tim)

        jumlah_pemain = int(input("Masukan jumlah pemain: "))
        for i in range(jumlah_pemain):
            nama_pemain = input(f"Masukan nama pemain {i+1}: ")
            tim_baru.tambah_pemain(nama_pemain)
    
        turnamen.daftar_tim_baru(tim_baru)
        print(f"Tim {nama_tim} berhasil didaftarkan")

    elif pilihan == '2':
        turnamen.tampilkan_daftar_tim()

    elif pilihan == '3':
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Masukan pilihan yang benar")