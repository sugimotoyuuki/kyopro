#include <bits/stdc++.h>
using namespace std;

// bもやったがaに上書きしてしまった
int main() {
  // input
  ifstream in("a29.txt");
  cin.rdbuf(in.rdbuf());

  unsigned long long a, b;
  cin >> a >> b;

  unsigned long long m = 1e9 + 7;
  unsigned long long ans = 1;

  // 1 << i だとオーバーフローしてしいまう
  for (int i = 0; i < 60; ++i) {
    if (b >> i & 1) ans = ((a % m) * (ans % m)) % m;
    a = ((a % m) * (a % m)) % m;
  }

  cout << ans << endl;

  return 0;
}