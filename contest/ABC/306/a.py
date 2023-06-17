import heapq as hq

n, k, q = map(int, input().split())
a = list()
ans = 0
for i in range(q):
  _, y = map(int, input().split())
  if len(a) > k:
    if y > a[0]:
      hq.heappushpop(a, y)
      ans += y - a[0]
      print(ans)
  else:
    hq.heappush(a, y)
    ans += y
    print(ans)