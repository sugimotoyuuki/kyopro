#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;
  int A[N + 1], B[N + 1];
  for (int i = 1; i <= N; ++i) { cin >> A[i]; }
  for (int i = 1; i <= M; ++i) { cin >> B[i]; }

  int ans = 0;
  for (int i = 1; i <= M; ++i) { ans += A[B[i]]; }

  cout << ans << endl;

  return 0;
}