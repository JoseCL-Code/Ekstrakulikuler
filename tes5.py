class Kendaraan:
    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis
        self.merk = merk
        self.tahun = tahun


    def info(self):
        return f"Jenis : {self.jenis}, Merk : {self.merk}, Tahun : {self.tahun}"
# Membuat objek dari class "Kendaraan"
mobil1 = Kendaraan("Mobil", "Toyota", 2020)
mobil2 = Kendaraan("Mobil", "Honda", 2022)

# Mengakses informasi objek
print("Informasi Mobil 1:", mobil1.info())
print("Informasi Mobil 2", mobil2.info())