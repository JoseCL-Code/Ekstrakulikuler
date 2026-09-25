#include <iostream>
#include <string>

using namespace std;

struct Student {
	string name;
	string major;
	double grade;
};

int main(){
	const int MAX_STUDENTS = 100;
	Student students[MAX_STUDENTS];
	int studentCount = 0;
	int choice;
	
	while (true) {
		cout << "\n--- Sistem Manajemen Nilai Mahasiswa ---\n";
		cout << "1. Tambah Mahasiswa\n";
		cout << "2. Tampilkan Data Mahasiswa\n";
		cout << "3. Keluar\n";
		cout << "Pilih Opsi: ";
		cin >> choice;
		
		switch (choice) {
			case 1:
				if(studentCount < MAX_STUDENTS){
					cout << "Masukkan nama mahasiswa: ";
					cin >> students[studentCount].name;
					cout << "Masukakan jurusan mahasiswa: ";
					cin >> students[studentCount].major;
					cout << "Masukkan nilai mahasiswa: ";
					cin >> students[studentCount].grade;
					studentCount++;
				}else {
					cout << "Data mahasiswa sudah penuh!" << endl;
				}
				break;
			case 2:
				cout << "\nDaftar Mahasiswa\n";
				for (int i = 0; i < studentCount; i++) {
					cout << "Nama: " << students[i].name
					     << ", Jurusan: " << students[i].major
					     << ", Nilai: " << students[i].grade << endl;
				}
				break;
			case 3:
				cout << "Terima kasih! Sampai jumpa!" << endl;
				return 0;
			default:
				cout << "Pilihan tidak valid! Silahkan coba lagi." << endl;
		}
	}
	return 0;
}
