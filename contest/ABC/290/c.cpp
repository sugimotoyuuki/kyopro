#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;
  set<int> A;
  int tmp;
  for (int i = 0; i < N; ++i) {
    cin >> tmp;
    A.insert(tmp);
  }

  for (int i = 0; i < K; ++i) {
    if (A.find(i) == A.end()) {
      cout << i << endl;
      return 0;
    }
  }

  cout << K << endl;

  return 0;
}