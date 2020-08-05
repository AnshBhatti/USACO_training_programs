/*
ID: anshvbh1
LANG: C++
PROB: ariprog
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	ifstream in("ariprog.in");
	ofstream out("ariprog.out");
	bool arr1[125001], boolean, f;
	f = true;
	int a, b, s;
	vector<int>arr;
	int x, y;
	cin >> x >> y;
	for (int i = 0; i <= y; i++)
		for (int j = i; j <= y; j++) {
			int r = pow(j, 2) + pow(i, 2);
			if (arr1[r] != true)
				arr.push_back(r);
			arr1[r] = true;
		}
	int p = -1;
	int p1 = -1;
	sort(arr.begin(), arr.end());
	int g = arr.back();
	for (int cd = 1; cd < g / (x - 1) + 1; cd++) {
		a = 0;
		while (a < arr.size() && arr[a] <= g - cd * (x - 1)) {
			s = arr[a];
			b = 0;
			boolean = true;
			while (s + cd <= g && b < x - 1 && boolean) {
				s = s + cd;
				if (arr1[s]!=true)
					boolean = false;
				b++;
			}
			if (b != x - 1)
				boolean = false;
			if (boolean) {
				f = false;
				if (p!=arr[a] || p1!=cd)
					cout << arr[a] << ' ' << cd << endl;
				p = arr[a];
				p1 = cd;
			}
			a++;
		}
	}
	if (f)
		cout << "NONE\n";
}