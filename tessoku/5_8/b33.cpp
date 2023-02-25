#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b33.txt");
  cin.rdbuf(in.rdbuf());

  int N, H, W;
  cin >> N >> H >> W;
  int a, b;
  vector<long long> A, B;
  for (int i = 0; i < N; ++i) {
    cin >> a >> b;
    if (a - 1 != 0) A.push_back(a - 1);
    if (b - 1 != 0) B.push_back(b - 1);
  }

  long long ans = 0;
  if (A.size() != 0 && B.size() != 0) {
    ans = A[0] ^ B[0];
  } else if (A.size() != 0 && B.size() == 0) {
    ans = A[0];
  } else if (A.size() == 0 && B.size() != 0) {
    ans = A[0];
  } else {
    cout << "First" << endl;
    return 0;
  }
  for (int i = 1; i < A.size(); ++i) { ans = ans ^ A[i]; }
  for (int i = 1; i < B.size(); ++i) { ans = ans ^ B[i]; }

  if (ans == 0) {
    cout << "Second" << endl;
  } else {
    cout << "First" << endl;
  }

  return 0;
}