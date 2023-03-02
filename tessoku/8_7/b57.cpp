#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b57.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;

  vector<vector<int>> dp(21, vector<int>(N + 1, 0));
  for (int j = 1; j <= N; ++j) {
    dp[0][j] = j;
    int tmp = j;
    while (tmp > 0) {
      dp[0][j] -= tmp % 10;
      tmp /= 10;
    }
  }

  // for (int j = 1; j <= N; ++j) { cout << dp[0][j] << " "; }

  for (int i = 1; i <= 20; ++i) {
    for (int j = 1; j <= N; ++j) { dp[i][j] = dp[i - 1][dp[i - 1][j]]; }
  }

  for (int i = 1; i <= N; ++i) {
    int pos = i;
    for (int j = 20; j >= 0; --j) {
      if (K & (1 << j)) pos = dp[j][pos];
    }
    cout << pos << endl;
  }

  return 0;
}