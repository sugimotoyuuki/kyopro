#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b43.txt");
  cin.rdbuf(in.rdbuf());

  int N, M;
  cin >> N >> M;

  int A[N + 1]{};
  int incid;
  for (int i = 0; i < M; ++i) {
    cin >> incid;
    A[incid] += 1;
  }

  for (int i = 1; i <= N; ++i) { cout << M - A[i] << endl; }

  return 0;
}