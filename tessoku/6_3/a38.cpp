#include <bits/stdc++.h>

using namespace std;

// ２日目３日目に関しては２２時間以下と１６時間以下で被っているが１６時間以下でないと怒られてしまうためそっちを採用
int main() {
  // input
  ifstream in("a38.txt");
  cin.rdbuf(in.rdbuf());

  int D, N;
  cin >> D >> N;
  int L[N + 1], R[N + 1], H[N + 1];
  for (int i = 1; i <= N; ++i) cin >> L[i] >> R[i] >> H[i];

  int lim[D + 1];
  for (int i = 1; i <= D; ++i) lim[i] = 24;

  for (int i = 1; i <= N; ++i) {
    for (int j = L[i]; j <= R[i]; ++j) { lim[j] = min(lim[j], H[i]); }
  }

  int ans = 0;
  for (int i = 1; i <= D; ++i) ans += lim[i];

  cout << ans << endl;

  return 0;
}