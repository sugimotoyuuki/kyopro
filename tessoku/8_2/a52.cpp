#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a52.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;
  queue<string> T;
  int op;
  string title;
  for (int i = 1; i <= Q; ++i) {
    cin >> op;
    if (op == 1) {
      cin >> title;
      T.push(title);
    }
    if (op == 2) { cout << T.front() << endl; }
    if (op == 3) { T.pop(); }
  }

  return 0;
}