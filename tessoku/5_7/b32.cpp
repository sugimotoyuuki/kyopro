#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b32.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  int a[K + 1];
  for (int i = 1; i <= K; ++i) cin >> a[i];

  bool vict[N + 1];
  for (int i = 0; i <= N; ++i) vict[i] = false;

  for (int i = 0; i <= N; ++i) {
    for (int j = 1; j <= K; ++j) {
      if (vict[i] == true) continue;
      if (i >= a[j] && vict[i - a[j]] == false) {
        vict[i] = true;
      } else {
        vict[i] = false;
      }
    }
  }

  for (int i = 0; i <= N; ++i) cout << vict[i] << endl;

  if (vict[N]) {
    cout << "First" << endl;
  } else {
    cout << "Second" << endl;
  }

  return 0;
}