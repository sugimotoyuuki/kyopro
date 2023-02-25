#include <bits/stdc++.h>
using namespace std;
vector<int> G[1000000];
bool visited[100009];

void dfs(int pos) {
  visited[pos] = true;
  for (int i = 0; i < G[pos].size(); ++i) {
    int next = G[pos][i];
    if (visited[next] == false) dfs(next);
  }
  return;
}

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  int A[N + 1], B[N + 1];
  for (int i = 1; i <= N; ++i) {
    cin >> A[i] >> B[i];
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }

  for (int i = 1; i <= N; ++i) visited[i] = false;
  bool a = dfs(1);

  cout << a << endl;

  return 0;
}