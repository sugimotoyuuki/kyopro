#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a53.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;

  priority_queue<int, vector<int>, greater<int>> Q;
  int query[N + 1];
  int num[N + 1]{};
  for (int i = 1; i <= N; ++i) {
    cin >> query[i];
    if (query[i] == 1) cin >> num[i];
  }

  for (int i = 1; i <= N; ++i) {
    if (query[i] == 1) Q.push(num[i]);
    if (query[i] == 2) cout << Q.top() << endl;
    if (query[i] == 3) Q.pop();
  }

  return 0;
}