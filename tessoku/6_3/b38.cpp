#include <bits/stdc++.h>

using namespace std;

// 下限値が1なのでAは1 -> Nで次の値が1増える, BはN ->
// 1で次の値が1増える配列を考える
int main() {
  // input
  ifstream in("b38.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  string S;
  cin >> S;

  int contiA[N]{};
  int contiB[N]{};

  int count = 1;
  contiA[0] = 1;
  for (int i = 0; i < N - 1; ++i) {
    if (S[i] == 'A') count += 1;
    if (S[i] == 'B') count = 1;
    contiA[i + 1] = count;
  }

  count = 1;
  contiB[N - 1] = 1;
  for (int i = N - 2; i >= 0; --i) {
    if (S[i] == 'B') count += 1;
    if (S[i] == 'A') count = 1;
    contiB[i] = count;
  }

  long long ans = 0;
  for (int i = 0; i < N; ++i) ans += max(contiA[i], contiB[i]);
  cout << ans << endl;

  return 0;
}