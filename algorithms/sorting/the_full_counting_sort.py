# The Full Counting Sort
N = int(raw_input())
a = []
for i in xrange(N):
    number, word = raw_input().split()
    number = int(number)
    if i < N/2:
        word = "-"
    a.append((number, word))
res = [None] * 100
for number, word in a:
    if res[number] is None:
        res[number] = [word]
    else:
        res[number].append(word)
b = []
for x in res:
    if x is None:
        continue
    b += x
print " ".join(b)