data_product = {
    1:"Nike",
    2:"Adidas",
    3:"Reebok",
    4:"Diadora",
    5:"Sketchers"
}
daftar_harga = {
    1:2000000,
    2:1800000,
    3:1500000,
    4:800000,
    5:750000
}

dict_trx = {}
daftar_metode = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit"
}
print("======================= LIST PRODUK =======================")
for i in data_product:
    print("ID Product : ",i, "\t Nama Produk", data_product[i], "\t Harga Product : ",daftar_harga[i])
    pilih_id = int(input("Pilih ID Product :"))
    if pilih_id in data_product:
        pilih_beli = input ("Ingin Membeli ? (Y/N) :")
        if pilih_beli == "y" or pilih_beli == "Y":
             nama_penerima = input("Nama Penerima : ")
        alamat_penerima = input("Alamat Penerima : ")
        telepon = input("No HP : ")
        kurir = input("Kurir Pengirim : ")
        dict_try = {
            "Nama Penerima ": nama_penerima,
            "Alamat Penerima ": alamat_penerima,
            "No HP ": telepon,
            "Kurir Pengirim ": kurir,
            "Product ID ": data_product
        }
    else:
        pass
    if len(dict_trx) > 0:
        print("======================= METODE PEMBAYARAN =======================")
        for i in daftar_metode_pembayaran:
            print("ID :,i, ""\t Metode Pembayaran : ", daftar_metode_pembayaran(i))
        pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
        if pilih_metode in daftar_metode:
             print("Nama Penerima : ",dict_trx("Nama penerima"))
        print("Alamat Penerima : ",dict_trx("Alamat Penerima"))
        print("No HP : ",dict_trx("No HP"))
        print("Kurir Pengiriman : ",dict_trx("Kurir Pengirim"))
        print("Product : ",data_product("pilih_id"))
        print("Harga : ",daftar_harga("pilih_id"))
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah kamu ingin melakukan pembayaran? (Y/N):")
        if konfirmasi == "y" or konfirmasi == "y" :
            print("Anda sudah berhasil melakukan pembayaran")
        else:
            pass
    else:
        print("ID metode pembayaran tidak tersedia")
else:
    print("ID Product tidak tersedia") 