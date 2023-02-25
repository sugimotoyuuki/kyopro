#include <bits/stdc++.h>

using namespace std;

int main() {
  // input
  ifstream in("B054.txt");
  cin.rdbuf(in.rdbuf());

  string A, B;
  cin >> A >> B;

  vector<char> s = {'A', 'B', 'C', 'D', 'E'};

  vector<long long> tA, tB;
  for (int i = 0; i < A.length(); ++i) { tA.push_back((int)A[i] - 65); }
  for (int i = 0; i < B.length(); ++i) { tB.push_back((int)B[i] - 65); }

  long long f = 0;
  for (int i = 0; i < tA.size(); ++i) {
    f += tA[i] * pow(5, A.length() - i - 1);
  }
  for (int i = 0; i < tB.size(); ++i) {
    f += tB[i] * pow(5, B.length() - i - 1);
  }

  vector<int> ans;
  if (f == 0) {
    cout << 'A' << endl;
    return 0;
  }
  while (f != 0) {
    ans.push_back(f % 5);
    f = f / 5;
  }

  for (int i = ans.size() - 1; i >= 0; --i) { cout << s[ans[i]]; }

  return 0;
}