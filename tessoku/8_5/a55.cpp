#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a55.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;

  set<int> query;
  int term, x;
  for (int i = 0; i < Q; ++i) {
    cin >> term >> x;
    if (term == 1) { query.insert(x); }
    if (term == 2) { query.erase(x); }
    if (term == 3) {
      auto itr = query.lower_bound(x);
      if (itr == query.end()) {
        cout << "-1" << endl;
      } else {
        cout << (*itr) << endl;
      }
    }
  }

  return 0;
}