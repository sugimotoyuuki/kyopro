#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a.txt");
  cin.rdbuf(in.rdbuf());

  int A[4][5];
  int a;
  for (int i = 1; i <= 3; ++i) {
    for (int j = 1; j <= 4; ++j) { cin >> A[i][j]; }
  }

  for (int i = 1; i <= 3; ++i) {
    for (int j = 2; j <= 4; ++j) { A[i][j] = A[i][j - 1] + A[i][j]; }
  }

  for (int j = 1; j <= 3; ++j) {
    for (int k = 1; k <= 4; ++k) { cout << A[j][k] << " "; }
    cout << endl;
  }
  cout << endl;

  for (int i = 2; i <= 3; ++i) {
    for (int j = 1; j <= 4; ++j) { A[i][j] = A[i - 1][j] + A[i][j]; }
  }

  for (int j = 1; j <= 3; ++j) {
    for (int k = 1; k <= 4; ++k) { cout << A[j][k] << " "; }
    cout << endl;
  }
  cout << endl;

  return 0;
}