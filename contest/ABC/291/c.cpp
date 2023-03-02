#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  string S;
  cin >> N >> S;

  set<pair<int, int>> G;

  G.insert(make_pair(0, 0));
  int x = 0;
  int y = 0;
  for (int i = 0; i < N; ++i) {
    if (S[i] == 'R') { x += 1; }
    if (S[i] == 'L') { x -= 1; }
    if (S[i] == 'U') { y += 1; }
    if (S[i] == 'D') { y -= 1; }
    if (G.count({x, y})) {
      cout << "Yes" << endl;
      return 0;
    }
    G.insert(make_pair(x, y));
  }

  cout << "No" << endl;

  return 0;
}