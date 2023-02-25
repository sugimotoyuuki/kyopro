#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("1.txt");
  cin.rdbuf(in.rdbuf());

  int N, A, B;
  cin >> N >> A >> B;
  vector<string> S(N);
  for (auto &str : S) cin >> str;

  if (S[A][B] == 'o') {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}