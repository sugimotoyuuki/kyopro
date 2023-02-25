#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b52.txt");
  cin.rdbuf(in.rdbuf());

  int N, X;
  cin >> N >> X;
  string color;
  cin >> color;

  queue<int> T;
  T.push(X - 1);
  color[X - 1] = '@';
  int pos;
  while (!T.empty()) {
    pos = T.front();
    T.pop();
    if (color[pos - 1] == '.') {
      color[pos - 1] = '@';
      T.push(pos - 1);
    }
    if (color[pos + 1] == '.') {
      color[pos + 1] = '@';
      T.push(pos + 1);
    }
  }

  for (int i = 0; i < color.length(); ++i) { cout << color[i]; }

  return 0;
}