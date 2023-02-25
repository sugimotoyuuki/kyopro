#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  string S[N];
  for (int i = 0; i < K; ++i) cin >> S[i];

  string tmp;
  for (int i = 0; i < K - 1; ++i) {
    for (int j = 0; j < K - 1; ++j) {
      if (S[j] > S[j + 1]) {
        tmp = S[j];
        S[j] = S[j + 1];
        S[j + 1] = tmp;
      }
    }
  }

  for (int i = 0; i <= K - 1; ++i) cout << S[i] << endl;

  return 0;
}