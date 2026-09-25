# inisiasi variabel
operator = str(input ("Nama Operator : ?"))
nama_pelanggan = str(input("Nama Pelanggan : ?"))
alamat_pelanggan = str(input ("Alamat Pelanggan : ?"))
no_hp = str(input ("Nomor HP : ?"))
berat_barang = float(input ("Berat : ?"))
biaya_perkilo = 5000 # harga per kilogram

# Hitung total biaya laundry
total_biaya_laundry = biaya_perkilo * berat_barang

# Cetak detail laundry
print("=================================")
print(f"CV. Clean Jasa Pencucian Pakaian")
print(f"================================")
print(f"Nama Operator : " + operator)
print(f"Nama Pelanggan : " + nama_pelanggan)
print(f"Alamat Pelanggan : " + alamat_pelanggan)
print(f"No. Whatsapp : " + no_hp)
print(f"Berat Barang : " + str(berat_barang) + " kg")
print(f"Biaya Per Kilogram : Rp." + str(biaya_perkilo))
print(f"Total Biaya Laundry : Rp." + str(total_biaya_laundry))
print(f"================================")
