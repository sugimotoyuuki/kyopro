#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a32.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  int A, B;
  cin >> A >> B;

  bool vict[N + 1];
  for (int i = 0; i <= N; ++i) { vict[i] = false; }
  vict[A] = true;
  for (int i = min(A, B) + 1; i <= N; ++i) {
    if (i >= A && vict[i - A] == false) {
      vict[i] = true;
    } else if (i >= B && vict[i - B] == false) {
      vict[i] = true;
    } else {
      vict[i] = false;
    }
  }

  if (vict[N]) {
    cout << "First" << endl;
  } else {
    cout << "Second" << endl;
  }

  return 0;
}