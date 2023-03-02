#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("d.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  vector<int, int> G(N);
  for (int i = 0; i < M; ++i) {
    int tmp1, tmp2;
    cin >> tmp1 >> tmp2;
    G[tmp1].push_back(tmp2);
  }
  for (int i = 1; i < G.size(); ++i) { unique(G[i].begin(), G[i].end()); }
  for (int i = 1; i < G.size(); ++i) {
    for (int j = 1; j < G[i].size(); ++j) cout << G[i][j] << endl;
  }

  return 0;
}