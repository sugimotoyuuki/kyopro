#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a43.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  long long L;
  cin >> N >> L;

  vector<long long> A;
  vector<char> B;
  long long tmpA;
  char tmpB;
  for (int i = 0; i < N; ++i) {
    cin >> tmpA >> tmpB;
    A.push_back(tmpA);
    B.push_back(tmpB);
  }

  long long ans = 0;
  for (int i = 0; i < N; ++i) {
    if (B[i] == 'W') ans = max(ans, A[i]);
    if (B[i] == 'E') ans = max(ans, L - A[i]);
  }

  cout << ans << endl;

  return 0;
}