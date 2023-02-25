#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;
  long long A[N + 1], B[N + 1];
  for (int i = 1; i <= N; ++i) cin >> A[i] >> B[i];

  for (int i = 1; i <= N; ++i) cout << A[i] + B[i] << endl;

  return 0;
}