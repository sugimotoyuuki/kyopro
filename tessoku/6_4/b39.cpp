#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b39.txt");
  cin.rdbuf(in.rdbuf());

  int N, D;
  cin >> N >> D;
  int X[N + 1], Y[N + 1];
  for (int i = 1; i <= N; ++i) cin >> X[i] >> Y[i];

  bool selected[N + 1];
  for (int i = 1; i <= N; ++i) selected[i] = false;
  int ans = 0;
  for (int i = 1; i <= D; ++i) {
    int maxvalue = 0;
    int maxid = 0;
    for (int j = 1; j <= N; ++j) {
      if (selected[j] == true) continue;
      if (maxvalue < Y[j] && X[j] <= i) {
        maxvalue = Y[j];
        maxid = j;
      }
    }
    if (maxid != 0) {
      ans += maxvalue;
      selected[maxid] = true;
    }
  }

  cout << ans << endl;

  return 0;
}