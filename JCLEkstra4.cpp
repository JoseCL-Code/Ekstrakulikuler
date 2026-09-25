#include <iostream>

using namespace std;

int main(){
	
	//deklarasi tipe data variabel
	string nama;
	int umur;
	char jenis_kelamin;
	
	// --- proses input --- 
	cout << "Siapakah Namamu?" << endl;
	cout << "Jawab: ";
	// menyimpan data ke variabel
	getline(cin, nama);
	
	cout << "Berapa Umurmu?" << endl;
	cout << "Jawab: ";
	// menyimpan data ke variabel
	cin >> umur;
	
	cout << "Jenis Kelamin [L/P]:";
    // menyimpan data ke variabel
	cin >> jenis_kelamin;
	
	// --- proses output ---
	cout << "Salam kenal, " << nama << " Sekarang engkau berusia ";
	cout << umur << " dan kau berjenis kelamin "<< jenis_kelamin;
	
	return 0;
}
