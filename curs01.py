from collections import Counter
a = input('enter text\t')
# a = 'aaaaadddaadadadfffefecvvaa'
mc = Counter(a)
print(mc.most_common(2))                    # most comon
print(list(mc.elements()))                  # list element
# print(mc.items())
rs = sorted(mc.items())                     # sorted
# print(rs)
for k, v in rs:
    print(k, v)                         # k,v for all elements
