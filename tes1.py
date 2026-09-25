print("Pilih Operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")    
print("4. Pembagian")
print("5. Keluar")

while True:
    pilihan = input("Pilihan Operasi(1/2/3/4/5): ")
    if pilihan == "1":
        first = float(input("Masukkan angka pertama: "))
        second = float(input("Masukkan angka kedua: "))
        jawaban = first + second
        print(f"Hasil: {jawaban}")
    elif pilihan == "2":
        first = float(input("Masukkan angka pertama: "))
        second = float(input("Masukkan angka kedua: "))   
        jawaban = first - second
        print(f"Hasil: {jawaban}")
    elif pilihan == "3":
        first = float(input("Masukkan angka pertama: "))
        second = float(input("Masukkan angka kedua: "))
        jawaban = first * second
        print(f"Hasil: {jawaban}")
    elif pilihan == "4":
        first = float(input("Masukkan angka pertama: "))
        second = float(input("Masukkan angka kedua: "))
        jawaban = first / second
        print(f"Hasil: {jawaban}")
    elif pilihan == "5":
        print("Terima Kasih")
        break
    else:
        print("Pilihan tidak valid. Silahkan pilih lagi")