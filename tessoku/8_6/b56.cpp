#include <bits/stdc++.h>

using namespace std;
long long prime = 900000011;
int N, Q;
long long tmp;
string S;
vector<long long> pow100, H, H_r;

long long calc_hash(int b, int e, bool R) {
  long long hash = 0;
  if (R == true) {
    int b_r = N - e + 1;
    int e_r = N - b + 1;
    hash = H_r[e_r] - (pow100[e_r - b_r + 1] * H_r[b_r - 1] % prime);
  } else {
    hash = H[e] - (pow100[e - b + 1] * H[b - 1] % prime);
  }
  if (hash < 0) hash += prime;
  return hash;
}

int main() {
  // input
  ifstream in("b56.txt");
  cin.rdbuf(in.rdbuf());

  cin >> N >> Q >> S;
  long long L[Q + 1], R[Q + 1];
  for (int i = 1; i <= Q; ++i) { cin >> L[i] >> R[i]; }

  pow100.push_back(1);
  for (int i = 1; i <= N; ++i) {
    pow100.push_back(pow100[i - 1] * 100 % prime);
  }

  H.push_back(0);
  for (int i = 1; i <= N; ++i) {
    tmp = (H[i - 1] * 100 + ((long long)S[i - 1] - 96)) % prime;
    H.push_back(tmp);
  }

  H_r.push_back(0);
  for (int i = N; i >= 1; --i) {
    tmp = (H_r[N - i] * 100 + ((long long)S[i - 1] - 96)) % prime;
    H_r.push_back(tmp);
  }

  for (int i = 1; i <= Q; ++i) {
    long long h = calc_hash(L[i], R[i], false);
    long long h_r = calc_hash(L[i], R[i], true);

    if (h == h_r) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }

  return 0;
}