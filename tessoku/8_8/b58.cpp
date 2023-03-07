#include <bits/stdc++.h>
using namespace std;
// わからん典型DPをさきにやる

class SegmentTree {
 public:
  int dat[300000], siz = 1;

  // initialize dat
  void init(int N) {
    siz = 1;
    while (siz < N) siz *= 2;
    for (int i = 1; i < siz * 2; ++i) dat[i] = 0;
  }

  // query1
  void update(int pos, int x) {
    pos = pos + siz - 1;
    dat[pos] = x;
    while (pos >= 2) {
      pos /= 2;
      dat[pos] = min(dat[pos * 2], dat[pos * 2 + 1]);
    }
  }

  // query2
  int query(int l, int r, int a, int b, int u) {
    if (r <= a || b <= l) return 1000000000;
    if (l <= a && b <= r) return dat[u];
    int m = (a + b) / 2;
    int ansl = query(l, r, a, m, u * 2);
    int ansr = query(l, r, m, b, u * 2 + 1);
    cout << ansl << " " << ansr << endl;
    return min(ansl, ansr);
  }
};

int N, L, R;
int X[100009];
int dp[100009];
SegmentTree Z;

int main() {
  // input
  ifstream in("b58.txt");
  cin.rdbuf(in.rdbuf());

  cin >> N >> L >> R;
  for (int i = 1; i <= N; ++i) { cin >> X[i]; }

  Z.init(N);
  dp[1] = 0;
  Z.update(1, 0);

  for (int i = 2; i <= N; i++) {
    // X[i]よりL前とR前に一番近い座標をposLRとしている
    // どこの範囲からposまで飛べるかを表している
    int posL = lower_bound(X + 1, X + N + 1, X[i] - R) - X;
    // 単純にposRに1を引いた値を渡しているだけ
    int posR = upper_bound(X + 1, X + N + 1, X[i] - L) - X - 1;
    // posLRの範囲の最小を求め、そこへ1を足す
    // 各dpにはposへの最小のジャンプ数が格納
    dp[i] = Z.query(posL, posR + 1, 1, Z.siz + 1, 1) + 1;
    Z.update(i, dp[i]);
    cout << dp[i] << endl;
    cout << posL << " " << posR << endl;
  }

  cout << dp[N] << endl;

  return 0;
}