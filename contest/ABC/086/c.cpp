#include <bits/stdc++.h>
using namespace std;

void solve() {}

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  int t[N + 1]{};
  int x[N + 1]{};
  int y[N + 1]{};

  for (int i = 1; i <= N; ++i) cin >> t[i] >> x[i] >> y[i];

  int even = true;
  for (int i = 1; i <= N; ++i) {
    int dist = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1]);
    int dt = t[i] - t[i - 1];
    if (dist > dt || (dt - dist) % 2 == 1) {
      cout << "No" << endl;
      return 0;
    }
  }

  cout << "Yes" << endl;

  return 0;
}