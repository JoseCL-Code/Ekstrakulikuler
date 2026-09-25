7#inisiasi varibel
operator = str(input ("Nama Operator : "))
nama_pelanggan = str(input ("Nama Pelanggan : "))
alamat_pelanggan = str(input ("Alamat pelanggan : "))
no_hp = str(input ("Nomor HP : "))
berat_barang = int(input ("Berat : "))
biaya_perkilo = 5000 # per kilogram

#Hitung total biaya laundry
total_biaya_laundry = biaya_perkilo * berat_barang

#Cetak detail laundry
print("================================")
print("JASA LAUNDRY AUDREY")
print("================================")
print("Nama operator : " + operator)
print("Nama pelanggan : " + nama_pelanggan)
print("Alamat pelanggan : " + nama_pelanggan)
print("Nomor Whatsapp : " + no_hp)
print("Berat Barang : " + str(berat_barang) + "Kg")
print("Biaya per Kilogram : Rp. " + str(biaya_perkilo))
print("Total Biaya Laundry : Rp. " + str(total_biaya_laundry))
print("================================")