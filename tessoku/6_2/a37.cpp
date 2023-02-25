#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a37.txt");
  cin.rdbuf(in.rdbuf());

  long long N, M, B;
  cin >> N >> M >> B;
  long long A[N + 1];
  long long C[M + 1];
  for (int i = 1; i <= N; ++i) cin >> A[i];
  for (int i = 1; i <= M; ++i) cin >> C[i];

  long long ans = 0;
  for (int i = 1; i <= N; ++i) ans += M * A[i];
  for (int i = 1; i <= M; ++i) ans += N * C[i];
  ans += N * M * B;
  cout << ans << endl;

  return 0;
}