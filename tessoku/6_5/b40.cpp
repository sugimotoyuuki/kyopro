#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b40.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;
  long long A[N];
  for (int i = 0; i < N; ++i) cin >> A[i];

  int ans = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      if ((A[i] + A[j]) % 100 == 0) ans += 1;
    }
  }

  cout << ans << endl;

  return 0;
}