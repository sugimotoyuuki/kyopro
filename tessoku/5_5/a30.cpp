#include <bits/stdc++.h>
using namespace std;
long long m = 1e9 + 7;

long long mod_factorial(long long N) {
  long long mod = 1;
  for (int i = 1; i <= N; ++i) mod = (mod * i) % m;
  return mod;
}

long long power(long long a, long long b, long long m) {
  long long powered = 1;
  for (int i = 0; i < 60; ++i) {
    if (b >> i & 1) powered = ((a % m) * (powered % m)) % m;
    a = ((a % m) * (a % m)) % m;
  }
  return powered;
}

int main() {
  // input
  ifstream in("a30.txt");
  cin.rdbuf(in.rdbuf());

  long long n, r;
  cin >> n >> r;

  long long nume, deno;
  nume = mod_factorial(n);
  deno = mod_factorial(n - r) * mod_factorial(r);

  cout << (nume * power(deno, m - 2, m)) % m << endl;

  return 0;
}