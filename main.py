# Write a function that takes in a positive integer and calculates the sum of multiplication of numbers at the edges
# until you get a single digit number.

# Example :
# Input 78952
# Calculation 7 * 2 + 8 * 5 + 9 = 63
# Calculation 6 * 3 = 18
# Output 1 * 8 = 8


def core(num):
    num = str(num)
    data = [int(i) for i in num]
    if len(data) == 1:
        return data[0]
    j = int(len(num) / 2) + 1
    abc = []
    for i in range(1, j + 1):
        if len(data) == 2:
            print("----")
            abc.append(data[0])
            abc.append(data[1])
            break
        if len(data) % 2 == 1:
            if data[i - 1] == data[-i]:
                abc.append(data[i - 1])
                break
        else:
            if data[i - 1] == data[-(i + 1)]:
                abc.append(data[i - 1] * data[-i])
                break
        da = data[i - 1] * data[-i]
        abc.append(da)

    print(abc)
    if len(abc) == 1:
        return abc[0]
    elif len(abc) == 2:
        a = abc[0] * abc[1]
        print(a)
        if len(str(a)) == 1:
            return a
        else:
            return core(a)
    else:
        res = sum(abc)
        print(res)
        return core(res)


ab = core(num=45387)
print(ab)
