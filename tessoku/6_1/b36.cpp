#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b36.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;

  string S;
  cin >> S;

  int on = 0;
  for (int i = 0; i < N; ++i) on += (int)S[i] - 48;

  if (abs(on - K) % 2 == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}