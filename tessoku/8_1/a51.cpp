#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a51.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;
  stack<string> S;
  int op;
  string title;
  for (int i = 1; i <= Q; ++i) {
    cin >> op;
    if (op == 1) {
      cin >> title;
      S.push(title);
    }
    if (op == 2) { cout << S.top() << endl; }
    if (op == 3) { S.pop(); }
  }

  return 0;
}