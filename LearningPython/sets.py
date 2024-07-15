prn_no = {787, 83, 83, 33, 179}
print(prn_no)
#
# for x in prn_no:
#     print(x)
#
# if 83 in prn_no:
#     print("true")
#
# prn_no.add(22)
# print(prn_no)
#
# numbers = [47, 63, 47, 11]
# prn_no.update(numbers)
# print(prn_no)
#
# prn_no.remove(47)
# print(prn_no)
#
# prn_no.discard(87)
# print(prn_no)

s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}

# s3 = s1.union(s2)
# print(s3)

# s1.intersection_update(s2)
# print(s1)

s1.symmetric_difference_update(s2)
print(s1)

