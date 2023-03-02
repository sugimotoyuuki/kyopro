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

  for (int i = 1; i < 30; ++i) {
    for (int j = 1; j <= N; ++j) { dp[i][j] = dp[i - 1][dp[i - 1][j]]; }
  }

  for (int i = 1; i <= Q; ++i) {
    vector<int> G = {};
    int div = y[i];
    int id = 0;
    while (div != 0) {
      if (div % 2 == 1) { G.push_back(id); }
      div /= 2;
      ++id;
    }
    int pos = x[i];
    for (int j = G.size() - 1; j >= 0; --j) { pos = dp[G[j]][pos]; }
    cout << pos << endl;
  }

  return 0;
}