#include <bits/stdc++.h>

using namespace std;

// 各カードの正負で場合分けして考えていく
// 最大値はカードの表裏の和が正になるときを取り続けていくことで得られる(負を取ると総和は減る)
// 絶対値の和は結合できる
// plusは表と裏が正負どちらを取るかを表している

int N;
vector<long long> A, B;

long long casesum(vector<bool> plus) {
  long long sum = 0;
  for (int i = 0; i < A.size(); ++i) {
    long long face = A[i];
    long long back = B[i];
    if (plus[0] == false) { face = -A[i]; }
    if (plus[1] == false) { back = -B[i]; }
    if (face + back >= 0) sum += face + back;
  }

  return sum;
}

int main() {
  // input
  ifstream in("b42.txt");
  cin.rdbuf(in.rdbuf());

  cin >> N;

  long long tmpA, tmpB;
  for (int i = 0; i < N; ++i) {
    cin >> tmpA >> tmpB;
    A.push_back(tmpA);
    B.push_back(tmpB);
  }

  vector<long long> ansvc(4);
  ansvc[0] = casesum({true, true});
  ansvc[1] = casesum({true, false});
  ansvc[2] = casesum({false, true});
  ansvc[3] = casesum({false, false});

  long long ans = 0;
  for (int i = 0; i < 4; ++i) { ans = max(ans, ansvc[i]); }
  cout << ans << endl;

  return 0;
}