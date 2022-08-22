'''Given a sentence as input print all the unique combinations of two words in lexicographical order
explanation:
if given sentence is raju plays cricket the possible combintion of two are (cricket,plays),(cricket,raju),(plays,raju).
input:
raju plays cricket
output:
cricket plays
cricket raju
plays raju'''

from itertools import combinations
lst = input('enter sentece:').split()
lst.sort()
c = list(combinations(lst,2))
for i in c:
    print(' '.join(i))
