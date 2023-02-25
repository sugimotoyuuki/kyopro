#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b41.txt");
  cin.rdbuf(in.rdbuf());

  int X, Y;
  cin >> X >> Y;

  vector<pair<int, int>> ans;
  while (!(X == 1 && Y == 1)) {
    ans.push_back(make_pair(X, Y));
    if (X > Y) {
      X = X - Y;
    } else if (X < Y) {
      Y = Y - X;
    } else if (X == 0 || Y == 0) {
      cout << 0 << endl;
      return 0;
    }
  }

  cout << ans.size() << endl;
  for (int i = ans.size() - 1; i >= 0; --i) {
    cout << ans[i].first << " " << ans[i].second << endl;
  }

  return 0;
}