#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  string S;
  cin >> S;

  int len = S.length();
  long long ans = 0;
  for (int i = 1; i <= len; ++i) {
    ans += pow(26, (len - i)) * (S[i - 1] - 64);
  }

  cout << ans << endl;

  return 0;
}