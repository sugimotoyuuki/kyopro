#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a61.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  int A[M + 1], B[M + 1];
  vector<int> G[N + 1];
  for (int i = 1; i <= M; ++i) {
    cin >> A[i] >> B[i];
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }

  for (int i = 1; i <= N; ++i) {
    cout << i << ": {";
    for (int j = 0; j < G[i].size(); ++j) {
      if (j >= 1) cout << ", ";
      cout << G[i][j];
    }
    cout << "}" << endl;
  }

  return 0;
}