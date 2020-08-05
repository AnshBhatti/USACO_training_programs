/*
ID: anshvbh1
LANG: C++11
PROB: milk3
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
int x, y, z;
bool search_space[100][100];
vector<int>ans;

void dfs(int a, int b, int c) {
	if (search_space[a][b])
		return;
	else
		search_space[a][b] = true;
	if (a == 0)
		ans.push_back(c);
	if (a > 0 && b < y)
		dfs(max(0, a + b - y), min(y, a + b), c);
	if (a > 0 && z < c)
		dfs(max(0, a + c - z), b, min(z, a + c));
	if (b > 0 && a < x)
		dfs(min(x, a + b), max(0, a + b - x), c);
	if (b > 0 && c < z)
		dfs(a, max(0, b + c - z), min(z, b + c));
	if (c > 0 && a < x)
		dfs(min(a + c, x), b, max(a + c - x, 0));
	if (c > 0 && b < y)
		dfs(a, min(y, c + b), max(c + b - y, 0));
}

int main() {
	ifstream in("milk3.in");
	ofstream out("milk3.out");
	in >> x >> y >> z;
	dfs(0, 0, z);
	sort(ans.begin(), ans.end());
	for (int i = 0; i < ans.size(); i++) {
		if (i==ans.size()-1) out << ans[i] << endl;
		else out << ans[i] << ' ';
	}
}