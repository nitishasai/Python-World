#qurstion
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=false
#sol

from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    s=input().split()
    fr=' '.join(s[:-1])
    q=int(s[-1])
    try:
        d[fr]=d[fr]+q
    except:
        d[fr]=q
for i,j in d.items():
    print(i,j)
