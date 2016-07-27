L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() for s in L]
r = []
for each in L:
    if isinstance(each, str):
        r.append(each)
print [s.lower() for s in r]