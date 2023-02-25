#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b37.txt");
  cin.rdbuf(in.rdbuf());

  // TLE
  long long N;
  cin >> N;
  long long ans = 0;
  for (int i = 1; i <= N; ++i) {
    string S = to_string(i);
    for (int j = 0; j < S.length(); ++j) { ans += S[j] - 48; }
  }
  cout << ans << endl;

  return 0;
}