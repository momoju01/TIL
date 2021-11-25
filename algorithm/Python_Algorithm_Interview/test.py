def test(num, cnt):
  global ans
  L = len(num)
  if L == 0:
    ans = min(ans, cnt)
    return
  elif cnt >= ans:
    return
  else:
    for i in range(L):
      s, e = i, i
      while s >= 0 and e < L and num[s] == num[e]:
        s -= 1
        e += 1
      if s >= 0 and e < L:
        temp = num[:s + 1] + num[e:]
      elif s >= 0:
        temp = num[:s + 1]
      else:
        temp = num[e:]

      test(temp, cnt + 1)


inp = '101110100101011110101'

ans = 16
test(inp, 0)
print(ans)