#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("B128.txt");
  cin.rdbuf(in.rdbuf());

  string num;
  cin >> num;

  int row = ((num.length() + 2) / 3) * 3;
  int col = (((num.length() - 1) % 3) + 1) * 3;

  char S[row][9];

  for (int j = 0; j < row; ++j) {
    for (int k = 0; k < 9; ++k) {
      for (int j = 0; j < row; ++j) {}
      S[j][k] = '.';
    }
  }

  for (int i = 0; i < num.length(); ++i) {
    int tmp = (int(num[i]) - 49);
    for (int j = 0; j <= tmp; ++j) {
      // cout << (i / 3) * 3 << " " << (i % 3) * 3 + (j % 3) << endl;
      S[(i / 3) * 3 + (j / 3)][(i % 3) * 3 + (j % 3)] = '#';
    }
  }

  for (int j = 0; j < row; ++j) {
    for (int k = 0; k < 9; ++k) {
      if (j >= row - 3 && k >= col) continue;
      cout << S[j][k];
    }
    cout << endl;
  }

  return 0;
}