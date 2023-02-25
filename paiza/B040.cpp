#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("B40.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  string trans;
  cin >> N >> trans;

  vector<string> A;
  string tmp;
  while (getline(cin, tmp, ' ')) { A.push_back(tmp); }
  A[0].erase(0, 1);
  A[A.size() - 1].pop_back();

  while (N != 0) {
    for (int i = 0; i < A.size(); ++i) {
      string tmp2 = "";
      for (int j = 0; j < A[i].size(); ++j) {
        tmp2 += 97 + trans.find(A[i][j]);
      }
      A[i] = tmp2;
    }
    N -= 1;
  }

  for (int i = 0; i < A.size(); ++i) {
    if (i != 0) cout << " ";
    cout << A[i];
  }

  return 0;
}