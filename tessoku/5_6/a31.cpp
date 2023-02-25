#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a31.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;

  long long P = (N / 3);
  long long Q = (N / 5);
  long long R = (N / 15);

  cout << P + Q - R << endl;

  return 0;
}