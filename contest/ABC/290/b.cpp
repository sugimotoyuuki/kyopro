#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  string S;
  for (int i = 0; i < N; ++i) { cin >> S; }
  int pass = 0;
  vector<int> id;
  for (int i = 0; i < S.length(); ++i) {
    if (S[i] == 'o') {
      pass += 1;
      if (K < pass) { S[i] = 'x'; }
    }
  }

  for (int i = 0; i < S.length(); ++i) { cout << S[i]; }

  return 0;
}