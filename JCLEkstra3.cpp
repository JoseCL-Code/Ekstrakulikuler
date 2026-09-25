#include <iostream>

using namespace std;

int main(){
	string nama,umur,agama,alamat;
	//Program Input Data
	cout << "Menu Input Data Siswa" << endl;
	cout << "Masukan Biodata Anda" << endl;
	cout << "Nama : ";
	getline(cin, nama);
	
	cout << "Umur : ";
	getline(cin, umur);

	cout << "Agama : ";
	getline(cin, agama);
	
	cout << "Alamat : ";
	
	getline(cin, alamat);
	/*Hasil Tampilan Biodata Mahasiswa 
	Universitas Konoha*/
	cout << endl;
	cout << "Menu Tampil" << endl;
	cout << "Biodata Anda" << endl;
	cout << "Nama : " << nama << endl;
	cout << "Umur : " << umur << endl;
	cout << "Agama : " << agama << endl;
	cout << "Alamat : " << alamat << endl;
	return 0;
}
