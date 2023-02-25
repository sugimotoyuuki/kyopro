#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a34.txt");
  cin.rdbuf(in.rdbuf());

  int N, X, Y;
  cin >> N >> X >> Y;
  vector<int> A;
  int tmp;
  for (int i = 0; i < N; ++i) {
    cin >> tmp;
    A.push_back(tmp);
  }

  int max = *max_element(A.begin(), A.end());

  int G[max + 1];

  for (int i = 0; i <= max; ++i) {
    bool trans[3] = {false, false, false};
    if (i >= X) trans[G[i - X]] = true;
    if (i >= Y) trans[G[i - Y]] = true;
    if (trans[0] == false) {
      G[i] = 0;
    } else if (trans[1] == false) {
      G[i] = 1;
    } else {
      G[i] = 2;
    }
  }

  int xor_sum = 0;
  for (int i = 0; i < N; ++i) { xor_sum = (xor_sum ^ G[A[i]]); }
  if (xor_sum != 0) {
    cout << "First" << endl;
  } else {
    cout << "Second" << endl;
  }

  return 0;
}