#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("b31.txt");
  cin.rdbuf(in.rdbuf());

  long long N;
  cin >> N;

  long long A = (N / 3);
  long long B = (N / 5);
  long long C = (N / 7);
  long long D = (N / 15);
  long long E = (N / 21);
  long long F = (N / 35);
  long long G = (N / 105);

  cout << A + B + C - D - E - F + G << endl;

  return 0;
}