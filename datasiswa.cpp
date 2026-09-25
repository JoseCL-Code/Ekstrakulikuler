#include <vector>
#include <iostream>
using namespace std;

int main(){
    int jumSiswa;
	cout << "Masukkan Jumlah Siswa Kelas XI.4: ";
    cin >> jumSiswa;
    cin.ignore(); // Menghilangkan newline dari input sebelumnya
    
    for (int i = 0; i < jumSiswa; i++){
    	string nama;
    	string j_kel;
    	string nis;
    	int nilai;
    	
    	cout << "\nData Siswa ke-" << i + 1 << endl;
    	cout << "Masukkan Nama: ";
    	getline(cin, nama);
    	cout << "Masukkan Jenis Kelamin (L/P): ";
    	cin >> j_kel;
    	cout << "Masukkan NIS: ";
    	cin >> nis;
    	cout << "Masukkan Nilai: ";
    	cin >> nilai;
    	cin.ignore(); // Menghilangkan newline dari input nilai
    	
    	// Menampilan identitas siswa
    	cout << "\nIdentitas Siswa Kelas XI.4" << endl;
    	cout << "Nama          : " << nama << endl;
    	cout << "Jenis Kelamin : " << (j_kel == "L"  ? "Laki-Laki" : "Perempuan") << endl;
    	cout << "NIS           : " << nis << endl;
    	
    	// Kondisi if majemuk untuk menentukan kategori nilai
    	cout << "Kategori Nilai: ";
    	if(nilai >= 90 & nilai <= 100){
	       cout << "A (Sangat Baik)" << endl;}
	    else if(nilai >= 80 & nilai < 90){
	       cout << "B (Baik)" << endl;}
	    else if(nilai >= 70 & nilai < 80){
	       cout << "C (Cukup)" << endl;}
	    else if(nilai >= 60 & nilai < 70){
	       cout << "D (Kurang)" << endl;}
	    else if(nilai >= 0 & nilai < 60){
	       cout << "E (Sangat Kurang)" << endl;}
	    else {
		   cout << "NIlai tidak valid." << endl;
	}
}
return 0;
}
    
