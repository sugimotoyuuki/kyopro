#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a64.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  int A[M + 1], B[M + 1], C[M + 1];
  vector<pair<int, int>> G[N + 1];
  for (int i = 1; i <= M; ++i) {
    cin >> A[i] >> B[i] >> C[i];
    G[A[i]].push_back(make_pair(B[i], C[i]));
    G[B[i]].push_back(make_pair(A[i], C[i]));
  }

  priority_queue<pair<long long, long long>, vector<pair<long long, long long>>,
                 greater<pair<long long, long long>>>
      Q;
  int cur[N + 1];
  bool confirmed[N + 1];

  for (int i = 1; i <= N; ++i) cur[i] = 2e9;
  for (int i = 1; i <= N; ++i) confirmed[i] = false;

  cur[1] = 0;
  Q.push(make_pair(0, 1));
  while (!Q.empty()) {
    int pos = Q.top().second;
    Q.pop();

    if (confirmed[pos] == true) continue;
    confirmed[pos] = true;

    for (int i = 0; i < G[pos].size(); ++i) {
      int next = G[pos][i].first;
      int cost = G[pos][i].second;
      if (cur[next] > cur[pos] + cost) {
        cur[next] = cur[pos] + cost;
        Q.push(make_pair(cur[next], next));
      }
    }
  }

  for (int i = 1; i <= N; ++i) {
    if (cur[i] == 2e9)
      cout << "-1" << endl;
    else
      cout << cur[i] << endl;
  }

  return 0;
}