#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b55.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;

  set<int> query;
  int term, x;
  int ans = 0;
  for (int i = 0; i < Q; ++i) {
    cin >> term >> x;
    if (term == 1) { query.insert(x); }
    if (term == 2) {
      if (query.empty()) {
        cout << "-1" << endl;
      } else {
        auto itr = query.lower_bound(x);
        if (itr == query.end()) {
          ans = abs(x - (*--itr));
        } else if (itr == query.begin()) {
          ans = abs(x - (*itr));
        } else if (query.size() > 1) {
          ans = abs(x - (*itr));
          --itr;
          ans = min(ans, abs(x - (*itr)));
        }
        cout << ans << endl;
      }
    }
  }

  return 0;
}