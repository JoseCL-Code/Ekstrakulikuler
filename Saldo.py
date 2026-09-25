def cek_saldo(saldo):
    print(f"Saldo anda saat ini: Rp{saldo}")

def tarik_tunai(saldo, jumlah):
    if jumlah <= saldo:
        saldo -= jumlah
        print(
            f"Anda berhasil tarik tunai sebesar Rp{jumlah}. Sisa saldo Anda : Rp{saldo}")
    else:
        print("Saldo Anda tidak cukup untuk penarikan tunai")


def setor_tunai(saldo, jumlah):
    saldo += jumlah
    print(
        f"Anda berhasil menyetor tunai sebesar Rp:{jumlah}. Sisa saldo anda: Rp{saldo}")
saldo_awal = 2500000 #Saldo awal akun
saldo = saldo_awal


while True:
    print("\n=======Mesin ATM=======")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

    pilihan =  int(input("Pilihan Layanan(1/2/3/4): "))

    if pilihan == 1:
        cek_saldo(saldo)
    elif pilihan == 2:
        jumlah_tarik = int(input("Masukkan jumlah uang yang mau ditaik: "))
        tarik_tunai(saldo, jumlah_tarik)
    elif pilihan == 3: 
        jumlah_setor = int(input("Masukkan jumlah uang yang mau disetor: "))
        setor_tunai(saldo, jumlah_setor)
    elif pilihan == 4:
        print("Terima kasih sudah menggunakan layanan ATM.")
        break
    else:
        print("Plihan tidak valid. Silakan pilih lagi.")
