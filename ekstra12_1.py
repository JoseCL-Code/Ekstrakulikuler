#Input/Masukan
nama_buku = input ("Masukan Nama Buku : ")
jumlah_buku = int(input("Masukan Jumlah Buku : "))
harga_satuan = int(input("Masukan Harga Satuan : "))

#Proses
harga = jumlah_buku * harga_satuan
ppn = harga * 0.10
harga_akhir = harga + ppn


#Output/Keluaran
print("\n========== RINCIAN PEMBELIAN ==========")
print("Nama Buku Yang di Beli : ",nama_buku )
print("Jumlah Buku Yang di Beli : ",jumlah_buku )
print("Harga Sebelum PPN : ",harga )
print("Total PPN : ", ppn)
print("Harga Setelah PPN :", harga_akhir )
if harga_akhir >= 750000:
    print("Bonus : Pena Cantik.")
elif harga_akhir >= 500000:
    print("Bonus : Kotak Pensil Cantik")
else:
    print("Bonus : Tidak Ada Bonus.")
print("\n==== TERIMA KASIH SUDAH BERBELANJA ====")