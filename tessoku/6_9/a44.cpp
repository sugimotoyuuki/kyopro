#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a44.txt");
  cin.rdbuf(in.rdbuf());

  int N, Q;
  cin >> N >> Q;

  int A[N + 1];
  int t, x, y, id;
  bool reverse = false;
  for (int i = 1; i <= N; ++i) { A[i] = i; }
  for (int i = 1; i <= Q; ++i) {
    cin >> t;
    if (t == 1) {
      cin >> x >> y;
      if (reverse == false) {
        A[x] = y;
      } else {
        A[N + 1 - x] = y;
      }
    }
    if (t == 2) { reverse = !reverse; }
    if (t == 3) {
      cin >> x;
      if (reverse == false) {
        cout << A[x] << endl;
      } else {
        cout << A[N + 1 - x] << endl;
      }
    }
  }

  return 0;
}