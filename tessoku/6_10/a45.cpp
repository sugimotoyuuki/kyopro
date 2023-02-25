#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a45.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  char C;
  string A;
  cin >> N >> C;
  cin >> A;

  int count = 0;
  for (int i = 0; i < N; ++i) {
    if (A[i] == 'B') count += 1;
    if (A[i] == 'R') count += 2;
  }

  int ans = count % 3;

  if (C == 'W' && ans == 0) {
    cout << "Yes" << endl;
  } else if (C == 'B' && ans == 1) {
    cout << "Yes" << endl;
  } else if (C == 'R' && ans == 2) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}