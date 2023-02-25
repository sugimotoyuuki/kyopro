#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b44.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  int A[N + 1][N + 1];
  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= N; ++j) { cin >> A[i][j]; }
  }

  int Q;
  cin >> Q;

  int r[N + 1];
  for (int i = 1; i <= N; ++i) { r[i] = i; }
  int t, x, y, tmp;
  for (int i = 1; i <= Q; ++i) {
    cin >> t;
    if (t == 1) {
      cin >> x >> y;
      tmp = r[x];
      r[x] = r[y];
      r[y] = tmp;
    }
    if (t == 2) {
      cin >> x >> y;
      cout << A[r[x]][y] << endl;
    }
  }

  return 0;
}