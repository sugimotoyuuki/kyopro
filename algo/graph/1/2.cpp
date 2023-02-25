#include <bits/stdc++.h>
using namespace std;

using Graph = vector<vector<int>>;

int main() {
  // input
  ifstream in("2.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  int A, B;
  Graph G(N);
  for (int i = 0; i < M; ++i) {
    cin >> A >> B;
    G[A].push_back(B);
  }

  for (int i = 0; i < N; ++i) {
    sort(G[i].begin(), G[i].end());
    for (auto to : G[i]) { cout << to << " "; }
    cout << endl;
  }

  return 0;
}