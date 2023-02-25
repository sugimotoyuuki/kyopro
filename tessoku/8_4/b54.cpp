#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("b54.txt");
  cin.rdbuf(in.rdbuf());

  int Q;
  cin >> Q;

  map<long long, long long> map;
  long long tmp;
  for (int i = 0; i < Q; ++i) {
    cin >> tmp;
    if (map.find(tmp) == map.end()) {
      map[tmp] = 1;
    } else {
      map[tmp] += 1;
    }
  }

  long long ans = 0;
  for (auto itr = map.begin(); itr != map.end(); ++itr) {
    long long n = itr->second;
    if (n >= 2) { ans += (n * (n - 1)) / 2LL; }
  }

  cout << ans << endl;

  return 0;
}