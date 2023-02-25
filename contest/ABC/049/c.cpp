#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("c.txt");
  cin.rdbuf(in.rdbuf());

  string S;
  cin >> S;

  int len = S.length();
  reverse(S.begin(), S.end());

  for (int i = 0; i < len; ++i) {
    if (S.substr(i, 5) == "maerd" || S.substr(i, 5) == "esare")
      i += 4;
    else if (S.substr(i, 6) == "resare")
      i += 5;
    else if (S.substr(i, 7) == "remaerd")
      i += 6;
    else {
      cout << "NO" << endl;
      return 0;
    }
  }

  cout << "YES" << endl;

  return 0;
}