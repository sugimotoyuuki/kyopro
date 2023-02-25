#include <bits/stdc++.h>
using namespace std;

using Graph = vector<vector<int>>;

int main() {
  // input
  ifstream in("4.txt");
  cin.rdbuf(in.rdbuf());

  int N, M, X;
  cin >> N >> M >> X;
  int A, B;
  Graph G(N);
  for (int i = 0; i < M; ++i) {
    cin >> A >> B;
    G[A].push_back(B);
    G[B].push_back(A);
  }

  // algoでは友達をsetで抽出し, countにて判定していた
  set<int> aqua;
  for (int i = 0; i < G[X].size(); ++i) {
    int idx = G[X][i];
    for (int j = 0; j < G[idx].size(); ++j) {
      sort(G[X].begin(), G[X].end());
      if (G[idx][j] != X &&
          binary_search(G[X].begin(), G[X].end(), G[idx][j]) == false)
        aqua.insert(G[idx][j]);
    }
  }

  cout << aqua.size() << endl;

  return 0;
}