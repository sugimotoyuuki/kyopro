#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a42.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  int A[N + 1];
  int B[N + 1];
  for (int i = 1; i <= N; ++i) cin >> A[i] >> B[i];

  int ans = 0;
  for (int i = 1; i <= 100 - K; ++i) {
    for (int j = 1; j <= 100 - K; ++j) {
      int count = 0;
      for (int k = 1; k <= N; ++k) {
        if (i <= A[k] && A[k] <= (i + K) && j <= B[k] && B[k] <= (j + K)) {
          count += 1;
        }
      }
      ans = max(ans, count);
    }
  }

  cout << ans << endl;

  return 0;
}