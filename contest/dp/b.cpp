#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  int h[N + 1];
  for (int i = 1; i <= N; ++i) cin >> h[i];

  int dp[N + 1]{};
  for (int i = 2; i <= N; ++i) {
    int minvalue = 2e5;
    for (int j = 1; j <= K; ++j) {
      if (i - j >= 1) {
        minvalue = min(minvalue, dp[i - j] + abs(h[i - j] - h[i]));
      }
    }
    dp[i] = minvalue;
  }

  for (int i = 1; i <= N; ++i) { cout << dp[i] << endl; }

  cout << dp[N] << endl;
  return 0;
}