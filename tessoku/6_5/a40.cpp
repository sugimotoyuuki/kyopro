#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a40.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;
  long long A[N];
  for (int i = 0; i < N; ++i) cin >> A[i];

  int sidelen[N + 1]{};
  for (int i = 0; i < N; ++i) sidelen[A[i]] += 1;

  long long ans = 0;
  for (int i = 1; i < N; ++i) {
    long long den = 1;
    for (int j = 0; j <= 2; ++j) {
      if (sidelen[i] != 0) { den *= sidelen[i] - j; }
    }
    ans += den / 6LL;
  }

  cout << ans << endl;

  return 0;
}