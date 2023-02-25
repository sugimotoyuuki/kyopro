#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a54.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;

  map<string, int> query;
  int term, score;
  string name;
  for (int i = 0; i < Q; ++i) {
    cin >> term;
    if (term == 1) {
      cin >> name >> score;
      query[name] = score;
    } else if (term == 2) {
      cin >> name;
      cout << query[name] << endl;
    }
  }

  return 0;
}