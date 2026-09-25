print("          REZA COFFEE             ")
print("    Jl. Kapten Marzuki No.132  ")
print("================================")
name = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")
menu = {
    "mie dasyat" : 12000, 
     "kentang crispy" : 15000, 
     "capucino" : 10000, 
     "tea hijau" : 6000, 
     "milk cat" : 8000, 
}
print("===========DAFTAR MENU===========")
for i in menu:
    print("Daftar Menu : ",i, "\t Harga : ", menu[i])
print("Pembelian diatas Rp.100.000,- mendapatkan potongan 15%")
print("================================")
beli = input("Pilih Menu :")
jumlah = int(input("Jumlah Pesanan : "))
harga = jumlah * menu[beli]

if harga >100000:
    diskon = harga*15/100
    total = harga - diskon
else :
    total = harga
print("===========DETAIL PESANAN===========")
print("Menu yang dipesan :", beli)
print("Jumlah yang dipesan :", jumlah)
print("Total biaya :", harga)
print("Total yang harus dibayar :", total)
print("================================")