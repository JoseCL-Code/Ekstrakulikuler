#include <iostream>
using namespace std;

int main(){
	string nama, kelas, alamat;
	cout << "Tuliskan Nama: ";
	getline(cin, nama);
	
	cout << "Tuliskan Kelas: ";
	getline(cin, kelas);
	
	cout << "Tuliskan Alamat: ";
	getline(cin, alamat);
	
	cout << "Hi " << nama;
	cout << ", Dari Kelas " << kelas;
	cout << ", Tempat Tinggal Di " << alamat;
	cout << ", Selamat Datang Di Club Informatika Xavega! " << endl;
	
	return 0;
}
