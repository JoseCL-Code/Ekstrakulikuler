#include <iostream>
#include <cmath> // Untuk fungsi sqrt dan pow
using namespace std;

int main(){
	double angka1, angka2; // Ubah menjadi double untuk mendukung hasil akar dan pangkat
	char operasi;
	
	cout << "Masukan operator (+, -, *, /, ^, r): ";
	cin >> operasi;
	
	if (operasi == 'r'){
		cout << "Masukakan angka: ";
		cin >> angka1;
		if(angka1 < 0){
			cout << "Tidak dapat mengambil akar dari angka negatif." << endl;
		}else {
			cout << "Akar dari " << angka1 << "adalah " << sqrt(angka1) << endl;
		}
	}else{
	cout << "Masukkan angka pertama: ";
	cin >> angka1;
    cout << "Masukkan angka kedua: ";
	cin >> angka2;
	
	switch (operasi){
		case '+':
			cout << angka1 + angka2 << endl;
			break;
		case '-':
			cout << angka1 - angka2 << endl;
		    break;
		case '*':
			cout << angka1 * angka2 << endl;
			break;
		case '/':
			if (angka2 !=0) {
			cout << angka1 / angka2 << endl;
		}else {
			cout << "Tidak dapat membagi dengan nol." << endl;
		}
			break;
		case '^':
			cout << angka1 << "Pangkat "<< angka2 << "adalah " << pow(angka1, angka2) << endl;
			break;
		default:
			cout << "Operasi tidak valid" << endl;
	}}
	return 0;
}
