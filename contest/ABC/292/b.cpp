#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, Q;
  cin >> N >> Q;
  bool exit[N + 1];
  for (int i = 1; i <= N; ++i) { exit[i] = false; }
  int yello[N + 1];
  for (int i = 1; i <= N; ++i) { yello[i] = 0; }

  for (int i = 1; i <= N; ++i) {
    int q, p;
    cin >> q >> p;
    if (q == 1) {
      yello[p] += 1;
      if (yello[p] >= 2) { exit[p] = true; }
    } else if (q == 2) {
      exit[p] = true;
    } else if (q == 3) {
      if (exit[p]) {
        cout << "Yes" << endl;
      } else {
        cout << "No" << endl;
      }
    }
  }
  return 0;
}