#include <bits/stdc++.h>
using namespace std;

const long long inf = 3e11;

int main() {
  // input
  ifstream in("input_10.txt");
  cin.rdbuf(in.rdbuf());

  int N, M, D, K;
  int u[M + 1], v[M + 1], w[M + 1];
  vector<pair<double, double>> dijk[N + 1];

  cin >> N >> M >> D >> K;
  // input
  for (int i = 1; i <= M; ++i) {
    cin >> u[i] >> v[i] >> w[i];
    dijk[u[i]].push_back(make_pair(v[i], w[i]));
    dijk[v[i]].push_back(make_pair(u[i], w[i]));
  }

  priority_queue<pair<double, double>, vector<pair<double, double>>,
                 greater<pair<double, double>>>
      Q;

  long long cur[N + 1];
  bool confirmed[N + 1];

  for (int i = 1; i <= N; ++i) cur[i] = inf;
  for (int i = 1; i <= N; ++i) confirmed[i] = false;

  cur[1] = 0;
  Q.push(make_pair(0, 1));
  while (!Q.empty()) {
    int pos = Q.top().second;
    Q.pop();

    if (confirmed[pos] == true) continue;
    confirmed[pos] = true;

    for (int i = 0; i < dijk[pos].size(); ++i) {
      int next = dijk[pos][i].first;
      int cost = dijk[pos][i].second;
      if (cur[next] > cur[pos] + cost) {
        cur[next] = cur[pos] + cost;
        Q.push(make_pair(cur[next], next));
      }
    }
  }

  return 0;
}