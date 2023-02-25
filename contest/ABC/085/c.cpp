#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  long long N, Y;
  cin >> N >> Y;

  int paper[3] = {-1, -1, -1};
  for (int i = 0; i <= N; ++i) {
    for (int j = 0; j <= N - i; ++j) {
      int k = N - i - j;
      if ((10000 * k + 5000 * j + 1000 * i) == Y) {
        paper[0] = k;
        paper[1] = j;
        paper[2] = i;
      }
    }
  }

  for (int i = 0; i < 3; ++i) {
    if (i >= 1) cout << " ";
    cout << paper[i];
  }
  cout << endl;

  return 0;
}