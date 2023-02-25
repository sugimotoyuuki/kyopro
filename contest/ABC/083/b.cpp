#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, A, B;
  cin >> N >> A >> B;

  int ans = 0;
  string tmp;
  for (int i = 1; i <= N; ++i) {
    int sum = 0;
    int j = i;
    while (j > 0) {
      sum += j % 10;
      j /= 10;
    }
    if (A <= sum && sum <= B) ans += i;
  }

  cout << ans << endl;

  return 0;
}