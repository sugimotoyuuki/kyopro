#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a;
  a.push_back(1);
  a[1] = 2;
  a[2] = 2;

  cout << a[2] << endl;

  return 0;
}