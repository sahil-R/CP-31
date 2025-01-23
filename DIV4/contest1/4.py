t = int(input())
for _ in range(t):
    s = input()
    cut = 0
    s = s.replace("10", "1B0")
    cut = s.count("B")
    s = s.split("B")
    type1 = 0
    type2 = 0
    type3 = 0
    for item in s:
        if item[0] != item[-1]:
            type3 += 1
        elif item[0] == '0' and item[0] == item[-1]:
            type1 += 1
        else:
            type2 += 1
    if type3 > 1:
        print(type1 + type2 + 2 * type3 - 1)
    else:
        print(type1 + type2 + type3)