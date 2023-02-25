#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a41.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  string S;
  cin >> S;

  if (S.find("RRR") != string::npos) {
    cout << "Yes" << endl;
  } else if (S.find("BBB") != string::npos) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}