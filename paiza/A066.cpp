#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("A066.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;

  vector<pair<int, int>> D;

  int tmpA, tmpB;
  for (int i = 0; i < N; ++i) {
    cin >> tmpA >> tmpB;
    D.push_back(make_pair(tmpA, tmpB));
  }

  sort(D.begin(), D.end());

  int start, end;
  vector<int> days;

  start = D[0].first;
  end = D[0].second;
  for (int i = 1; i < N; ++i) {
    if (start <= D[i].first && D[i].first <= end + 1) {
      end = max(end, D[i].second);
    } else {
      days.push_back(end - start + 2);
      start = D[i].first;
      end = D[i].second;
    }
  }
  days.push_back(end - start + 1);

  int maxday = *max_element(days.begin(), days.end());

  cout << maxday << endl;

  return 0;
}