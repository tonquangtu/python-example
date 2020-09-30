def solution(n):
    num = long(n)
    count = 0
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = (num - 1) / 2
            if num != 1 and num % 2 == 1:
                num += 1
            count += 2
    return count


print solution('1')
print solution('2')
print solution('3')
print solution('5')
print solution('7')
print solution('9')
print solution('15')
print solution('16')
print solution('768')
print solution('1027')
print solution('12121222222222222222222222222222222222222222222222222222222')
# 0
# 1
# 2
# 3
# 4
# 4
# 5
# 4
# 10
# 12
# 11
