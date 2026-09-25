#include <iostream>
using namespace std;

// Deklarasi variabel global
double saldo = 0; // Saldo awal

// Fungsi untuk menampilkan saldo saat ini
void cekSaldo(){
	cout << "Saldo Anda saat ini adalah: Rp " << saldo << endl;
}

// Fungsi untuk menambah saldo(menabung)
void menabung(){
	double jumlah;
	cout << "Masukkan jumlah uang yang ingin ditabung: Rp ";
	cin >> jumlah;
	if(jumlah > 0){
		saldo += jumlah;
		cout << "Berhasil menabung! Saldo Anda sekarang: Rp " << saldo << endl;
	}else{
		cout << "Jumlah tidak valid. Masukkan Jumlah yang benar." << endl;
	}
}

// Fungsi untuk menarik saldo
void tarik(){
	double jumlah;
	cout << "Masukkan jumlah uang yang ingin ditarik: Rp ";
	cin >> jumlah;
	if(jumlah > 0){
		saldo -= jumlah;
		cout << "Berhasil menarik! Saldo Anda Sekarang: Rp " << saldo << endl;
	}else{
		cout << "Jumlah saldo Anda kurang. Masukkan jumlah yang benar." << endl;
	}
}

int main(){
 	int pilihan;
 	
 	cout << "Selamat datang di Program Menabung Sederhana!" << endl;
 	
 	// Menu utama
 	do{
 		cout << "\nMenu:\n";
 		cout << "1. Cek Saldo\n";
 		cout << "2. Menabung\n";
 		cout << "3. Tarik Saldo\n";
 		cout << "4. Keluar\n";
 		cout << "Pilih opsi: ";
 		cin >> pilihan;
 		
 		switch (pilihan){
 			case 1:
 				cekSaldo();
 				break;
 			case 2:
 				menabung();
 				break;
 			case 3:
 				tarik();
 				break;
 			case 4:
 				cout << "Terima kasih telah menggunakan layanan nabung kami!" << endl;
 				break;
 			default:
 				cout << "Opsi tidak valid. Silahkan coba lagi." << endl;
		 }
	 }while(pilihan != 4);
	 return 0;
 }
