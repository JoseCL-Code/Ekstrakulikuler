import random

def game_tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    nyawa = 5
    percobaan = 0


    print("Selamat datang di permainan Tebak Angka!")
    print("Saya sudah memilih angka antara 1 hingga 100. Coba tebak Angkanya!")

    while nyawa > 0:
        try:
            tebakan = int(input("Masukkan tebakkanmu: "))
            percobaan += 1
            nyawa -= 1
            if tebakan < angka_rahasia:    
                print("Terlalu rendah, coba angka yang lebih besar.")
                print(f"Sisa nyawa anda = {nyawa}.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi, coba angka yang lebih kecil.")
                print(f"Sisa nyawa anda = {nyawa}.")
            else:
                print(f"Selamat! Kau berhasil menebak angkanya dalam {percobaan} percobaan dengan sisa nyawa {nyawa}.")
                break
            if nyawa == 0:
                print(f"Kamu kehabisan nyawa! Angka yang benar = {angka_rahasia}")
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

game_tebak_angka()