from collections import Counter

with open('hits.txt') as f:
    counter=Counter(f.read().strip().replace('\t',' ').split(' '))
print(counter.most_common(5))
