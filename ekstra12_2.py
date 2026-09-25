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
    print(f"{produk[i]}-{terjual[i]} terjual @Rp{harga[i]}")

# === Pengenalan pola: cari prodyuk terlaris ===
index_terlaris = terjual.index(max(terjual))
print(f"\nProduk terlaris: {produk[index_terlaris]}"
      f"- {terjual[index_terlaris]} terjual")

# === Tambahan: produk kurang laris
index_kurang = terjual.index(min(terjual))
print(f"\nProduk kurang laris: {produk[index_kurang]}"
      f"- {terjual[index_kurang]} terjual")

# === Abstraksi: hitung total penjualan (omset) ===
total_penjualan = 0
for i in range(n):
    total_penjualan += harga[i] * terjual[i]

print("Total omset kantin: Rp", total_penjualan)

# Tambahan:rata-rata penjualan per produk
rata_rata = total_penjualan / n 
print("Rata-rata omset per produk: Rp", rata_rata)

# Tambahan: cari produk tertentu
cari = input("\nMasukkan nama produk yang ingin dicari: ")
if cari in produk:
    idx = produk.index(cari)
    print(f"Data produk: {produk[idx]} - {terjual[idx]} terjual @Rp{harga[idx]}")
else:
    print("Produk tidak ditemukan.")