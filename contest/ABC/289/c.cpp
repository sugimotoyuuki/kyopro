#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  vector<int> A;
  int tmp, C, count;
  for (int i = 0; i < M; ++i) {
    cin >> C;
    tmp = 0;
    count = 0;
    for (int j = 0; j < C; ++j) {
      cin >> tmp;
      count += 1 << (tmp - 1);
    }
    A.push_back(count);
  }

  int ans = 0;
  for (int bit = 0; bit < (1 << M); ++bit) {
    int sum = 0;
    for (int i = 0; i < A.size(); ++i) {
      if (bit & (1 << i)) sum |= A[i];
    }
    if (sum == (1 << N) - 1) ans += 1;
  }

  cout << ans << endl;

  return 0;
}