
names = sorted(open('names.txt').read().rstrip().replace('"', '').split(','))
count = lambda word: sum(ord(c)-64 for c in word)
print(names)
total = sum(ln*count(name) for ln, name in enumerate(names,1))
print(total)