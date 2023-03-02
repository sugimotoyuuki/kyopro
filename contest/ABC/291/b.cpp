#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;

  double X[5 * N];
  for (int i = 0; i < (5 * N); ++i) { cin >> X[i]; }
  sort(X, X + (5 * N));
  double sum = 0;
  for (int i = N; i < (4 * N); ++i) { sum += X[i]; }
  cout << sum / (3 * N) << endl;

  return 0;
}