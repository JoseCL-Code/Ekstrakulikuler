# Program Pengelolahan Data Kantin Sekolah

# Input Jumlah Produk
n = int(input("Masukkan jumlah produk yang dicatat : "))

# List Untuk Menyimpan Data
produk = []
harga = []
terjual = []

# Input Data Prodyuk
for i in range(n):
    print(f"\nData produk ke-{i+1}")
    produk.append(input("Nama produk: "))
    harga.append(int(input("Harga satuan: ")))
    terjual.append(int(input("Jumlah terjual: ")))

# === DEKOMPOSISI: Menampilkan data penjualan per produk ===
print("\n=== Data Penjualan Kantin Xavega ===")
for i in range(n):
    print(f"{produk[i]} - {terjual[i]} terjual @Rp{harga[i]}")

# Produk Paling Laris/Laku
index_terlaris = terjual.index(max(terjual))
print(f"\nProduk Terlaris : {produk[index_terlaris]}"
      f" - {terjual[index_terlaris]} terjual")

# Produk Kurang Laris/Laku
index_kurang = terjual.index(min(terjual))
print(f"\nProduk Kurang Laris : {produk[index_kurang]}"
      f" - {terjual[index_kurang]} terjual")

# Hitung Total Penjualan (Omset)
total_penjualan = 0
for i in range(n):
    total_penjualan += harga[i]*terjual[i]
    print("Total Omset Kantin : Rp", total_penjualan)