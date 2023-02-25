#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a35.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  long long dp[N + 1][N + 1]{};
  for (int i = 1; i <= N; ++i) { cin >> dp[N][i]; }
  for (int i = N - 1; i > 0; --i) {
    for (int j = 1; j <= N; ++j) {
      if (i % 2 == 1) dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]);
      if (i % 2 == 0) dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]);
    }
  }

  cout << dp[1][1] << endl;

  return 0;
}