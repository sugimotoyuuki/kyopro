#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("a.txt");
  cin.rdbuf(in.rdbuf());

  string s;
  cin >> s;

  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == '0') {
      s[i] = '1';
    } else if (s[i] == '1') {
      s[i] = '0';
    }
  }

  cout << s << endl;

  return 0;
}