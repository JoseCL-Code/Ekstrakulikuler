#include <iostream>
using namespace std;

int main(){
	int angka1, angka2;
	char operasi;

	cout << "Masukkan angka pertama: ";
	cin >> angka1;
	cout << "Masukan operator (+, -, *, /)";
	cin >> operasi;
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
			cout << angka1 / angka2 << endl;
			break;
		default:
			cout << "Operasi tidak valid" << endl;
	}
	}
	return 0;
}
