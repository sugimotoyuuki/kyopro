#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b51.txt");
  cin.rdbuf(in.rdbuf());

  string S;
  cin >> S;
  S[S.length()] = '(';
  stack<int> id1;
  vector<int> id2;
  for (int i = 0; i < S.length(); ++i) {
    if (S[i] == '(') { id1.push(i + 1); }
    if (S[i] == ')') {
      id2.push_back(i + 1);
      if (S[i + 1] == '(') {
        for (int i = 0; i < id2.size(); ++i) {
          cout << id1.top() << " ";
          cout << id2[i] << endl;
          id1.pop();
        }
        id2 = {};
      }
    }
  }

  return 0;
}