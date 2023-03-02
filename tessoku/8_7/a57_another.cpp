#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a57.txt");
  cin.rdbuf(in.rdbuf());

  int N, Q;
  cin >> N >> Q;
  int A[N + 1];
  for (int i = 1; i <= N; ++i) { cin >> A[i]; }
  int x[Q + 1], y[Q + 1];
  for (int i = 1; i <= Q; ++i) { cin >> x[i] >> y[i]; }

  long long dp[30][N + 1];
  for (int j = 1; j <= N; ++j) { dp[0][j] = A[j]; }

  for (int d = 1; d < 30; ++d) {
    for (int j = 1; j <= N; ++j) { dp[d][j] = dp[d - 1][dp[d - 1][j]]; }
  }

  for (int i = 1; i <= Q; ++i) {
    int pos = x[i];
    for (int d = 29; d >= 0; --d) {
      if (y[i] & (1 << d)) { pos = dp[d][pos]; }
    }
    cout << pos << endl;
  }

  return 0;
}