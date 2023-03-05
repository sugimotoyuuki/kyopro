#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  long long ans = 0;
  for (int i = 1; i < N; ++i) {
    int L = i;
    int R = N - i;
    long long a = 0, b = 0;
    for (int j = 1; j * j <= L; ++j) {
      if (L % j == 0) {
        ++a;
        if (L != j * j) ++a;
      }
    }
    for (int j = 1; j * j <= R; ++j) {
      if (R % j == 0) {
        ++b;
        if (R != j * j) ++b;
      }
    }
    ans += a * b;
  }

  cout << ans << endl;

  return 0;
}