#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;

  vector<int> a;
  for (int i = 0; i < N; ++i) {
    int tmp;
    cin >> tmp;
    a.push_back(tmp);
  }
  sort(a.begin(), a.end());
  reverse(a.begin(), a.end());

  int ali, bob = {};
  for (int i = 0; i < a.size(); ++i) {
    if (i % 2 == 0)
      ali += a[i];
    else
      bob += a[i];
  }

  cout << ali - bob << endl;

  return 0;
}