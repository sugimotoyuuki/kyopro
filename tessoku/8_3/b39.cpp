#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b39.txt");
  cin.rdbuf(in.rdbuf());

  int N, D;
  cin >> N >> D;

  long long X[N + 1], Y[N + 1];
  vector<long long> G[D + 1]{};
  for (int i = 1; i <= N; ++i) {
    cin >> X[i] >> Y[i];
    G[X[i]].push_back(Y[i]);
  }

  priority_queue<long long> Q;
  long long ans = 0;
  for (int i = 1; i <= D; ++i) {
    for (const auto& e : G[i]) { Q.push(e); }
    if (!Q.empty()) {
      ans += Q.top();
      Q.pop();
    }
  }

  cout << ans << endl;

  return 0;
}