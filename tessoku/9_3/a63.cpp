#include <bits/stdc++.h>
using namespace std;

vector<int> G[100009];  // 要素素数はNで問題ない
bool visited[100009];
queue<int> Q;

int main() {
  // input
  ifstream in("a63.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  int A[M + 1], B[M + 1];
  for (int i = 1; i <= M; ++i) {
    cin >> A[i] >> B[i];
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }

  int dist[N + 1];
  for (int i = 1; i <= N; ++i) dist[i] = -1;
  Q.push(1);
  dist[1] = 0;

  while (!Q.empty()) {
    int pos = Q.front();
    Q.pop();
    for (int i = 0; i < G[pos].size(); ++i) {
      int to = G[pos][i];
      if (dist[to] == -1) {
        dist[to] = dist[pos] + 1;
        Q.push(to);
      }
    }
  }

  for (int i = 1; i <= N; ++i) cout << dist[i] << endl;

  return 0;
}