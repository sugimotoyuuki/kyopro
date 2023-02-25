#include <bits/stdc++.h>
using namespace std;

const long long inf = 2e9;

void wf(vector<vector<long long>> &G) {
  int V = G.size();
  for (int k = 1; k < V; k++) {
    for (int i = 1; i < V; i++) {
      for (int j = 1; j < V; j++) { G[i][j] = min(G[i][j], G[i][k] + G[k][j]); }
    }
  }
}

int main() {
  // input
  ifstream in("input_10.txt");
  cin.rdbuf(in.rdbuf());

  int N, M, D, K;
  cin >> N >> M >> D >> K;

  int u[M + 1], v[M + 1], w[M + 1];
  vector<vector<long long>> dij(N + 1, vector<long long>(N + 1, inf));
  // input
  for (int i = 1; i <= M; ++i) {
    cin >> u[i] >> v[i] >> w[i];
    dij[u[i]][v[i]] = w[i];
    dij[v[i]][u[i]] = w[i];
  }
  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= N; ++j) {
      if (i == j) dij[i][j] = 0;
    }
  }

  // 工事していないときの最短距離
  wf(dij);

  long long fik[M + 1];
  for (int i = 1; i <= M; ++i) {
    vector<vector<long long>> dijk(N + 1, vector<long long>(N + 1, inf));

    for (int j = 1; j <= N; ++j) {
      for (int k = 1; k <= N; ++k) {
        if (j == k) dijk[j][k] = 0;
      }
    }

    // u[i], v[i] の辺を除去
    for (int j = 1; j <= M; ++j) {
      if (i != j) {
        dijk[u[j]][v[j]] = w[j];
        dijk[v[j]][u[j]] = w[j];
      }
    }

    // 一箇所だけ工事したときの最短距離
    wf(dijk);

    // fijkを算出するためにdijk - dijを行う
    long long fijk[N + 1][N + 1];
    for (int j = 1; j <= N; ++j) {
      for (int k = 1; k <= N; ++k) { fijk[j][k] = 0; }
    }
    for (int j = 1; j <= N; ++j) {
      for (int k = 1; k <= N; ++k) { fijk[j][k] = dijk[j][k] - dij[j][k]; }
    }

    // fijk について総和を取る
    for (int j = 1; j <= N; ++j) {
      for (int k = 2; k <= N; ++k) { fijk[j][k] = fijk[j][k - 1] + fijk[j][k]; }
    }

    for (int j = 2; j <= N; ++j) {
      for (int k = 1; k <= N; ++k) { fijk[j][k] = fijk[j - 1][k] + fijk[j][k]; }
    }

    fik[i] = fijk[N][N];
  }

  for (int j = 1; j <= M; ++j) cout << fik[j] << " ";

  return 0;
}