colors = ("red", "yellow", "green")
print(colors[1:2])
# print(colors)
# print(type(colors))
# print(len(colors))
# print(colors[1])
#
# for i in colors :
#     print(i)

# more_colors = ("blue", "brown")
# colors = colors + more_colors
# print(colors)
#
# # UNPACKING A TUPLE
# color1, color2, color3, color4, color5 = colors
# print(color1, color2, color3, color4, color5)

#-------------------- REVERSE A TUPPLE --------------------

num = [10, 11, 12, 13, 14, 15]
new_num = []
for i in reversed(num):
    new_num.append(i)

output_num = tuple(new_num)
print(output_num)
print(type(output_num))