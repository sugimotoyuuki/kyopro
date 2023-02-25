#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a36.txt");
  cin.rdbuf(in.rdbuf());

  int N, K;
  cin >> N >> K;

  if (K >= (2 * N - 2) && K % 2 == 0)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}