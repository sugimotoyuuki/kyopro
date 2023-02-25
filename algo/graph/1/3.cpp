#include <bits/stdc++.h>
using namespace std;

using Graph = vector<vector<int>>;

int main() {
  // input
  ifstream in("3.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  int A, B;
  Graph G(N);
  for (int i = 0; i < M; ++i) {
    cin >> A >> B;
    G[A].push_back(B);
    G[B].push_back(A);
  }

  int count = 0;
  int S[N];
  for (int i = 0; i < N; ++i) {
    sort(G[i].begin(), G[i].end());
    S[i] = (int)G[i].size();
  }

  int index = distance(S, max_element(S, S + N));
  for (int j = 0; j < G[index].size(); ++j) { cout << G[index][j] << " "; }
  cout << endl;

  return 0;
}