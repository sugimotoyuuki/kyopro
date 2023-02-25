#include <bits/stdc++.h>
using namespace std;

// 1 ~ 9までの値がいくつあるかを数え上げれば良い
int main() {
  // input
  ifstream in("b37.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;

  // numberDigではi桁にjがいくつあるかを数え上げる
  long long numberDig[17][10];

  // 10の累乗を定義する
  long long exp[17];
  exp[0] = 1;
  for (int i = 1; i <= 16; i++) { exp[i] = exp[i - 1] * 10; }

  for (int i = 0; i <= 15; i++) {
    // 下から i 桁目の数字を求める
    long long Dig = (N / exp[i]) % 10;
    for (int j = 0; j <= 9; ++j) {
      if (j < Dig) { numberDig[i][j] = (N / exp[i + 1] + 1) * exp[i]; }
      if (j == Dig) {
        numberDig[i][j] = (N / exp[i + 1]) * exp[i] + (N % exp[i]) + 1;
      }
      if (j > Dig) { numberDig[i][j] = (N / exp[i + 1]) * exp[i]; }
    }
  }

  // 答えに書く桁の数をかけ合わせて総和を取る
  long long ans = 0;
  for (int i = 0; i <= 15; ++i) {
    for (int j = 0; j <= 9; ++j) ans += j * numberDig[i][j];
  }

  cout << ans << endl;

  return 0;
}