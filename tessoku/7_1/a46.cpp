#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  ifstream in("a46.txt");
  cin.rdbuf(in.rdbuf());

  int N;
  cin >> N;
  double x[N + 1], y[N + 1];
  for (int i = 1; i <= N; ++i) cin >> x[i] >> y[i];

  double dist[N + 2];
  for (int i = 1; i <= N; ++i) dist[i] = 2e9;
  int pos[N + 1]{};
  dist[1] = 0;
  pos[1] = 1;

  for (int i = 2; i <= N; ++i) {
    for (int j = 1; j <= N; ++j) {
      bool exists = find(pos + 1, pos + N + 1, j) != pos + N + 1;
      if (exists) continue;
      if (dist[i] >
          sqrt(pow(x[pos[i - 1]] - x[j], 2) + pow(y[pos[i - 1]] - y[j], 2))) {
        dist[i] =
            sqrt(pow(x[pos[i - 1]] - x[j], 2) + pow(y[pos[i - 1]] - y[j], 2));
        pos[i] = j;
      }
    }
  }

  dist[N + 1] =
      sqrt(pow(x[pos[N]] - x[pos[1]], 2) + pow(y[pos[N]] - y[pos[1]], 2));

  for (int i = 1; i <= N; ++i) { cout << pos[i] << " "; }
  cout << 1 << endl;
  /*double num;
  for (int i = 1; i <= N + 1; ++i) {
    num += dist[i];
    cout << num << " ";
  }*/

  return 0;
}