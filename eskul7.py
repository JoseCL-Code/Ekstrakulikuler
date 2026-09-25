saldo_awal = 1000 #Saldo awal akun
saldo = saldo_awal
def cek_saldo(saldo):
    print(f"Saldo anda saat ini adalah: Rp{saldo}")
def tarik_tunai(jumlah):
    if jumlah <= saldo_awal:
        saldos = saldo - jumlah
        print (saldos)
    else: 
        print("Saldo Anda tidak cukup untuk tarik tunai")

def setor_tunai(saldo,jumlah):
    saldo += jumlah
    print(
        f"Anda berhasil menyetor tunai sebesar Rp:{jumlah}")

while True:
    print("===ATM===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")


    pilihan = int(input("Pilihan Layanan(1/2/3/4): "))
    if pilihan ==1:
        cek_saldo(saldo)
    elif pilihan ==2:
        jumlah_tarik = int(input("Masukan Jumlah uang yang mau ditarik: "))
        tarik_tunai(jumlah_tarik)
    elif pilihan ==3:
            jumlah_setor = int(input("Masukan Jumlah uang yang mau disetor: "))
            setor_tunai(saldo, jumlah_setor)
    elif pilihan ==4:
            print("Terima Kasih Sudah Menggunakan Layanan Kami")
            break
    else:
        print("Pilihan tidak valid. Silahkan pilih lagi")