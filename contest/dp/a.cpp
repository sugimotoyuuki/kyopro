#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;
  long long h[N + 1];
  for (int i = 1; i <= N; ++i) cin >> h[i];

  int dp[N + 1]{};
  dp[2] = abs(h[2] - h[1]);
  for (int i = 3; i <= N; ++i) {
    dp[i] =
        min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]));
  }

  cout << dp[N] << endl;
  return 0;
}