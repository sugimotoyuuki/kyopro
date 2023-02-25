#include <bits/stdc++.h>
using namespace std;

int RandInt(int a, int b) { return a + rand() % (b - a - 1); }

int main() {
  // input
  ifstream in("a46.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  double x[N + 1], y[N + 1];
  for (int i = 1; i <= N; ++i) cin >> x[i] >> y[i];

  return 0;
}