#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  int k;
  vector<int> ans[M];
  for (int i = 1; i <= M; ++i) {
    cin >> k;
    int A[k + 1] = {};
    for (int j = 1; j <= k; ++j) {
      cin >> A[j];
      ans[A[j]].push_back(i);
      cout << A[j];
    }
  }

  /*for (int i = 0; i < M; ++i) {
    for (int j = 1; j < ans[i].size(); ++j) { cout << ans[i][j] << endl; }
  }*/
  return 0;
}