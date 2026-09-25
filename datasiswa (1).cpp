#include <iostream>
#include <vector>
#include <string>
#include <limits> // Tambahkan pustaka ini untuk menggunakan numeric_limits

using namespace std;

// Struktur untuk menyimpan data siswa
struct Siswa{
	int id;
	string nama;
	string kelas;
	string jurusan;
};

// Fungsi untuk menambah data siswa
void tambahSiswa(vector<Siswa>& daftarSiswa, int id,const string& nama,const string& kelas,const string& jurusan){
	Siswa siswa = {id, nama, kelas, jurusan};
	daftarSiswa.push_back(siswa);
	cout << "Siswa " << nama << " berhasil ditambahkan.\n";
}

// Fungsi untuk menampilkan data semua siswa
void tampilkanDataSiswa(const vector<Siswa>& daftarSiswa){
	cout << "\nDaftar Data Siswa: \n";
	cout << "ID\tNama\tKelas\tJurusan\n";
	cout << "==================================\n";
	for(size_t i = 0; i < daftarSiswa.size(); i++){
		cout << daftarSiswa[i].id << "\t" << daftarSiswa[i].nama << "\t"
		<< daftarSiswa[i].kelas << "\t" << daftarSiswa[i].jurusan << "\t" << endl;
	}
}

// Fungsi untuk mencari siswa berdasarkan ID
void cariSiswa(const vector<Siswa>& daftarSiswa, int id){
	bool ditemukan = false;
	for(size_t i = 0; i < daftarSiswa.size(); i++){
		if (daftarSiswa[i].id == id){
			cout << "\nData Siswa Ditemukan:\n";
			cout << "ID: " << daftarSiswa[i].id << "\n";
			cout << "Nama: " << daftarSiswa[i].nama << "\n";
			cout << "Kelas: " << daftarSiswa[i].kelas << "\n";
			cout << "Jurusan: " << daftarSiswa[i].jurusan << "\n";
			ditemukan = true;
			break;	
		}
	}
	if (!ditemukan) {
		cout << "Siswa dengan ID " << id << " tidak ditemukan.\n";
	}
}

int main(){
	vector<Siswa> daftarSiswa;
	int pilihan;
	int id;
	string nama;
	string kelas;
	string jurusan;
	
	do {
		cout << "\n===== Program Data Siswa SMA =====\n";
		cout << "1. Tambah Data Siswa\n";
		cout << "2. Tampilkan Data Semua Siswa\n";
		cout << "3. Cari Data Siswa Berdasarkan ID\n";
		cout << "4. Keluar\n";
		cout << "Pilih menu: ";
		cin >> pilihan;
		
		// Validasi input untuk pilihan menu
		if(cin.fail()){
			cin.clear();// Reset status error
			cin.ignore(numeric_limits<streamsize>::max(), '\n');//Bersihkan input
			cout << "Input tidak valid, silahkan coba lagi.\n";
			continue;
		}
		
		switch(pilihan){
			case 1:
				cout << "Masukkan ID Siswa: ";
				cin >> id;
				cin.ignore();// Bersihkan karakter newline tersisa
				cout << "Masukkan Nama Siswa: ";
				getline(cin,nama);
				cout << "Masukkan Kelas Siswa: ";
				getline(cin,kelas);
				cout << "Masukkan Jurusan Siswa: ";
				getline(cin,jurusan);
				tambahSiswa(daftarSiswa, id, nama, kelas, jurusan);
				break;
				
			case 2:
				tampilkanDataSiswa(daftarSiswa);
				break;
				
			case 3: 
			    cout << "Masukkan ID Siswa yang ingin dicari: ";
			    cin >> id;
			    cariSiswa(daftarSiswa,id);
			    break;
			    
			case 4:
				cout << "Keluar dari program.\n";
				break;
			default:
				cout << "Pilihan tidak valid. Coba lagi.\n";
		}
	}while (pilihan !=4 );  
	return 0;
}
