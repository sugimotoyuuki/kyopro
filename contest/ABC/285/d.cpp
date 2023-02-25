#include <bits/stdc++.h>
using namespace std;

long long stolong(string S) {
  int len = S.length();
  long long ver = 0;
  for (int i = 1; i <= len; ++i) {
    ver += pow(26, (len - i)) * (S[i - 1] - 64);
  }
  return ver;
}

int main() {
  // input
  ifstream in("d.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;

  map<long long, long long> G;
  string tmp1, tmp2;
  long long ver1, ver2;
  for (int i = 0; i < N; ++i) {
    cin >> tmp1 >> tmp2;
    ver1 = stolong(tmp1);
    ver2 = stolong(tmp2);
    G[ver1] = ver2;
  }

  for (auto i = G.begin(); i != G.end(); ++i) {
    cout << i->first << " => " << i->second << endl;
  }

  return 0;
}