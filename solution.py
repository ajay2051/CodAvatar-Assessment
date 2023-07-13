import math


def reverse(num):
    reversed_number = 0
    while num > 0:
        remainder = num % 10
        reversed_number = reversed_number * 10 + remainder
        num = num // 10
    return reversed_number


def number_length(num):
    if num == 0:
        return 1
    elif num < 0:
        num = -num
    length = math.floor(math.log10(num)) + 1
    return length


def mul(num, ans=0, count=0, exp=0):
    if (num == 0) and (number_length(ans) == 1) and (number_length(exp) == 1):
        final_ans = ans + exp
        if number_length(final_ans) != 1:
            mul(final_ans, 0, 0, 0)
        else:
            return final_ans
    if num == 0:
        ans += exp
        return mul(ans, 0, 0, 0)
    last_num = num % 10
    num = num // 10
    count += 1
    if count == 2:
        exp *= last_num
        count = 0
        pass
    else:
        exp += last_num
        num = reverse(num)
        return mul(num, ans, count, exp)
    ans += exp
    return mul(num, ans, count, exp=0)


print(mul(45625476))
