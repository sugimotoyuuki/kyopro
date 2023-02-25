#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a33.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  long long A[N];
  for (int i = 0; i < N; ++i) cin >> A[i];

  long long ans = A[0] ^ A[1];
  for (int i = 2; i < N; ++i) { ans = ans ^ A[i]; }

  if (ans == 0) {
    cout << "Second" << endl;
  } else {
    cout << "First" << endl;
  }

  return 0;
}