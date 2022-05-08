# a = {5, 5, 4, 4, 3, 2, 1, 0, 0}
# b = []
# for i in range(len(a)):
#     c = min(a)
#     a.remove(c)
#     b.append(c)
# print(b)


l = [70, 3, 45, 86, 1, 89, 3, 89]
list = []
for i in range(len(l)):
    min_of_l = min(l)
    list.insert(i, min_of_l)
    l.remove(min_of_l)
print(list)
