#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a39.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;
  long long L[N + 1], R[N + 1];
  for (int i = 1; i <= N; ++i) cin >> L[i] >> R[i];

  vector<pair<long long, long long>> RL;
  for (int i = 1; i <= N; ++i) RL.push_back(make_pair(R[i], L[i]));
  sort(RL.begin(), RL.end());

  long long end = RL[0].first;
  int count = 1;
  for (int i = 1; i < N; ++i) {
    if (RL[i].second >= end) {
      end = RL[i].first;
      count += 1;
    }
  }

  cout << count << endl;

  return 0;
}