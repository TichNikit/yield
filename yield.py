from itertools import combinations

def all_variants(text):
    lis = []
    for i in range(1, len(text)+1):
        lis = []
        b = combinations(text, i)
        lis.extend(b)
        for j in lis:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    print(i)

aa = all_variants("my name is Nikita)))")
for i in aa:
    print(i)

# a = combinations('ABCD', 2)
# a = a
#
# for i in a:
#     i = list(i)
#     print(''.join(i))