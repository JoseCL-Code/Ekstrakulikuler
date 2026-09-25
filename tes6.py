class Kursus:
    def __init__(self, kode, nama, durasi, biaya):
        self.kode = kode
        self.nama = nama
        self.durasi =durasi
        self.biaya = biaya
        self.peserta = []

    def tambah_peserta(self, nama_peserta):
        self.peserta.append(nama_peserta)
        print(f"{nama_peserta} telah mendaftar ke kursus {self.nama}")

    def lihat_peserta(self):
        print(f"Daftar Peserta Kursus {self.nama}:")
        for peserta in self.peserta:
            print(peserta)
            
class ProgramKursus:
    def __init__(self):
        self.kursus_list = []

    def tambah_kursus(self, kode, nama, durasi, biaya):
        kursus = Kursus(kode, nama, durasi, biaya)
        self.kursus_list.append(kursus)
        print(f"Kursus {nama} ditambahkan.")

    def lihat_kursus(self):
        print("Daftar Kursus")
        for kursus in self.kursus_list:
            print(f"Kode: {kursus.kode} - {kursus.nama} - Durasi:{kursus.durasi} jam - Biaya: {kursus.biaya}")

    def daftar_peserta(self, kode_kursus, nama_peserta):
        for kursus in self.kursus_list:
            if kursus.kode == kode_kursus:
                kursus.tambah_peserta(nama_peserta)
                return
            print(f"Kursus dengan kode {kode_kursus} tidak ditemukan")

    def lihat_peserta_kursus(self, kode_kursus):
        for kursus in self.kursus_list:
            if kursus.kode == kode_kursus:
                kursus.lihat_peserta()
                return
            print(f"Kursus dengan kode {kode_kursus} tidak ditemukan. ")

def main():
        program_kursus = ProgramKursus()

        while True:
            print("\nMenu Program Kursus:")
            print("1. Tambah Kursus")
            print("2. Lihat Kursus")
            print("3. Daftar Peserta Kursus")
            print("4. Lihat Peserta Kursus")
            print("5. Exit")

            pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

            if pilihan == "1":
                kode = input("Masukkan kode kursus: ")
                nama = input("Masukkan nama kursus: ")
                durasi = int(input("Masukkan durasi kursus (jam): "))
                biaya = float(input("Masukkan biaya kursus: "))
                program_kursus.tambah_kursus(kode, nama, durasi, biaya)
            elif pilihan == "2":
                program_kursus.lihat_kursus()
            elif pilihan == "3":
                kode_kursus = input("Masukkan kode kursus yang diikuti: ")
                nama_peserta = input("Masukkan nama peserta: ")
                program_kursus.daftar_peserta(kode_kursus, nama_peserta)
            elif pilihan == "4":
                kode_kursus = input("Masukkan kode kursus yang ingin dilihat pesertanya")
                program_kursus.lihat_peserta_kursus(kode_kursus)
            elif pilihan == "5":
                print("Terima kasih. Keluar dari Aplikasi.")
                break
            else:
                print("Pilihan tidak Valid. Silahkan coba lagi") 

if __name__ == "__main__":
    main()