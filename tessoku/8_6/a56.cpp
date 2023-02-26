#include <bits/stdc++.h>

using namespace std;
// primeが大きすぎてはいけない
long long prime = 1001000107;
vector<long long> H, pow100;

long long calc_hash(int s, int e) {
  long long hash = H[e] - (pow100[e - s] * H[s] % prime);
  if (hash < 0) hash += prime;
  return hash;
}

int main() {
  // input
  ifstream in("a56.txt");
  cin.rdbuf(in.rdbuf());

  int N, Q;
  string S;
  cin >> N >> Q >> S;
  vector<pair<long long, long long>> l, r;
  l.push_back(make_pair(-1, -1));
  r.push_back(make_pair(-1, -1));
  for (int i = 1; i <= Q; ++i) {
    int tmpl1, tmpl2, tmpr1, tmpr2;
    cin >> tmpl1 >> tmpl2 >> tmpr1 >> tmpr2;
    l.push_back(make_pair(tmpl1 - 1, tmpl2));
    r.push_back(make_pair(tmpr1 - 1, tmpr2));
  }

  pow100.push_back(1);
  for (int i = 1; i <= N; ++i) {
    pow100.push_back(pow100[i - 1] * 100 % prime);
  }

  H.push_back(0);
  for (int i = 1; i <= N; ++i) {
    long long tmp = (H[i - 1] * 100 + ((long long)S[i - 1] - 96)) % prime;
    H.push_back(tmp);
  }

  for (int i = 1; i <= Q; ++i) {
    long long hash1 = calc_hash(l[i].first, l[i].second);
    long long hash2 = calc_hash(r[i].first, r[i].second);
    if (hash1 == hash2) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }

  return 0;
}