#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b34.txt");
  cin.rdbuf(in.rdbuf());

  int N, X, Y;
  cin >> N >> X >> Y;
  long long A[N];
  for (int i = 0; i < N; ++i) { cin >> A[i]; }

  long long G[N];
  for (int i = 0; i < N; ++i) {
    if (A[i] % 5 == 4) {
      G[i] = 2;
    } else if (A[i] % 5 == 3 || A[i] % 5 == 2) {
      G[i] = 1;
    } else if (A[i] % 5 == 1 || A[i] % 5 == 0) {
      G[i] = 0;
    }
  }

  int xor_sum = 0;
  for (int i = 0; i < N; ++i) { xor_sum = (xor_sum ^ G[i]); }
  if (xor_sum != 0) {
    cout << "First" << endl;
  } else {
    cout << "Second" << endl;
  }

  return 0;
}