#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  int a[M + 1]{};
  for (int i = 1; i <= M; ++i) cin >> a[i];
  a[M + 1] = 2e5;

  int num[N + 1];
  for (int i = 1; i <= N; ++i) num[i] = i;

  vector<int> start;
  vector<int> end;
  start.push_back(a[1]);
  for (int i = 1; i <= M; ++i) {
    if (a[i] + 1 != a[i + 1]) {
      end.push_back(a[i] + 1);
      start.push_back(a[i + 1]);
    }
  }

  for (int i = 0; i < start.size() - 1; ++i) {
    sort(num + (int)start[i], num + (int)end[i] + 1, greater<int>());
  }

  for (int i = 1; i <= N; ++i) {
    if (i != 1) cout << " ";
    cout << num[i];
  }

  return 0;
}