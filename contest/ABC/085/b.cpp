#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  vector<int> d;
  for (int i = 0; i < N; ++i) {
    int tmp;
    cin >> tmp;
    d.push_back(tmp);
  }
  sort(d.begin(), d.end());
  d.erase(unique(d.begin(), d.end()), d.end());
  cout << d.size() << endl;

  return 0;
}