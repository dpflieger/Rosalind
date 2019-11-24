from bisect import bisect_left, bisect_right
import math

def longest_increasing_subsequence(x):
    """Longest increasing subsequence

    :param x: sequence
    :returns: longest strictly increasing subsequence y
    :complexity: `O(|x|*log(|y|))`
    """
    n = len(x)
    p = [None] * n
    h = [None]
    b = [-math.inf]  # - infinity
    for i in range(n):
        #print("n=", n, "p=", p, "h=", h, "b=", b[-1])
        if int(x[i]) > b[-1]:
            p[i] = h[-1]
            h.append(i)
            b.append(int(x[i]))
        else:
            #   -- recherche dichotomique: b[k - 1] < x[i] <= b[k]
            k = bisect_left(b, int(x[i]))
            h[k] = i
            b[k] = int(x[i])
            p[i] = h[k - 1]
    # extraire solution
    q = h[-1]
    s = []
    while q is not None:
        s.append(x[q])
        q = p[q]
    return s[::-1]

def longest_decreasing_subsequence(A):
  m = [0] * len(A)
  for x in range(len(A) - 2, -1, -1):
    for y in range(len(A) - 1, x, -1):
      if int(m[x]) <= int(m[y]) and int(A[x]) > int(A[y]):
        m[x] += 1

  max_value = max(m)

  result = []
  for i in range(len(m)):
    if max_value == m[i]:
      result.append(A[i])
      max_value -= 1

  return result

# The holy grail !
def lgis(X, compare_func):
    piles = []

    for i in X:
        try:
            idx = next(j for j in range(len(piles)) if compare_func(piles[j][-1][0],i))
            piles[idx].append((i,len(piles[idx-1]) if idx > 0 else -1))
        except StopIteration:
            piles.append( [(i,len(piles[-1]) if piles else -1)])

    result = []
    bp = -1
    for i in range(len(piles)-1,-1,-1):
        result.append(piles[i][bp][0])
        bp = piles[i][bp][1]-1

    return result[::-1]


# def lgis(n, π):
#     S = [[]]*(n+1)
#     for i in π:
#         S[i] = max(S[:i], key=len)+[i]
#     return ' '.join(map(str, max(S, key=len)))



if __name__ == '__main__':
    #x = list("51423")
    k = " ".join(open("rosalind_lgis.txt").readlines()[1:])
    k = k.strip().split(" ")
    print(" ".join(longest_increasing_subsequence(k)))
    print(" ".join(longest_increasing_subsequence(k[::-1])[::-1]))

    print(lgis(n, π)) # longest increasing subsequence
    print(lgis(n, reversed(π))[::-1]) # longest decreasing subsequence
