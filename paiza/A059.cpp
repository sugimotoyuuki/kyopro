#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("A059.txt");
  cin.rdbuf(in.rdbuf());

  int N, x;
  cin >> N >> x;
  int w[N + 1];
  int r[N + 1];
  for (int i = 1; i <= N; ++i) { cin >> w[i] >> r[i]; }

  int dp[N + 2][x + 2];
  for (int i = 0; i <= N; ++i) {
    for (int j = 0; j < x; ++j) { dp[i][j] = -10000000; }
  }

  dp[0][0] = 0;

  for (int i = 1; i <= N; ++i) {
    for (int j = 0; j < x; ++j) {
      if (j < w[i]) {
        dp[i][j] = dp[i - 1][j];
      } else {
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + r[i]);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < x; ++i) ans = max(ans, dp[N][i]);
  cout << ans << endl;

  return 0;
}